# Jiani (Elva) He — personal website

Personal research and professional portfolio, designed for GitHub Pages.

**Live website:** https://jiani19980225.github.io/

## Edit the website

The published site is plain HTML, CSS, and JavaScript. No package installation or framework build is required to serve it.

- `content.json`: publications, profile links, and the optional Verto Mind role.
- `scripts/build.py`: page text and shared layouts. Run `python3 scripts/build.py` after editing content or templates. Commit the generated HTML files too.
- `assets/styles.css`: colors, typography, responsive layout, and print styles.
- `assets/site.js`: mobile menu, theme preference, publication filters, and citation dialog.
- `scripts/build_cv.py`: public CV PDF generator. Requires `reportlab`. Run after changing the PDF content or research list.

Preview locally with `python3 -m http.server 8000` and open http://localhost:8000.

## Deployment

GitHub Pages serves the repository root from `main`. Updating and pushing the generated files republishes the site. The `.nojekyll` file enables plain static serving.

## Content sources

Professional experience and education: the supplied Jiani He Data Science Consultant resume. The public CV is a newly typeset version with an updated research list; the original attachment and its telephone number are not included in this repository.

Research checked in October 2026:

- Google Scholar: https://scholar.google.com/citations?user=QoV_NDIAAAAJ&hl=en
- https://arxiv.org/abs/2609.02116
- https://arxiv.org/abs/2608.11154
- https://arxiv.org/abs/2607.13331
- https://arxiv.org/abs/2610.27305
- https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7554440

Conference labels reflect public arXiv records; the site distinguishes acceptance/presentation from proceedings publication. The SSRN listing is conservatively labeled as a preprint. The SSRN description is limited to its title/topic. Citation counts are deliberately not hardcoded.

Verto Mind product description: https://testflight.apple.com/join/h7WgfPgM. The product journey is an editorial overview, not an app screenshot. The site claims no unconfirmed founder title or individual product responsibility.

Design: original implementation inspired by the editorial hierarchy and generous spacing of https://yvonnexu442.github.io/research.html. Brand accents use Verto Mind blue `#0077B6` and warm gold-orange `#EB993F`, paired with navy `#102D46`, warm paper `#FAF8F3`, and pale sky `#E0F2FE`. No source code or private assets from the app are included.

The website has no analytics, cookies, external application API calls, or backend. Theme preference is stored locally in the visitor's browser. Google Fonts supplies the display and body fonts, with system fallbacks.
