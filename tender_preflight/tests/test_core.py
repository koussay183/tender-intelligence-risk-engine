import sys
import io
import json
import unittest
import zipfile
from unittest.mock import patch
from pathlib import Path
from pypdf import PdfWriter

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from core import CNRE_PDF, ai_explain, ai_findings, analyze, cnre_requirements, pdf_pages, simulate
from report import make_report
from package import make_package

DATA = CNRE_PDF.parent
TENDER = CNRE_PDF.read_bytes()
PROPOSAL = (DATA / "demo_proposal.pdf").read_bytes()
GUARANTEE = (DATA / "demo_guarantee.pdf").read_bytes()


class TenderTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base = analyze(TENDER, PROPOSAL, None, False)

    def test_source_quotes_and_page_numbers(self):
        pages = pdf_pages(TENDER)
        self.assertEqual(len(pages), 57)
        for rule in cnre_requirements(pages):
            self.assertIn(rule["source_quote"], pages[rule["page"] - 1])

    def test_missing_guarantee_is_blocking(self):
        self.assertEqual(self.base["summary"]["blocking"], 1)
        self.assertEqual(self.base["decision"], "Blocking issues found")
        self.assertEqual(next(x for x in self.base["checks"] if x["id"] == "guarantee")["page"], 7)

    def test_adding_copy_clears_only_automatic_blocker(self):
        result = analyze(TENDER, PROPOSAL, GUARANTEE, False)
        self.assertEqual(result["summary"]["blocking"], 0)
        self.assertEqual(result["decision"], "Ready for final human review")
        self.assertGreater(result["summary"]["review"], 0)

    def test_simulator_distinguishes_90_and_120_days(self):
        wrong = simulate(self.base, {"guarantee_present": True, "guarantee_amount": 1000, "guarantee_days": 90})
        right = simulate(self.base, {"guarantee_present": True, "guarantee_amount": 1000, "guarantee_days": 120})
        self.assertEqual(wrong["summary"]["blocking"], 1)
        self.assertEqual(right["summary"]["blocking"], 0)
        self.assertTrue(right["simulated"])

    def test_wrong_arithmetic_is_blocking(self):
        result = analyze(TENDER, (DATA / "demo_bad_totals.pdf").read_bytes(), GUARANTEE, False)
        self.assertEqual(next(x for x in result["checks"] if x["id"] == "amounts")["status"], "blocking")

    def test_unknown_tender_not_given_cnre_rules(self):
        result = analyze(PROPOSAL, PROPOSAL, None, False)
        self.assertFalse(result["known_tender"])
        self.assertEqual(result["checks"], [])
        self.assertEqual(result["decision"], "Human mapping required")

    def test_pdf_errors(self):
        with self.assertRaises(ValueError):
            pdf_pages(b"not a pdf")
        with self.assertRaises(ValueError):
            pdf_pages(b"%PDF-broken")
        writer = PdfWriter()
        writer.add_blank_page(width=300, height=300)
        output = io.BytesIO()
        writer.write(output)
        with self.assertRaisesRegex(ValueError, "OCR"):
            pdf_pages(output.getvalue())

    def test_report_is_pdf(self):
        self.assertTrue(make_report(self.base).startswith(b"%PDF-"))

    def test_review_package_preserves_originals_and_sorts_pages(self):
        result = analyze(TENDER, PROPOSAL, GUARANTEE, False)
        data = make_package(result, TENDER, PROPOSAL, GUARANTEE)
        with zipfile.ZipFile(io.BytesIO(data)) as z:
            names = set(z.namelist())
            self.assertIn("Originals/tender.pdf", names)
            self.assertIn("Originals/bid_pack.pdf", names)
            self.assertIn("Guarantees/guarantee_copy_UNVERIFIED.pdf", names)
            self.assertIn("Administrative/bid_page_01.pdf", names)
            self.assertIn("Technical/bid_page_02.pdf", names)
            self.assertIn("Financial/bid_page_03.pdf", names)
            self.assertEqual(z.read("Originals/bid_pack.pdf"), PROPOSAL)
            self.assertEqual(len(json.loads(z.read("Review/manifest.json"))["pages"]), 3)

    def test_local_ai_suggestions_keep_exact_page_quotes(self):
        reply = {"choices": [{"message": {"content": "Check the tender requirement before bidding."}}]}
        class Response(io.BytesIO):
            def __enter__(self):
                return self
            def __exit__(self, *args):
                self.close()
        with patch("core.urlopen", side_effect=lambda *a, **kw: Response(json.dumps(reply).encode())):
            findings = ai_findings(pdf_pages(TENDER), "local", "llama.cpp", True)
        self.assertEqual(len(findings), 5)
        self.assertEqual(findings[0]["source_page"], 7)
        pages = pdf_pages(TENDER)
        self.assertTrue(all(x["source_quote"] in pages[x["source_page"] - 1] for x in findings))

    def test_explain_has_source_and_rules_fallback(self):
        check = next(x for x in self.base["checks"] if x["id"] == "guarantee")
        answer = ai_explain(check, {"available": False})
        self.assertEqual(answer["source_page"], 7)
        self.assertIn("No guarantee PDF", answer["text"])


if __name__ == "__main__":
    unittest.main()
