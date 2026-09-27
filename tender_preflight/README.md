# Tender Intelligence & Risk Engine

NovaTeam's local prototype for the GOMYCODE x NVIDIA hackathon and the Guepard AI Automation Award. Lead: Koussay Jebali, solo entrant, Sousse Hackerspace, Tunisia.

It turns a public 57-page CNRE tender into a source-linked risk review and a practical bid plan. The included **TechVision Tunisia** bid, guarantee, people and bank are fictional demonstration data. The CNRE 02/2026 tender is a historical sample, not a current bidding opportunity.

The finished submission assets are in the repository root: `output/pdf/tender_intelligence_pitch.pdf` and `output/video/tender_intelligence_demo.mp4` (90 seconds, narrated and captioned). `FORM_READINESS_CHECKLIST.md` contains copyable form answers and the remaining public-link checks.

## What works

- Upload the tender, bid pack and optional guarantee PDF. The built-in sample loads in one click.
- See 12 mapped checks, nine risk and information signals, and the published 30/20/50 technical rubric.
- Open the original tender page with a highlighted location for each mapped rule.
- Simulate guarantee presence, amount and validity, or change the TTC total. A scenario does not alter the uploaded files.
- Review four submission dossiers, export a PDF preflight report, and download a ZIP that proposes page folders while preserving the originals.
- Search verified mapped requirements in “Ask the tender.” This source search is **not** a live AI answer.
- Optional local AI explains mapped risks in easy English from the exact source quote and detected bid fact. For an unmapped tender, it can draft candidate actions from exact source excerpts; a person must verify them before rules apply. No API key is required. If the model is unavailable, the verified CNRE rule pack continues to run and the interface says so.

## Run locally

Requires Python 3.11+ and a modern browser.

```powershell
cd tender_preflight
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python server.py
```

Open <http://127.0.0.1:8001>. Click **Load sample bid**. The dashboard should show one blocking guarantee issue. Click its source to inspect page 7. In the simulator, try a 90-day guarantee and then 120 days. Click **Add demo guarantee**; the blocker count becomes zero and the result reads **Ready for final human review**. Export the report and review ZIP. The sample guarantee is deliberately marked invalid for real-world use.

The web app is a Python standard-library server with no build step. `PORT=8001` by default. On PowerShell, use `$env:PORT=8002` before `python server.py` to change it. The server binds to `127.0.0.1`; a reviewer cannot access your localhost. Record it in the video or deploy it before sharing a live link.

## API and architecture

- `GET /api/health`: server and local-model status.
- `POST /api/analyze`: JSON with base64 strings `tender`, `proposal`, optional `guarantee`, and boolean `use_ai`. Returns checks, risk map, rooms, rubric, AI candidates, and report/package URLs.
- `POST /api/simulate`: JSON with `analysis_id` and a `changes` object. It returns a projected result without changing the stored analysis.
- `GET /api/report/{analysis_id}`: PDF review report.
- `GET /api/package/{analysis_id}`: ZIP with original PDFs, proposed page folders, manifest and report.

`core.py` owns document parsing, verified rule mapping, calculations, model calls and simulation. `build_evidence.py` renders source-page images and coordinate maps. `package.py` proposes page folder assignments and preserves originals. `report.py` makes the export PDF. `web/` is the browser UI. All uploads stay in memory for this local demo; the server keeps at most five recent analyses and loses them on restart.

## Optional local AI

The tested demonstration works without a model. The repository also supports a local Ollama server at `127.0.0.1:11434` or a local llama.cpp server at `127.0.0.1:8080`. These run on the user's machine; no provider API key is needed.

Ollama example:

```powershell
ollama pull qwen3:4b-instruct
```

Leave Ollama running, restart the app, and check **Use local AI when available**. Set `$env:OLLAMA_MODEL='your-installed-model-name'` if you use another model. On the mapped CNRE sample, the model explains detected blockers from a verified source quote; it never changes the check result. On a different tender, it writes draft suggestions from excerpts selected directly from that PDF. A person must map those suggestions before the simulator or checks can apply.

For llama.cpp, run its `llama-server` with a compatible GGUF model on port 8080. The app uses the server's local OpenAI-compatible chat endpoint and does not send data to a cloud API. We tested [Qwen2.5-1.5B-Instruct Q4_K_M](https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct-GGUF/blob/main/qwen2.5-1.5b-instruct-q4_k_m.gguf) with the official llama.cpp Windows CPU build. The model file is about 1.12 GB and is not committed to the repository. Its publisher lists an Apache-2.0 license. Start it with a command like:

```powershell
llama-server -m path\to\qwen2.5-1.5b-instruct-q4_k_m.gguf -c 4096 --host 127.0.0.1 --port 8080
```

On this development machine, the tested binaries and model are in the repository's ignored `tmp/llama/` folder. From the repository root, the exact command is:

```powershell
& 'tmp\llama\bin\llama-server.exe' -m 'tmp\llama\qwen2.5-1.5b-instruct-q4_k_m.gguf' -c 4096 --host 127.0.0.1 --port 8080 --threads 8
```

Leave that terminal running and start `tender_preflight/server.py` in another. The model weights are not included in GitHub source. The downloaded model's SHA-256 was `6a1a2eb6d15622bf3c96857206351ba97e1af16c30d7a74ee38970e434e9407e`.

Model quality and licensing depend on which model you install.

**Tested AI path:** The 1.5B model ran locally and explained the sample missing-guarantee blocker using the exact page 7 clause and detected bid fact. The rules-only path and all sample browser flows were also tested. If the model is not running when you record, say that the recording shows rules mode.

## Tests

```powershell
python -m unittest discover -s tests -v
```

The browser test uses Playwright and Chrome:

```powershell
node tests/browser_check.cjs
```

It checks initial rejection, source dialog and highlight, simulation, real recheck after adding the sample guarantee, source search, and mobile overflow. If Playwright is missing, install it only for browser testing; it is not required to run the app.

## Source and method

- Official public tender: [CNRE Appel d'offres 02/2026](https://www.marchespublics.gov.tn/storage/tender/2026/02/06/a7ba80e0-5885-446b-8ed1-f8ea7287d967_1770391436_e7dc21ec7b4204831508b4942be2a1f1.pdf).
- Key PDF pages: p.7 guarantee and physical original; p.9 automatic rejection grounds; pp.10–11 technical rubric and 70/100 threshold; p.14 financial ranking and post-award formalities.
- `core.py` hashes the included official PDF. CNRE-specific rules apply only when the uploaded tender exactly matches that file. Another tender receives candidate AI findings when a local model is installed, but requires human mapping before the simulator can be used.
- The quote and page pointers are auditable. The highlight is a location cue on a rendered page; read the full source clause in context.

## Boundaries

The app cannot authenticate a bank guarantee, determine whether a reference is truly similar, read handwritten signatures reliably, prove physical delivery, verify current TUNEPS deadlines, submit a bid, or assign the jury's technical score. It never calls a bid legally compliant or predicts that it will win. “Ready for final human review” means no mapped automatic blocker remains in the supplied PDFs; it does not mean submission is complete.

The ZIP is a **review aid**, not a TUNEPS-ready submission. A page that mixes categories goes to `Unsorted`, and each proposed page folder must be checked by a person.

No NVIDIA Brev credits or infrastructure were used. No private bidder data was needed for the public demo.

OpenAI Codex assisted with research, design, coding, writing and generation of the fictional sample PDFs and presentation. The runtime model tested here was Qwen2.5-1.5B-Instruct Q4_K_M through local llama.cpp. There is no cloud inference API call in the app. Rendered source-page PNGs and screenshots are generated assets from the public tender and prototype UI.
