"""Build a review ZIP, keeping originals and proposed folder assignments."""

import io
import json
import zipfile
from pypdf import PdfReader, PdfWriter

from core import fold
from report import make_report


def classify(page_text: str) -> str:
    text = fold(page_text).upper()
    financial = "OFFRE FINANCIERE" in text or "BORDEREAU DES PRIX" in text
    technical = "OFFRE TECHNIQUE" in text or "CV -" in text
    administrative = "FICHE DE RENSEIGNEMENTS" in text or "ENTREPRISE:" in text
    matches = [name for ok, name in ((financial, "Financial"), (technical, "Technical"), (administrative, "Administrative")) if ok]
    return matches[0] if len(matches) == 1 else "Unsorted"


def make_package(result: dict, tender_data: bytes, proposal_data: bytes, guarantee_data: bytes | None) -> bytes:
    reader = PdfReader(io.BytesIO(proposal_data))
    manifest = {"purpose": "Human review package - not a TUNEPS submission", "tender": result["tender_name"], "decision": result["decision"], "dossiers": result["rooms"], "pages": []}
    output = io.BytesIO()
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as z:
        z.writestr("Originals/tender.pdf", tender_data)
        z.writestr("Originals/bid_pack.pdf", proposal_data)
        if guarantee_data:
            z.writestr("Guarantees/guarantee_copy_UNVERIFIED.pdf", guarantee_data)
        for index, page in enumerate(reader.pages, 1):
            folder = classify(page.extract_text() or "")
            writer = PdfWriter()
            writer.add_page(page)
            buf = io.BytesIO()
            writer.write(buf)
            name = f"{folder}/bid_page_{index:02d}.pdf"
            z.writestr(name, buf.getvalue())
            manifest["pages"].append({"source_page": index, "proposed_folder": folder, "file": name})
        z.writestr("Review/preflight_report.pdf", make_report(result))
        z.writestr("Review/manifest.json", json.dumps(manifest, indent=2, ensure_ascii=False))
        z.writestr("Review/READ_ME_FIRST.txt", "REVIEW PACKAGE ONLY. Folder assignment is proposed from page text. Check every file, signature, date, original guarantee, tender notice and TUNEPS requirements before submitting. This ZIP is not a tender submission.\n")
    return output.getvalue()
