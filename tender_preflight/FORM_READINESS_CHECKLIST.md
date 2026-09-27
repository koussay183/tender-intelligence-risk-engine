# NovaTeam — form readiness checklist

**Submission deadline:** 27 September 2026, 17:30 Tunis time. [Official event schedule](https://hackathon.gomycode.com/). The Google Form is the submission; uploading files elsewhere does not submit the project.

## What is ready

- [x] Working Tender Intelligence & Risk Engine prototype and source code in `tender_preflight/`.
- [x] Eight-slide English presentation: `output/pdf/tender_intelligence_pitch.pdf`.
- [x] Narrated, captioned 90-second demo from real app interactions: `output/video/tender_intelligence_demo.mp4`.
- [x] Public CNRE tender sample, clearly fictional bid pack and guarantee copy.
- [x] README, run commands, limitations and test review.
- [x] Project summary under 150 words, award-fit text and AI/tool disclosure below.

## Still needed before opening the form

- [ ] Confirm the **lead email** used in Final Team Confirmation: `________________________`.
- [x] Publish the actual source code in a public GitHub repository. Source URL: https://github.com/koussay183/tender-intelligence-risk-engine
- [x] Publish the PDF presentation on a viewable GitHub Pages page. Presentation URL: https://koussay183.github.io/tender-intelligence-risk-engine/presentation.html
- [x] Publish the MP4 on a viewable GitHub Pages page. Demo video URL: https://koussay183.github.io/tender-intelligence-risk-engine/demo.html
- [x] Open all three URLs without GitHub authentication. The repository, PDF and MP4 returned HTTP 200; the published Pages passed a signed-out browser test for the 90-second video, captions, presentation and mobile layout on 27 September 2026. Recheck the links once more before pressing Submit.

## Copy into the project form

| Field | Answer |
| --- | --- |
| Team name | NovaTeam |
| Lead / only member | Koussay Jebali |
| Lead email | Use the exact email from Final Team Confirmation |
| Country | Tunisia |
| Space | Sousse Hackerspace |
| Team size | 1 (solo) |
| Project title | Tender Intelligence & Risk Engine |
| Primary prize | Guepard AI Automation Award |
| Additional partner award, if offered | Artefact Data & AI Award |

**Project summary (119 words):**

> Tender Intelligence & Risk Engine helps a Tunisian bidder prepare a public tender with less manual checking. Upload a tender and bid pack to see a risk map, exact source pages, a scenario simulator, and four submission dossiers. The prototype maps 12 requirements in a real 57-page CNRE tender. A fictional bid starts with one automatic rejection risk: a missing 1,000 TND guarantee. A local AI model explains that risk from the verified clause and bid fact. Adding a demo copy clears the blocker while physical delivery and bank authenticity stay in human review. The tender’s published 30/20/50 technical rubric becomes a practical bid focus list. Next, we will test more public tenders with bidders and measure time saved.

**Problem:** Long public tenders hide rejection rules and scoring details across many pages. A small bidder can miss a critical document or focus its proposal on the wrong evidence.

**Solution and key features:** Source-linked risk map; original-page highlight; AI explanation constrained by a verified rule and bid fact; bid change simulator; administrative, technical, financial and guarantee review dossiers; rubric-based proposal focus list; PDF and ZIP exports.

**Technology:** Python, `pypdf`, `pdfplumber`, ReportLab, HTML/CSS/JavaScript, local Qwen2.5-1.5B-Instruct through llama.cpp. No cloud inference API key is required.

**Next step:** Evaluate more public tenders with bidders. Measure review time, missed requirements and false alarms before expanding verified rule coverage.

**Guepard fit:** The workflow turns a long tender and bid files into a risk map, source evidence, simulations and organized review dossiers. The demo traces a missing guarantee to page 7, uses local AI to explain the verified finding, tests a fix and rechecks a fictional copy. A person still signs off on originals and submission.

**Artefact fit, if selected:** The prototype turns public tender text and bid data into actionable, source-linked risk findings and a focused technical bid plan. The demo shows the original evidence and the change in review status after a proposed fix. A supervised pilot will measure time saved and false alarms.

**AI, data and generated-asset disclosure:** The app uses Qwen2.5-1.5B-Instruct Q4_K_M through local llama.cpp to explain a verified missing-guarantee finding. Confirmed checks and simulation results come from deterministic rules; the model cannot change them. OpenAI Codex assisted with research, code, design, slides and fictional demo documents. The 90-second video uses synthetic English narration from Piper `en_US-ljspeech-medium`, trained from a public-domain speech dataset, plus captions. Data comes from the public CNRE 02/2026 tender and clearly fictional TechVision bid files. Generated assets include the slide PDF, sample bid PDFs, source-page previews and video. No private bidder data, cloud inference API, NVIDIA Brev or API keys were used.

## Final submit checks

- [ ] The team name and lead email exactly match Final Team Confirmation.
- [x] The three link fields above contain **public URLs**, not local file paths or `localhost`.
- [ ] The demo video is 90 seconds and shows the app working, including source evidence and the blocker changing from one to zero.
- [ ] The repository README explains setup, model download, sample data, run steps, limits and AI/tool use. No passwords, API keys or vouchers are committed.
- [ ] Select Guepard as primary. Select Artefact only if the current form offers it. The published SupplyzPro challenge is about AI-agent failure analysis, so this procurement prototype does not fit it.
- [ ] Complete every required form field, press **Submit** before 17:30 Tunis time, and save the confirmation.

[Open the project submission form](https://docs.google.com/forms/d/e/1FAIpQLSebmyKeBPv2mrmy4T_wI2_z9SBjjSTZ-O-_ewiWs6PBEikRjw/viewform)

**Demo accuracy note:** The included CNRE tender is a historical public sample. After adding the fictional guarantee, the prototype reports zero *mapped blockers* and six checks for human review. The 67% to 75% progress indicator is checklist completion, not eligibility or a chance of winning. The app does not verify bank authenticity, physical delivery or submission to TUNEPS.
