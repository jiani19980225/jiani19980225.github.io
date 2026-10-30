// Render the social preview image and touch icon: node scripts/build_images.js (requires Playwright).
const path = require('path');

const root = path.resolve(__dirname, '..');
const data = require(path.join(root, 'content.json'));
const fonts = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@500;600&family=Newsreader:ital,opsz,wght@0,6..72,500;1,6..72,400&display=swap">';
const gradient = 'linear-gradient(180deg,#E5F2FD 0%,#EBF5FD 50%,#FBF8F2 100%)';
const photo = data.photo ? 'data:image/jpeg;base64,' + require('fs').readFileSync(path.join(root, data.photo)).toString('base64') : '';
const stats = data.stats.slice(0, 3).map(s => `<div><b>${s.value}</b><span>${s.short || s.label}</span></div>`).join('');

const og = `<!doctype html><html><head><meta charset="utf-8">${fonts}<style>
*{margin:0;box-sizing:border-box}
body{width:1200px;height:630px;background:${gradient};font-family:Inter,sans-serif;color:#252829;padding:72px 84px;display:flex;flex-direction:column;position:relative;overflow:hidden}
body::after{content:'';position:absolute;right:-120px;top:-120px;width:520px;height:520px;border-radius:50%;border:2px solid rgba(200,150,62,.35)}
.top{display:flex;align-items:center;gap:18px;font-size:22px;font-weight:600;color:#285F96;letter-spacing:.12em;text-transform:uppercase}
.mono{width:64px;height:64px;border-radius:18px;border:2px solid #C8963E;display:grid;place-items:center;font:500 28px Newsreader,serif;letter-spacing:0;color:#E4BB68;background:#17375C}
h1{font:500 100px/1 Newsreader,serif;letter-spacing:-.02em;margin-top:46px}
h1 i{font-weight:400;color:#3375B1;font-size:.55em}
p{font:400 italic 31px/1.3 Newsreader,serif;margin-top:20px;color:#3E4447;max-width:${photo ? 640 : 900}px}
.photo{position:absolute;right:84px;top:64px;width:280px;height:280px;border-radius:50%;padding:6px;background:linear-gradient(140deg,#C8963E,#F3DDAA 45%,#3375B1)}
.photo img{display:block;width:100%;height:100%;border-radius:50%;object-fit:cover;border:5px solid #fff}
.stats{display:flex;gap:18px;margin-top:auto}
.stats div{background:#17375C;border-radius:20px;padding:18px 24px;display:flex;align-items:baseline;gap:12px;font-size:17px;color:#BFCCDB;white-space:nowrap}
.stats b{font:500 40px Newsreader,serif;color:#E4BB68}
</style></head><body><div class="top"><span class="mono">JH</span>Data science · Research · Applied AI</div><h1>Jiani He <i>(Elva)</i></h1><p>${data.social_description || data.positioning}</p><div class="stats">${stats}</div>${photo ? `<div class="photo"><img src="${photo}" alt=""></div>` : ''}</body></html>`;

const icon = `<!doctype html><html><head><meta charset="utf-8">${fonts}<style>
*{margin:0}body{width:180px;height:180px;background:#17375C;display:grid;place-items:center;font:500 76px Newsreader,serif;color:#E4BB68;box-shadow:inset 0 0 0 7px #C8963E}
</style></head><body>JH</body></html>`;

(async () => {
  if (process.argv.includes('--html-only')) {
    require('fs').mkdirSync(path.join(root, 'tmp'), { recursive: true });
    require('fs').writeFileSync(path.join(root, 'tmp', 'social-preview.html'), og);
    console.log('Built tmp/social-preview.html');
    return;
  }
  const { chromium } = require('playwright');
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
