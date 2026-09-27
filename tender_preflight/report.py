"""Human-readable preflight PDF export."""

import io
from pathlib import Path
from xml.sax.saxutils import escape
import reportlab
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.utils import simpleSplit
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether, PageBreak
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

INK = colors.HexColor("#102338")
TEAL = colors.HexColor("#0c6772")
PAPER = colors.HexColor("#f5f4ee")
FONT_DIR = Path(reportlab.__file__).parent / "fonts"
pdfmetrics.registerFont(TTFont("Vera", str(FONT_DIR / "Vera.ttf")))
pdfmetrics.registerFont(TTFont("VeraBd", str(FONT_DIR / "VeraBd.ttf")))
pdfmetrics.registerFontFamily("Vera", normal="Vera", bold="VeraBd")


def make_report(result: dict) -> bytes:
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4, rightMargin=42, leftMargin=42, topMargin=42, bottomMargin=43)
    title = ParagraphStyle("title", fontName="VeraBd", fontSize=22, leading=26, textColor=INK)
    small = ParagraphStyle("small", fontName="Vera", fontSize=8.4, leading=12, textColor=INK)
    heading = ParagraphStyle("heading", fontName="VeraBd", fontSize=11, leading=15, textColor=INK, spaceBefore=12)
    body = ParagraphStyle("body", fontName="Vera", fontSize=9.2, leading=13, textColor=INK)
    story = [Paragraph("Tender Preflight", title), Spacer(1, 8),
             Paragraph("Source-linked bid review | NovaTeam demo", small), Spacer(1, 22)]
    s = result["summary"]
    box = Table([["DECISION", result["decision"]], ["RESULTS", f"{s['blocking']} blocking  /  {s['review']} to review  /  {s['clear']} detected clear"], ["PROGRESS", f"{s['progress_pct']}% checklist progress; not an eligibility score"]], colWidths=[90, 410])
    box.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), PAPER), ("TEXTCOLOR", (0, 0), (-1, -1), INK), ("FONTNAME", (0, 0), (0, -1), "VeraBd"), ("FONTSIZE", (0, 0), (-1, -1), 9), ("BOTTOMPADDING", (0, 0), (-1, -1), 10), ("TOPPADDING", (0, 0), (-1, -1), 10)]))
    story += [box, Spacer(1, 18), Paragraph(f"Tender: {escape(result['tender_name'])}", body), Paragraph(f"Bidder: {escape(result['company'])}", body), Paragraph(f"Engine: {escape(result['engine'])}", body), Paragraph(escape(result["ai_warning"]), small), Spacer(1, 8)]
    if result.get("risks"):
        story.append(Paragraph("Risk map", heading))
        for risk in result["risks"]:
            story.append(Paragraph(f"<b>{escape(risk['kind'])}</b> | {escape(risk['title'])} | {escape(risk['status'])} | source p.{risk['page']}", small))
        story += [Spacer(1, 8), Paragraph("Submission room", heading)]
        for room in result.get("rooms", []):
            story.append(Paragraph(f"<b>{escape(room['name'])}</b> | {escape(room['status'])} | {escape(', '.join(room['items']))}", small))
        story += [Spacer(1, 11), Paragraph("Requirement checks", heading)]
    for check in result["checks"]:
        color = "#a43423" if check["status"] == "blocking" else "#97631a" if check["status"] == "review" else "#0c6772"
        group = [Paragraph(f"<font color='{color}'>{escape(check['status'].upper())}</font>  {escape(check['title'])}", heading),
                 Paragraph(escape(check["evidence"]), body),
                 Paragraph(f"Tender PDF p.{check['page']}: {escape(check['source_quote'])}", small)]
        if check["action"]:
            group.append(Paragraph("Next: " + escape(check["action"]), small))
        story += [KeepTogether(group), Spacer(1, 7)]
    if result.get("strategy"):
        story += [PageBreak(), Paragraph("Bid focus from the published rubric", title), Spacer(1, 10),
                  Paragraph("These are planning prompts from the public CNRE scoring table. Only the jury scores a real bid.", body), Spacer(1, 15)]
        for item in result["strategy"]:
            story += [Paragraph(f"<b>{escape(item['title'])}</b> | {escape(item['weight'])}", heading),
                      Paragraph(escape(item['insight']), body),
                      Paragraph(f"Source: original tender PDF, page {item['page']}", small), Spacer(1, 8)]
    story += [Spacer(1, 14), Paragraph("Human sign-off", heading),
              Paragraph("Confirm originals, signatures, bank authenticity, the current TUNEPS notice and actual submission. A detected section is not proof of eligibility.", body),
              Spacer(1, 14), Paragraph("Reviewer: ____________________    Date: __________", body)]
    def footer(canvas, document):
        canvas.setStrokeColor(TEAL)
        canvas.line(42, 29, 553, 29)
        canvas.setFont("Vera", 8)
        canvas.setFillColor(INK)
        canvas.drawString(42, 17, "NovaTeam | Tender Preflight | human review required")
        canvas.drawRightString(553, 17, str(document.page))
    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    return buffer.getvalue()
