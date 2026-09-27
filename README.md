# Tender Intelligence & Risk Engine — NovaTeam

**Current hackathon project:** a source-linked procurement copilot for the [GOMYCODE x NVIDIA hackathon](https://hackathon.gomycode.com/) and Guepard AI Automation Award. Koussay Jebali is the solo lead at Sousse Hackerspace, Tunisia.

The working app, sample data, tests and submission pack are in [`tender_preflight/`](tender_preflight/README.md). The eight-slide jury PDF is [`output/pdf/tender_intelligence_pitch.pdf`](output/pdf/tender_intelligence_pitch.pdf). The narrated 90-second demo is [`output/video/tender_intelligence_demo.mp4`](output/video/tender_intelligence_demo.mp4).

## Jury links

- [Watch the 90-second demo](https://koussay183.github.io/tender-intelligence-risk-engine/demo.html)
- [View the presentation](https://koussay183.github.io/tender-intelligence-risk-engine/presentation.html)
- [Browse the source code](https://github.com/koussay183/tender-intelligence-risk-engine)

## Quick start

```powershell
cd tender_preflight
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python server.py
```

Open <http://127.0.0.1:8001> and click **Load sample bid**. See one blocking guarantee issue, inspect the original tender page, test 90 and 120 days in the simulator, then add the fictional demo guarantee. The app exports a PDF review and a foldered review ZIP. The local Qwen model is optional to run the core checks; setup and tested behavior are documented in the project README.

## Handoff

- [Detailed project README](tender_preflight/README.md)
- [Test review](tender_preflight/TEST_REVIEW.md)
- [90-second video script](tender_preflight/VIDEO_SCRIPT.md)
- [Form readiness checklist and copyable answers](tender_preflight/FORM_READINESS_CHECKLIST.md)
- [Detailed submission notes](tender_preflight/SUBMISSION.md)
