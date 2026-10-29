// Render the social preview image and touch icon: node scripts/build_images.js (requires Playwright).
const path = require('path');
const { chromium } = require('playwright');

const root = path.resolve(__dirname, '..');
const data = require(path.join(root, 'content.json'));
const fonts = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@500;600&family=Newsreader:ital,opsz,wght@0,6..72,500;1,6..72,400&display=swap">';
const gradient = 'linear-gradient(180deg,#EBF5FD 0%,#E5F2FD 30%,#FBF6EE 68%,#FDF2E2 100%)';
const stats = data.stats.slice(0, 3).map(s => `<div><b>${s.value}</b><span>${s.label}</span></div>`).join('');

const og = `<!doctype html><html><head>${fonts}<style>
*{margin:0;box-sizing:border-box}
body{width:1200px;height:630px;background:${gradient};font-family:Inter,sans-serif;color:#252829;padding:72px 84px;display:flex;flex-direction:column;position:relative;overflow:hidden}
body::after{content:'';position:absolute;right:-120px;top:-120px;width:520px;height:520px;border-radius:50%;border:2px solid rgba(200,150,62,.35)}
.top{display:flex;align-items:center;gap:18px;font-size:22px;font-weight:600;color:#285F96;letter-spacing:.12em;text-transform:uppercase}
.mono{width:64px;height:64px;border-radius:18px;border:2px solid #C8963E;display:grid;place-items:center;font:500 28px Newsreader,serif;letter-spacing:0;color:#252829;background:rgba(255,255,255,.6)}
h1{font:500 100px/1 Newsreader,serif;letter-spacing:-.02em;margin-top:46px}
h1 i{font-weight:400;color:#3375B1;font-size:.55em}
p{font:400 italic 34px/1.3 Newsreader,serif;margin-top:20px;color:#3E4447;max-width:900px}
.stats{display:flex;gap:18px;margin-top:auto}
.stats div{background:rgba(255,255,255,.7);border-radius:20px;padding:18px 24px;display:flex;align-items:baseline;gap:12px;font-size:17px;color:#3E4447;white-space:nowrap}
.stats b{font:500 40px Newsreader,serif;color:#3375B1}
</style></head><body><div class="top"><span class="mono">JH</span>Data science · Research · Applied AI</div><h1>Jiani He <i>(Elva)</i></h1><p>How evidence becomes better operational decisions: forecasting, causal decision support, and AI-assisted reverse logistics.</p><div class="stats">${stats}</div></body></html>`;

const icon = `<!doctype html><html><head>${fonts}<style>
*{margin:0}body{width:180px;height:180px;background:${gradient};display:grid;place-items:center;font:500 76px Newsreader,serif;color:#252829;box-shadow:inset 0 0 0 7px #C8963E}
</style></head><body>JH</body></html>`;

(async () => {
  const proxy = process.env.HTTPS_PROXY ? { server: process.env.HTTPS_PROXY } : undefined;
  const browser = await chromium.launch({ proxy });
  for (const [html, size, file] of [[og, { width: 1200, height: 630 }, 'og-image.png'], [icon, { width: 180, height: 180 }, 'apple-touch-icon.png']]) {
    const page = await browser.newPage({ viewport: size, ignoreHTTPSErrors: true });
    await page.setContent(html, { waitUntil: 'networkidle' });
    await page.evaluate(() => document.fonts.ready);
    await page.screenshot({ path: path.join(root, 'assets', file) });
    await page.close();
  }
  await browser.close();
  console.log('Built assets/og-image.png and assets/apple-touch-icon.png');
})();
