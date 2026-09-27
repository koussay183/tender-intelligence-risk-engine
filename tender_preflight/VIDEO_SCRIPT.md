# 90-second demo script

The ready narrated video is `output/video/tender_intelligence_demo.mp4` (from the repository root). This script is for rerecording it in your own voice if desired.

Speak slowly. Record the browser and keep the cursor visible. Use the fictional sample only. Do one practice run and cut pauses.

| Time | Show on screen | Say this |
|---|---|---|
| 0–10 s | Title and Load sample bid | “A company can lose a public tender because one document is missing. Tender Preflight helps us see that risk before we submit.” |
| 10–25 s | Click **Load sample bid** | “This is a real, 57-page Tunisian tender and a fictional company bid. The app turns the tender into a risk map and checks the files we uploaded.” |
| 25–40 s | Show **1 Blocking**. Click **AI explanation**, then the guarantee source. | “It found one automatic rejection risk: the guarantee is missing. Local AI explains why. I can open page seven and see the original rule highlighted.” |
| 40–56 s | Scroll to Bid Simulator, enter guarantee present, 90 days, 1,000 TND; run. Then change to 120 days and run. | “I can test a change without editing the real files. A 90-day guarantee is still blocked. At 120 days, that field clears in the simulation.” |
| 56–69 s | Click **Add demo guarantee**, show **0 Blocking** | “Now I add a fictional guarantee copy and run the real review again. The blocker count goes from one to zero. The app still asks a person to verify the original and the TUNEPS upload.” |
| 69–82 s | Show Submission Room and 30/20/50 rubric | “It also prepares four review folders and shows the tender’s real scoring weights, so the team knows where to add proof.” |
| 82–90 s | Export report or review ZIP, close on title | “We export a source-linked review package. Next, we will test it with more public tenders and real bidders.” |

## Recording notes

- Start the app with `python server.py`, then open `http://127.0.0.1:8001`.
- For the AI demo, start the local Qwen model before the app and leave **Use local AI when available** checked. The test on this machine took a few seconds for the missing-guarantee explanation. If the model is unavailable, show rules mode and replace “Local AI explains why” with “The app explains why from the verified rule.”
- The demo guarantee is **fictional and invalid for real procurement**. Say “fictional copy” on camera.
- Use screen recording at 1080p. Zoom the browser to about 90–100%, keep the app full-screen, and show the PDF highlight clearly.
- Exported report opens in a new tab. Save a copy if you want a still image for the video ending.
- Test the finished video URL in a private browser window before putting it in the form.
