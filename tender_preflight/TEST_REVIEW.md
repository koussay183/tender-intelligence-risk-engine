# Test review — 27 September 2026

## Result

The prototype passed its tests on the bundled public CNRE 02/2026 tender and fictional TechVision bid. A local Qwen2.5-1.5B-Instruct Q4_K_M model also explained the missing-guarantee risk in the browser. The model's words are advisory; the blocker decision came from the verified rule pack.

| Area | What was checked | Result |
|---|---|---|
| Source integrity | The bundled official tender hash is pinned; 57 pages read; mapped quotes occur on their cited pages | Pass |
| Core rules | No guarantee gives 1 blocker; demo copy with 1,000 TND and 120 days gives 0 mapped blockers and keeps human review items | Pass |
| Scenario simulator | 90-day guarantee stays blocked; 120 days clears the projected blocker without modifying uploaded files | Pass |
| Financial arithmetic | Wrong TTC total triggers a blocker | Pass |
| Unmapped tender | CNRE-specific rules are not applied to a different PDF | Pass |
| Input errors | Invalid and broken PDFs are rejected; textless scanned PDF requests OCR instead of giving false results | Pass |
| Review package | ZIP includes untouched tender/bid originals, unverified guarantee copy, administrative/technical/financial page folders, manifest and report | Pass |
| Browser flow | Sample load, nine risk signals, source highlight, simulator, real recheck, source search, PDF report and ZIP endpoints | Pass |
| Browser errors | Invalid API payload returns HTTP 400; no JavaScript page errors observed | Pass |
| Responsive layout | No horizontal overflow at 390-pixel width, before and after review | Pass |
| Local AI | Qwen via llama.cpp explained one mapped blocker from the page 7 quote and detected bid fact; decision stayed deterministic | Pass |
| PDF output | Eight-slide pitch and three-page sample report rendered and visually inspected | Pass |
| Demo video | Real browser interactions recorded; final MP4 is exactly 90 seconds, 1280×720 H.264/AAC, opens in Chrome, has audible-range narration and visibly clears the blocker | Pass |

Automated checks: **11 Python unit tests**, the browser journey in `tests/browser_check.cjs`, and the local-model browser journey in `tests/browser_ai_check.cjs`.

## How to repeat

```powershell
cd tender_preflight
python -m unittest discover -s tests -q
python server.py
```

In another terminal, with Playwright available:

```powershell
node tests/browser_check.cjs
node tests/browser_ai_check.cjs
```

The AI browser test requires a local Qwen-compatible model served on port 8080 (or a configured Ollama model). The first browser test explicitly turns AI off so the deterministic flow is repeatable.

## What this review does not prove

- A detected guarantee PDF is not a valid bank instrument. The app cannot verify its issuer, authenticity, physical original or actual delivery to CNRE.
- Text detection does not prove signatures, initials, full CV evidence, reference similarity, current TUNEPS deadlines or completed submission.
- The 67% to 75% progress indicator is a transparent weighted checklist: clear = 1, review = 0.5, blocker = 0. It is **not** an eligibility score or a win probability.
- The verified rule pack is for this exact public CNRE PDF. Another tender needs human rule mapping. AI suggestions for unmapped tenders remain drafts.
- Image-only scanned PDFs need OCR, which this prototype does not include.
- The app stores recent analyses only in memory, binds to localhost, and is not publicly deployed. The finished source, presentation and video still need public URLs for submission.

The small 0.5B local model was also tried and produced unreliable summaries. We chose the stronger 1.5B model for the tested explanation and kept compliance decisions independent of model wording.
