# NovaTeam submission pack

For a short, copy-ready checklist with the final video path, see [`FORM_READINESS_CHECKLIST.md`](FORM_READINESS_CHECKLIST.md).

**Deadline:** 27 September 2026, **17:30 Tunis time**, according to the [official event page](https://hackathon.gomycode.com/). Submit early enough to test each link.

## Identity and project card

- **Team:** NovaTeam
- **Country / space:** Tunisia / Sousse Hackerspace
- **Lead and only member:** Koussay Jebali
- **Lead email:** Use the exact email from your Final Team Confirmation.
- **Project title:** Tender Intelligence & Risk Engine
- **Primary prize:** Guepard AI Automation Award
- **Additional award to consider if the form shows it:** Artefact Data & AI Award. The published award is open to teams from all participating countries and recognizes projects that turn data into actionable insights for a real problem. Check the final form for its current selection rules.

### Project summary (under 150 words)

“Tender Intelligence & Risk Engine helps a Tunisian bidder prepare a public tender with less manual checking. Upload a tender and bid pack to see a risk map, exact source pages, a scenario simulator, and four submission dossiers. The prototype maps 12 requirements in a real 57-page CNRE tender. A fictional bid starts with one automatic rejection risk: a missing 1,000 TND guarantee. A local AI model explains that risk from the verified clause and bid fact. Adding a demo copy clears the blocker while physical delivery and bank authenticity stay in human review. The tender’s published 30/20/50 technical rubric becomes a practical bid focus list. Next, we will test more public tenders with bidders and measure time saved.”

### Problem, solution, technology and next step

- **Problem:** Long tenders hide automatic rejection rules and scoring details across many pages. A small team may submit a bid that is incomplete or hard to review.
- **Solution:** Source-linked risk map, bid simulator, evidence view, submission room and rubric-based bid focus list, plus a PDF report.
- **Technology:** Python standard-library HTTP server, `pypdf`, `pdfplumber`, ReportLab, HTML/CSS/JavaScript. Local Qwen2.5-1.5B-Instruct through llama.cpp for plain-English explanations of verified clauses. No cloud API key is required.
- **Next step:** Evaluate on more public tenders and run a supervised pilot with bidders. Measure missed requirements, review time and false alarms.

### Award fit text

**Guepard (primary):** “The workflow turns a 57-page procurement PDF and bid documents into a risk map, source evidence, simulations and organized review dossiers. The demo shows one automatic blocker, asks a local AI model to explain it from the exact page 7 clause, tests a fix and exports a review package. Verified rules and human sign-off control the final decision.”

**Artefact (additional, if available):** “The prototype turns a public 57-page tender and a fictional bid into actionable, source-linked risk findings and a focused technical bid plan. The demo shows a verified rejection risk, the original evidence, and the change in review status after a proposed fix. We will measure review time and missed requirements in a supervised pilot.”

The published SupplyzPro award is specifically for finding recurring failures in AI-agent conversations and tool calls; this procurement prototype does not address that challenge, so do not select it on the current scope.

### Honest AI and tool disclosure

Use the version that matches the recorded demo:

**If the recorded demo is rules mode:** “OpenAI Codex assisted with research, code, design, the presentation and fictional demo documents. The recorded app demo used a verified CNRE rule pack, PDF extraction and deterministic checks. The app can also run a local Qwen model for source-linked explanations, but no model was active in this recording. Public CNRE tender data and clearly fictional bid PDFs were used. NVIDIA Brev was not used.”

**For the ready MP4, recorded with the tested local model running:** “The app used Qwen2.5-1.5B-Instruct Q4_K_M through llama.cpp running locally. It explained the mapped missing-guarantee risk using the exact CNRE page 7 clause and detected bid fact. Confirmed checks, calculations and simulations were deterministic. OpenAI Codex assisted with research, code, design, slides and fictional demo documents. Piper `en_US-ljspeech-medium` generated the English video narration locally from a voice trained on public-domain speech recordings. The source data was the public CNRE 02/2026 PDF; no private bidder data or cloud inference API was used. NVIDIA Brev was not used.”

List any other models or generated assets you actually used. Never paste keys, passwords or vouchers.

**Asset list to disclose:** the 8-slide PDF pitch; fictional TechVision bid and demo guarantee PDFs; rendered page previews and highlight coordinates from the public tender; browser screenshots; a narrated 90-second MP4 recorded from real app interactions. The video narration was synthesized locally with Piper `en_US-ljspeech-medium` from a public-domain speech dataset. The app does not generate a real bank guarantee or submit to TUNEPS.

## Three required public links

1. **Source code URL:** https://github.com/koussay183/tender-intelligence-risk-engine
2. **Presentation URL:** https://koussay183.github.io/tender-intelligence-risk-engine/presentation.html
3. **90-second demo video URL:** https://koussay183.github.io/tender-intelligence-risk-engine/demo.html

The Pages links show the PDF and MP4 in a browser and provide direct file links as a fallback. `VIDEO_SCRIPT.md` is available if you want to record your own voice later.

The Google Form asks for URLs, not file uploads. Docker and a deployed app are optional. The GitHub Pages links host the presentation and video, not the live app; a localhost app address is not accessible to the jury.

## Final form checklist

1. Make sure the team name, lead email, country, space and solo roster exactly match the Final Team Confirmation.
2. Paste the title, summary, problem, solution, features, stack, next step and honest AI disclosure.
3. Select **Guepard AI Automation Award** as primary. Add only eligible partner checkboxes; the country podium is automatic under the event rules.
4. Paste the three tested links. Show a working prototype in the video.
5. Open each link in a signed-out/private window. Confirm source is visible, slides open and video plays.
6. Open the [project submission form](https://docs.google.com/forms/d/e/1FAIpQLSebmyKeBPv2mrmy4T_wI2_z9SBjjSTZ-O-_ewiWs6PBEikRjw/viewform), complete every required field, submit before 17:30 Tunis time and save the confirmation.

The form itself is the submission. Pushing to GitHub or uploading a PDF does not submit the project.
