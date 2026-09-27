"""Create clearly fictional bid documents for the public demo."""

from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

ROOT = Path(__file__).parent
DATA = ROOT / "data"
DATA.mkdir(exist_ok=True)


def sheet(path: Path, title: str, lines: list[str]):
    c = canvas.Canvas(str(path), pagesize=A4)
    w, h = A4
    def header():
        c.setFillColor(colors.HexColor("#102338"))
        c.rect(0, h - 112, w, 112, fill=1, stroke=0)
        c.setFillColor(colors.white)
        c.setFont("Helvetica-Bold", 21)
        c.drawString(42, h - 61, title)
        c.setFont("Helvetica", 10)
        c.drawString(43, h - 86, "FICTIONAL HACKATHON SAMPLE  |  NOT A REAL BID")
    header()
    y = h - 150
    for line in lines:
        if line == "===PAGE===":
            c.showPage()
            header()
            y = h - 150
            continue
        if y < 72:
            c.showPage()
            header()
            y = h - 150
        heading = line.startswith("#")
        c.setFillColor(colors.HexColor("#0c6772") if heading else colors.HexColor("#253647"))
        c.setFont("Helvetica-Bold" if heading else "Helvetica", 12 if heading else 10.5)
        c.drawString(45, y, line.lstrip("# ")[:100])
        y -= 27 if heading else 22
    c.setFont("Helvetica-Oblique", 9)
    c.setFillColor(colors.HexColor("#b3512a"))
    c.drawString(45, 38, "Synthetic data. Review real originals and the current TUNEPS notice before bidding.")
    c.save()


sheet(DATA / "demo_proposal.pdf", "TechVision Tunisia | Bid pack", [
    "ENTREPRISE: TechVision Tunisia.",
    "SOCIETE: TechVision Tunisia (fictional sample).",
    "# Fiche de renseignements",
    "FICHE DE RENSEIGNEMENTS: donnees de demonstration uniquement.",
    "===PAGE===",
    "# Offre technique",
    "OFFRE TECHNIQUE: campagne multimedia et contenus pedagogiques proposes.",
    "REFERENCE QUALIFIANTE: 45 000 TND TTC - 2024 - projet similaire (fictif).",
    "# Equipe proposee - formulaire T4",
    "CV - CHEF DE PROJET: Amira Ben Salem; coordination; profil fictif.",
    "CV - CONSULTANT REDACTEUR: Sami Trabelsi; redaction; profil fictif.",
    "CV - GRAPHIC DESIGNER: Lina Mansour; design; profil fictif.",
    "CV - MOTION DESIGNER: Youssef Mejri; animation; profil fictif.",
    "===PAGE===",
    "# Offre financiere",
    "OFFRE FINANCIERE: prix en DINAR TUNISIEN (TND).",
    "BORDEREAU DES PRIX: a completer, dater, parapher et signer dans un vrai depot.",
    "TOTAL HT: 80 000 TND",
    "TVA: 15 200 TND",
    "TTC: 95 200 TND",
])

sheet(DATA / "demo_guarantee.pdf", "Demo guarantee copy", [
    "# CAUTION PROVISOIRE - DEMONSTRATION UNIQUEMENT",
    "BANQUE: Banque Exemple (institution fictive, aucun engagement reel).",
    "MONTANT: 1 000 TND",
    "VALIDITE: 120 JOURS",
    "Ce document illustre uniquement la reconnaissance des champs par le prototype.",
    "Il n'est pas une garantie bancaire valable et ne prouve aucune remise physique.",
])

sheet(DATA / "demo_bad_totals.pdf", "Bid pack | wrong total", [
    "ENTREPRISE: TechVision Tunisia.",
    "SOCIETE: TechVision Tunisia.",
    "OFFRE TECHNIQUE: sample.",
    "OFFRE FINANCIERE: sample TND.",
    "REFERENCE QUALIFIANTE: 45 000 TND TTC - 2024 - projet similaire fictif.",
    "CV - CHEF DE PROJET: sample.",
    "CV - CONSULTANT REDACTEUR: sample.",
    "CV - GRAPHIC DESIGNER: sample.",
    "CV - MOTION DESIGNER: sample.",
    "BORDEREAU DES PRIX: sample.",
    "TOTAL HT: 80 000 TND",
    "TVA: 15 200 TND",
    "TTC: 94 200 TND",
])

print("Created fictional proposal, guarantee and wrong-total PDFs in", DATA)
