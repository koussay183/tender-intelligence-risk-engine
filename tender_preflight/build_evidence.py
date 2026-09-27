"""Render original public-tender pages and map visible source locations."""

import json
import subprocess
from pathlib import Path
import pdfplumber

ROOT = Path(__file__).parent
PDF = ROOT / "data" / "cnre_2026_02.pdf"
OUT = ROOT / "web" / "evidence"
OUT.mkdir(parents=True, exist_ok=True)
POPPLER = Path(r"C:\Users\kouss\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe")

queries = {
    "guarantee": (7, "absence", 0), "reference": (9, "référence", 1),
    "cvs": (9, "CV", 1), "price_schedule": (9, "Bordereau de prix", 0),
    "technical": (5, "offre technique", 0), "financial": (5, "offre financière", 0),
    "language": (6, "langue française", 0), "currency": (6, "Dinar Tunisien", 0),
    "amounts": (6, "TVA", 0), "physical": (7, "original hors ligne", 0),
    "tuneps": (12, "TUNEPS", 0), "rne": (12, "Registre National", 0),
    "strategy_0": (10, "Références à partir de 2021", 0),
    "strategy_1": (10, "Présentation claire", 0),
    "strategy_2": (11, "Chef de projet communication", 0),
    "strategy_3": (14, "classement", 0), "strategy_4": (11, "minimum requis", 0),
    "risk_4": (14, "classement", 0), "risk_5": (11, "minimum requis", 0),
    "risk_6": (11, "Cent vingt", 0), "risk_7": (14, "Vingt", 0),
    "risk_8": (11, "TOTAL 100", 0),
}

mapping = {}
with pdfplumber.open(PDF) as doc:
    for key, (num, term, index) in queries.items():
        page = doc.pages[num - 1]
        found = page.search(term, case=False)
        if not found or index >= len(found):
            print("No evidence location:", key, term)
            continue
        hit = found[index]
        mapping[key] = {"page": num, "x": hit["x0"] / page.width, "y": hit["top"] / page.height,
                        "w": (hit["x1"] - hit["x0"]) / page.width, "h": (hit["bottom"] - hit["top"]) / page.height,
                        "term": hit["text"]}

for num in sorted(set(x["page"] for x in mapping.values())):
    target = OUT / f"p{num}"
    subprocess.run([str(POPPLER), "-f", str(num), "-l", str(num), "-singlefile", "-r", "110", "-png", str(PDF), str(target)], check=True, capture_output=True)

(OUT / "map.json").write_text(json.dumps(mapping, indent=2), encoding="utf-8")
print(f"Rendered {len(set(x['page'] for x in mapping.values()))} public tender pages and mapped {len(mapping)} locations")
