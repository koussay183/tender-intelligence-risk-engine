const assert = require('node:assert/strict');
const fs = require('node:fs');
const { chromium } = require('playwright');

const base = (process.env.PUBLIC_BASE || 'http://127.0.0.1:8012').replace(/\/$/, '');
fs.mkdirSync('tmp/pages_qa', { recursive: true });

(async () => {
  const browser = await chromium.launch({ headless: true, executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe' });
  const desktop = await browser.newPage({ viewport: { width: 1440, height: 900 } });
  await desktop.goto(`${base}/index.html`, { waitUntil: 'networkidle' });
  await desktop.getByRole('heading', { name: /Tender Intelligence/ }).waitFor();
  assert.equal(await desktop.evaluate(() => document.documentElement.scrollWidth > innerWidth), false);
  await desktop.screenshot({ path: 'tmp/pages_qa/index_desktop.png', fullPage: true });

  const mobile = await browser.newPage({ viewport: { width: 390, height: 844 } });
  await mobile.goto(`${base}/index.html`, { waitUntil: 'networkidle' });
  assert.equal(await mobile.evaluate(() => document.documentElement.scrollWidth > innerWidth), false);
  await mobile.getByRole('link', { name: /Watch the 90-second demo/ }).waitFor();
  await mobile.screenshot({ path: 'tmp/pages_qa/index_mobile.png', fullPage: true });

  await desktop.goto(`${base}/demo.html`, { waitUntil: 'networkidle' });
  const media = await desktop.locator('video').evaluate(async video => {
    if (video.readyState < 1) await new Promise(resolve => video.addEventListener('loadedmetadata', resolve, { once: true }));
    return { duration: video.duration, width: video.videoWidth, height: video.videoHeight, error: video.error?.message || null };
  });
  assert.deepEqual(media, { duration: 90, width: 1280, height: 720, error: null });
  const vtt = await desktop.request.get(`${base}/output/video/tender_intelligence_demo.vtt`);
  assert.equal(vtt.status(), 200);
  assert.match(await vtt.text(), /^WEBVTT/);
  await desktop.screenshot({ path: 'tmp/pages_qa/demo_desktop.png', fullPage: true });

  await desktop.goto(`${base}/presentation.html`, { waitUntil: 'networkidle' });
  const pdf = await desktop.request.get(`${base}/output/pdf/tender_intelligence_pitch.pdf`);
  assert.equal(pdf.status(), 200);
  assert.equal((await pdf.body()).subarray(0, 5).toString(), '%PDF-');
  await desktop.screenshot({ path: 'tmp/pages_qa/presentation_desktop.png', fullPage: true });
  await browser.close();
  console.log(`PASS public pages at ${base}: desktop/mobile layout, 90s MP4, captions, PDF`);
})().catch(error => { console.error(error); process.exit(1); });
