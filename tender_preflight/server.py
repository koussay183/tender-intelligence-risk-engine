"""Zero-framework local app for a source-linked tender review demo."""

from __future__ import annotations

import base64
import json
import mimetypes
import os
import secrets
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

from core import ai_explain, analyze, ollama_status, simulate
from report import make_report
from package import make_package

ROOT = Path(__file__).parent
WEB = ROOT / "web"
DATA = ROOT / "data"
RESULTS: dict[str, dict] = {}
MAX_REQUEST = 37 * 1024 * 1024


def decode_pdf(payload: dict, key: str, required: bool = True) -> bytes | None:
    raw = payload.get(key)
    if not raw:
        if required:
            raise ValueError(f"{key} PDF is required")
        return None
    try:
        return base64.b64decode(raw, validate=True)
    except (ValueError, TypeError) as exc:
        raise ValueError(f"{key} is not valid base64") from exc


class Handler(BaseHTTPRequestHandler):
    def send_data(self, code: int, data: bytes, content_type: str):
        self.send_response(code)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        try:
            self.wfile.write(data)
        except (BrokenPipeError, ConnectionAbortedError):
            pass

    def json_data(self, code: int, data: dict):
        self.send_data(code, json.dumps(data, ensure_ascii=False).encode("utf-8"), "application/json; charset=utf-8")

    def do_GET(self):
        path = urlparse(self.path).path
        if path == "/api/health":
            return self.json_data(200, {"ok": True, "model": ollama_status()})
        if path.startswith("/api/report/"):
            key = path.rsplit("/", 1)[-1]
            session = RESULTS.get(key)
            if not session:
                return self.json_data(404, {"error": "Report not found in this server session"})
            return self.send_data(200, make_report(session["result"]), "application/pdf")
        if path.startswith("/api/package/"):
            key = path.rsplit("/", 1)[-1]
            session = RESULTS.get(key)
            if not session:
                return self.json_data(404, {"error": "Package not found in this server session"})
            payload = make_package(session["result"], session["tender"], session["proposal"], session["guarantee"])
            return self.send_data(200, payload, "application/zip")
        samples = {"/sample/tender.pdf": "cnre_2026_02.pdf", "/sample/proposal.pdf": "demo_proposal.pdf", "/sample/guarantee.pdf": "demo_guarantee.pdf", "/sample/bad-totals.pdf": "demo_bad_totals.pdf"}
        if path in samples:
            return self.send_data(200, (DATA / samples[path]).read_bytes(), "application/pdf")
        filename = "index.html" if path == "/" else path.lstrip("/")
        target = (WEB / filename).resolve()
        if WEB.resolve() not in target.parents or not target.is_file():
            return self.send_data(404, b"Not found", "text/plain")
        return self.send_data(200, target.read_bytes(), mimetypes.guess_type(str(target))[0] or "application/octet-stream")

    def do_POST(self):
        path = urlparse(self.path).path
        if path not in ("/api/analyze", "/api/simulate", "/api/explain"):
            return self.json_data(404, {"error": "Unknown endpoint"})
        try:
            size = int(self.headers.get("Content-Length", "0"))
            if size <= 0 or size > MAX_REQUEST:
                raise ValueError("Request exceeds 37 MB or is empty")
            payload = json.loads(self.rfile.read(size))
            if path == "/api/explain":
                session = RESULTS.get(str(payload.get("analysis_id", "")))
                if not session:
                    raise ValueError("Run a review before asking for an explanation")
                check = next((x for x in session["result"]["checks"] if x["id"] == payload.get("check_id")), None)
                if not check:
                    raise ValueError("Check not found")
                cache = session.setdefault("explanations", {})
                if check["id"] not in cache:
                    status = ollama_status() if session["result"]["ai_enabled"] and session["result"]["ai_model_ready"] else {"available": False}
                    cache[check["id"]] = ai_explain(check, status)
                return self.json_data(200, cache[check["id"]])
            if path == "/api/simulate":
                session = RESULTS.get(str(payload.get("analysis_id", "")))
                if not session:
                    raise ValueError("Run a review before simulating")
                return self.json_data(200, simulate(session["result"], payload.get("changes", {})))
            tender, proposal, guarantee = decode_pdf(payload, "tender"), decode_pdf(payload, "proposal"), decode_pdf(payload, "guarantee", False)
            result = analyze(tender, proposal, guarantee, bool(payload.get("use_ai", True)))
            key = secrets.token_urlsafe(10)
            RESULTS[key] = {"result": result, "tender": tender, "proposal": proposal, "guarantee": guarantee, "explanations": dict(result["ai_explanations"])}
            if len(RESULTS) > 5:
                RESULTS.pop(next(iter(RESULTS)))
            result["report_url"] = "/api/report/" + key
            result["package_url"] = "/api/package/" + key
            result["analysis_id"] = key
            return self.json_data(200, result)
        except (ValueError, TypeError, KeyError, json.JSONDecodeError) as exc:
            return self.json_data(400, {"error": str(exc)})
        except Exception as exc:
            return self.json_data(500, {"error": f"Analysis failed: {type(exc).__name__}"})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8001"))
    print(f"Tender Preflight at http://127.0.0.1:{port}", flush=True)
    ThreadingHTTPServer(("127.0.0.1", port), Handler).serve_forever()
