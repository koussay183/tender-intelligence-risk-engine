# NovaTeam — form readiness checklist

**Submission deadline:** 27 September 2026, 17:30 Tunis time. [Official event schedule](https://hackathon.gomycode.com/). The Google Form is the submission; uploading files elsewhere does not submit the project.

## What is ready

- [x] Working Tender Intelligence & Risk Engine prototype and source code in `tender_preflight/`.
- [x] Eight-slide English presentation: `output/pdf/tender_intelligence_pitch.pdf`.
- [x] Narrated, captioned 90-second demo from real app interactions: `output/video/tender_intelligence_demo.mp4`.
- [x] Public CNRE tender sample, clearly fictional bid pack and guarantee copy.
- [x] README, run commands, limitations and test review.
- [x] Project summary under 150 words, award-fit text and AI/tool disclosure below.

## Public links and identity

- [x] Lead email supplied privately by Koussay. Keep the exact address out of the public repository; enter it only in the form.
- [x] Publish the actual source code in a public GitHub repository. Source URL: https://github.com/koussay183/tender-intelligence-risk-engine
- [x] Publish the PDF presentation on a viewable GitHub Pages page. Presentation URL: https://koussay183.github.io/tender-intelligence-risk-engine/presentation.html
- [x] Publish the MP4 on a viewable GitHub Pages page. Demo video URL: https://koussay183.github.io/tender-intelligence-risk-engine/demo.html
- [x] Open all three URLs without GitHub authentication. The repository, PDF and MP4 returned HTTP 200; the published Pages passed a signed-out browser test for the 90-second video, captions, presentation and mobile layout on 27 September 2026. Recheck the links once more before pressing Submit.

## Copy into the project form

| Field | Answer |
| --- | --- |
| Team name | NovaTeam |
| Lead / only member | Koussay Jebali |
| Lead email | Use the privately confirmed Final Team Confirmation email |
| Team members — required field | Koussay Jebali |
| Country | Tunisia |
| Space | Sousse Hackerspace |
| Team size | 1 (solo) |
| Project title | Tender Intelligence & Risk Engine |
| Primary prize | Guepard AI Automation Award |
| Additional partner award, if offered | Artefact Data & AI Award |

**Project summary (119 words):**

> Tender Intelligence & Risk Engine helps a Tunisian bidder prepare a public tender with less manual checking. Upload a tender and bid pack to see a risk map, exact source pages, a scenario simulator, and four submission dossiers. The prototype maps 12 requirements in a real 57-page CNRE tender. A fictional bid starts with one automatic rejection risk: a missing 1,000 TND guarantee. A local AI model explains that risk from the verified clause and bid fact. Adding a demo copy clears the blocker while physical delivery and bank authenticity stay in human review. The tender’s published 30/20/50 technical rubric becomes a practical bid focus list. Next, we will test more public tenders with bidders and measure time saved.

**Problem:** Long public tenders hide rejection rules and scoring details across many pages. A small bidder can miss a critical document or focus its proposal on the wrong evidence.

**Solution and key features — paste as short bullets:**

- Built during the hackathon: upload a tender and bid, see 12 mapped checks and a risk map, inspect the cited original page, test a guarantee change, recheck the bid, and export a PDF report and four review dossiers. See the video at 19–82 seconds.
- The sample company and guarantee are fictional. The simulator changes a scenario, not the uploaded files. Physical originals, bank authenticity, signatures, TUNEPS submission and rule mapping for other tenders still need a person.
- NovaTeam built the workflow, verified CNRE rule pack, UI and exports with Codex assistance. It reused the public CNRE PDF, open-source Python libraries, Qwen model and llama.cpp runtime; model weights are not included in the repository.

**Technology:** Python, `pypdf`, `pdfplumber`, ReportLab, HTML/CSS/JavaScript, local Qwen2.5-1.5B-Instruct through llama.cpp. No cloud inference API key is required.

**Next step:** Evaluate more public tenders with bidders. Measure review time, missed requirements and false alarms before expanding verified rule coverage.

**Guepard fit:** The workflow turns a 57-page tender and bid files into source-linked checks, a risk map, simulations and organized review dossiers. The video shows the page 7 guarantee risk, a local AI explanation, original evidence and a recheck at 19–75 seconds; the code is in `tender_preflight/core.py` and `server.py`. NovaTeam is in Tunisia, and the published Guepard award lists no country restriction; human sign-off still controls the final bid.

**Artefact fit, if selected:** The prototype turns public tender text and bid data into actionable, source-linked risk findings and a focused technical bid plan. The video shows the original evidence at 39–49 seconds and a proposed fix changing the mapped blocker at 67–75 seconds. The published Artefact award is open to all participating countries, including Tunisia; a supervised pilot will measure time saved and false alarms.

**AI/tool disclosure — paste into the required field:** The product uses Qwen2.5-1.5B-Instruct Q4_K_M through local llama.cpp on CPU. For example, input = the verified CNRE page 7 guarantee clause plus the fact that the fictional bid has no guarantee copy; AI action = explain that finding in simple English; output = a source-linked explanation shown at 29–39 seconds in the video. A verified rule pack, not the model, sets check results and simulation status. For an unfamiliar tender, model suggestions remain drafts for human mapping; if the model is offline, the CNRE rule pack still works without AI explanation. OpenAI Codex helped with research, code, UI, slides and fictional demo documents; the rules and quotes were checked against the source, and 11 unit tests plus browser journeys passed. Data: a [public historical CNRE 02/2026 tender](https://www.marchespublics.gov.tn/storage/tender/2026/02/06/a7ba80e0-5885-446b-8ed1-f8ea7287d967_1770391436_e7dc21ec7b4204831508b4942be2a1f1.pdf) and fictional TechVision bid files. Generated assets: the slide PDF, sample bid PDFs, source-page previews and 90-second demo. Piper `en_US-ljspeech-medium` generated the English video narration locally from a voice trained on public-domain speech recordings. No private bidder data, cloud inference API, paid API key or NVIDIA Brev was used; the local model weights are not in the repository.

## Optional supporting fields on the current form

**Project cover / screenshot / logo URL:** https://koussay183.github.io/tender-intelligence-risk-engine/output/video/tender_intelligence_poster.jpg

**Live demo URL:** Leave blank. The app runs locally and is shown working in the 90-second video; the GitHub Pages site hosts the deck and video, not the app.

**Testing, results and known limitations — paste as three bullets:**

- The public 57-page CNRE sample with the fictional bid produced one mapped blocker for the missing guarantee; adding the fictional copy produced zero mapped blockers and six human-review items. See `tender_preflight/TEST_REVIEW.md` and video 19–75 seconds.
- Eleven Python unit tests and browser journeys passed for source highlighting, 90-to-120-day simulation, PDF/ZIP exports and 390-pixel mobile layout. The public video and PDF links were also tested without sign-in. See `tender_preflight/TEST_REVIEW.md`.
- Broken PDFs are rejected, scanned image-only PDFs request OCR, and unfamiliar tenders do not inherit CNRE rules. The app cannot verify bank authenticity, signatures or physical delivery. The local AI needs no paid API key and falls back to verified rules when unavailable.

**Responsible AI and data — paste as 2–4 sentences:** We use a publicly accessible historical CNRE tender and clearly fictional bid documents; no private bidder data is needed for the demo. Each mapped finding links to the original page, model wording cannot change a rule result, and a person must verify originals and submission. Unknown tenders require human rule mapping, and scanned PDFs need OCR; false negatives remain a risk until further evaluation. The narration voice and generated assets are disclosed above, and no secrets are included in the public source.

## Final submit checks

- [ ] The team name and lead email exactly match Final Team Confirmation.
- [x] The three link fields above contain **public URLs**, not local file paths or `localhost`.
- [x] The demo video is 90 seconds and shows the app working, including source evidence and the blocker changing from one to zero.
- [x] The repository README explains setup, model download, sample data, run steps, limits and AI/tool use. No passwords, API keys or vouchers are committed.
- [ ] Select Guepard as primary. Select Artefact only if the current form offers it. The published SupplyzPro challenge is about AI-agent failure analysis, so this procurement prototype does not fit it.
- [ ] Complete every required form field, press **Submit** before 17:30 Tunis time, and save the confirmation.

[Open the project submission form](https://docs.google.com/forms/d/e/1FAIpQLSebmyKeBPv2mrmy4T_wI2_z9SBjjSTZ-O-_ewiWs6PBEikRjw/viewform)

**Demo accuracy note:** The included CNRE tender is a historical public sample. After adding the fictional guarantee, the prototype reports zero *mapped blockers* and six checks for human review. The 67% to 75% progress indicator is checklist completion, not eligibility or a chance of winning. The app does not verify bank authenticity, physical delivery or submission to TUNEPS.
