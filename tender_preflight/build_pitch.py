"""Build the jury PDF deck from the running prototype and verified tender."""

from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader, simpleSplit
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PIL import Image

ROOT = Path(__file__).parent
OUT = ROOT.parent / "output" / "pdf" / "tender_intelligence_pitch.pdf"
OUT.parent.mkdir(parents=True, exist_ok=True)
ASSETS = ROOT / "tests"
W,H = 960,540
INK=HexColor('#102338'); DARK=HexColor('#0c2637'); TEAL=HexColor('#0c6772'); MINT=HexColor('#dce9df'); PAPER=HexColor('#f6f7f3'); ORANGE=HexColor('#f29a6b'); WHITE=HexColor('#ffffff'); GREY=HexColor('#61757c'); RED=HexColor('#b74935')

pdfmetrics.registerFont(TTFont('Segoe','C:/Windows/Fonts/segoeui.ttf'))
pdfmetrics.registerFont(TTFont('SegoeBold','C:/Windows/Fonts/segoeuib.ttf'))

c=canvas.Canvas(str(OUT),pagesize=(W,H),pageCompression=1)
c.setTitle('Tender Intelligence & Risk Engine | NovaTeam')
c.setAuthor('Koussay Jebali - NovaTeam')

def bg(color=PAPER):
    c.setFillColor(color);c.rect(0,0,W,H,fill=1,stroke=0)

def text(x,y,s,size=16,bold=False,color=INK):
    c.setFillColor(color);c.setFont('SegoeBold' if bold else 'Segoe',size);c.drawString(x,y,s)

def para(x,y,s,width,size=17,leading=None,color=INK,bold=False,max_lines=10):
    leading=leading or size*1.42
    lines=simpleSplit(s,'SegoeBold' if bold else 'Segoe',size,width)
    for line in lines[:max_lines]:text(x,y,line,size,bold,color);y-=leading
    return y

def kicker(s,x=54,y=489,color=TEAL):
    text(x,y,s.upper(),11,True,color)

def footer(n,source='CNRE public tender 02/2026, PDF pages cited in slide text'):
    c.setStrokeColor(HexColor('#c8d7d1'));c.line(54,37,906,37)
    text(54,20,'NOVATEAM  /  SOUSSE HACKERSPACE',8,True,GREY)
    text(343,20,source[:93],7,False,GREY)
    text(878,20,f'{n:02d}',9,True,TEAL)

def image_fit(path,x,y,w,h,mode='contain'):
    im=Image.open(path); iw,ih=im.size
    if mode=='cover':
        scale=max(w/iw,h/ih); sw,sh=iw*scale,ih*scale
        c.saveState();p=c.beginPath();p.rect(x,y,w,h);c.clipPath(p,stroke=0,fill=0)
        c.drawImage(ImageReader(im),x+(w-sw)/2,y+(h-sh)/2,sw,sh,mask='auto');c.restoreState()
    else:
        scale=min(w/iw,h/ih);sw,sh=iw*scale,ih*scale
        c.drawImage(ImageReader(im),x+(w-sw)/2,y+(h-sh)/2,sw,sh,mask='auto')

def slide():c.showPage()

# 1 / title
bg(DARK)
kicker('Gomycode x NVIDIA hackathon  /  Guepard AI Automation Award',color=ORANGE)
text(54,400,'TENDER',61,True,WHITE)
text(54,330,'INTELLIGENCE',61,True,WHITE)
text(54,260,'& RISK ENGINE',61,True,ORANGE)
para(57,194,'A practical bid copilot for Tunisia. See the risks, the source, and the next action before you submit.',520,17,26,HexColor('#c9dad7'))
text(57,88,'NovaTeam  /  Koussay Jebali',13,True,WHITE)
text(57,66,'Sousse Hackerspace  /  Tunisia  /  Solo team',11,False,HexColor('#a2b9b6'))
c.setFillColor(MINT);c.roundRect(697,82,217,338,7,fill=1,stroke=0)
image_fit(ASSETS/'evidence.png',704,90,203,322,'cover')
slide()

# 2 / problem
bg();kicker('01 / the problem')
text(54,422,'A good bid can fail before',39,True,INK)
text(54,371,'anyone judges its quality.',39,True,INK)
para(56,315,'This real CNRE tender runs 57 PDF pages. Four missing items can trigger automatic rejection. The guarantee alone has amount, validity, digital copy and physical original rules.',485,18,27,GREY)
text(54,146,'57',70,True,TEAL);text(174,165,'pages to inspect',19,True,INK)
text(54,76,'4',43,True,RED);text(101,89,'automatic rejection categories',16,True,INK)
c.setFillColor(WHITE);c.roundRect(602,80,316,371,6,fill=1,stroke=0)
image_fit(ROOT/'web'/'evidence'/'p9.png',610,86,300,359)
footer(2,'Source: CNRE tender 02/2026, PDF pp. 7, 9')
slide()

# 3 / product
bg(MINT);kicker('02 / the product')
text(54,425,'One workspace for the full bid decision',35,True,INK)
text(54,377,'From the PDF to a reviewable submission room.',18,False,GREY)
steps=[('01','MAP RISK','Identify rejection, financial and contract risks.'),('02','OPEN EVIDENCE','Click a source and inspect the original page.'),('03','TEST A FIX','Change a value and see the projected blocker count.'),('04','PLAN THE BID','Use the tender\'s published scoring rubric.'),('05','PREPARE THE ROOM','Review administrative, technical, financial and guarantee dossiers.')]
y=321
for num,title,desc in steps:
    text(55,y,num,21,True,TEAL);text(118,y,title,16,True,INK);text(118,y-25,desc,12,False,GREY);y-=60
footer(3,'Product workflow in the working local prototype')
slide()

# 4 / risk + evidence
bg(DARK);kicker('03 / a real blocker, with evidence',color=ORANGE)
text(54,418,'The sample bid is missing',36,True,WHITE)
text(54,370,'the 1,000 TND guarantee.',36,True,ORANGE)
para(56,310,'The engine flags the missing copy. A click opens page 7 of the original PDF with the relevant line highlighted.',392,18,27,HexColor('#c8d9d7'))
text(55,174,'1 BLOCKER',23,True,ORANGE)
text(55,140,'Source: CNRE tender, PDF p. 7',12,False,HexColor('#acc5c3'))
text(55,102,'Physical delivery still needs a person.',13,True,WHITE)
c.setFillColor(WHITE);c.roundRect(496,75,421,389,6,fill=1,stroke=0)
image_fit(ASSETS/'evidence.png',502,81,409,377,'cover')
footer(4,'Source: CNRE tender 02/2026, PDF p. 7')
slide()

# 5 / simulator
bg();kicker('04 / bid simulator')
text(54,422,'See the effect before you edit a file',36,True,INK)
para(55,370,'A scenario never changes the uploaded bid. It recomputes the same checks with proposed values.',770,17,25,GREY)
for x,top,value,line in [(55,'AS UPLOADED','MISSING','1 automatic blocker'),(361,'SIMULATE','90 DAYS','Still blocked'),(667,'SIMULATE','120 DAYS','Guarantee field clears')]:
    c.setFillColor(WHITE);c.roundRect(x,140,237,174,6,fill=1,stroke=0)
    text(x+18,281,top,10,True,TEAL);text(x+18,228,value,25,True,INK);text(x+18,184,line,13,False,RED if value!='120 DAYS' else TEAL)
text(55,94,'Then add the demo guarantee: blocker count changes from 1 to 0.',17,True,TEAL)
footer(5,'Prototype scenario; not proof of bank authenticity or delivery')
slide()

# 6 / strategy
bg();kicker('05 / competitive strategy from the tender')
text(54,422,'The published rubric shows where',35,True,INK)
text(54,378,'the proposal needs proof.',35,True,INK)
for x,w,n,label,color in [(54,255,'30','Experience & references',HexColor('#d7e8df')),(311,171,'20','Project approach',HexColor('#add5c8')),(484,423,'50','Proposed team',HexColor('#72b5a7'))]:
    c.setFillColor(color);c.rect(x,233,w,95,fill=1,stroke=0);text(x+18,269,n,36,True,DARK);para(x+83,276,label,w-99,12,16,DARK,True)
para(55,184,'Financial offers are ranked from lowest price. The jury then evaluates technical quality; at least 70/100 is needed.',820,17,26,INK)
text(55,97,'Our strategy assistant turns these published weights into five concrete bid actions.',15,True,TEAL)
footer(6,'Source: CNRE tender 02/2026, PDF pp. 10, 11, 14')
slide()

# 7 / architecture + truth
bg(MINT);kicker('06 / how it works')
text(54,420,'Source first. Automation second.',36,True,INK)
parts=[('PDF INPUT','Extract pages and text from the tender and bid.'),('RULE + AI LAYER','Verified rules decide status. Local Qwen explains a blocker from the clause and bid fact.'),('EVIDENCE GATE','Keep the original page and exact quote beside each model explanation.'),('HUMAN SIGN-OFF','Check originals, signatures, dates and TUNEPS submission.')]
y=348
for i,(head,desc) in enumerate(parts):
    text(57,y,f'{i+1:02d}',18,True,TEAL);text(112,y,head,15,True,INK);para(112,y-24,desc,730,12,17,GREY);y-=75
text(55,56,'Tested local AI: Qwen2.5-1.5B-Instruct via llama.cpp. No API key. Its answer is advisory.',11,True,TEAL)
footer(7,'Prototype architecture and tested-mode disclosure')
slide()

# 8 / closing
bg(DARK);kicker('07 / demo + next step',color=ORANGE)
text(54,426,'Watch one blocker disappear.',39,True,WHITE)
text(54,368,'Keep every manual check visible.',30,True,ORANGE)
para(55,303,'Demo: load the fictional TechVision bid, ask local AI why it is at risk, inspect page 7, simulate 90 versus 120 days, add a sample guarantee, then export the review ZIP.',820,19,28,HexColor('#c8dad8'))
c.setStrokeColor(HexColor('#5c8286'));c.line(54,178,906,178)
text(55,145,'NEXT',11,True,ORANGE)
para(55,113,'Pilot with real bidders; expand tender-specific mapping and evaluate local AI extraction on more public tenders.',770,17,26,WHITE)
text(55,56,'NovaTeam  /  Koussay Jebali  /  Sousse Hackerspace, Tunisia',12,True,HexColor('#a8c6c4'))
slide()

c.save()
print(OUT)
