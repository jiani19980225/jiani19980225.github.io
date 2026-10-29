# Jiani (Elva) He — personal website

Research and professional portfolio for GitHub Pages, written so collaborators and recommendation-letter writers can find achievements, papers, and profile links quickly.

**Live website:** https://jiani19980225.github.io/

## Pages

- `index.html`: profile links (Google Scholar, LinkedIn, GitHub, email, CV), achievement stats, a copyable short bio, highlights, research program, selected papers, and Verto Mind.
- `research.html`: the research program: one guiding question, three streams (motivation, origin in practice, problems, papers), and the research journey.
- `publications.html`: all papers grouped by first-author, accepted, and under review, with stream filters, DOIs, code, and BibTeX.
- `experience.html`: experience, education, service and leadership, skills.
- `cv.html` and `assets/Jiani_He_CV.pdf`: web and PDF CV.

## Edit the website

The published site is plain HTML, CSS, and JavaScript. Nothing needs to be installed to serve it.

- `content.json`: all text content: profile links, stats, bio, highlights, research streams, publications, experience, education, skills. Set `photo` to an image path (for example `assets/headshot.jpg`) to replace the monogram with a portrait, and `verto_role` to show a title in the Verto Mind section.
- `scripts/build.py`: page layouts. Run `python3 scripts/build.py` after editing content or templates, and commit the generated HTML files.
- `scripts/build_cv.py`: regenerates the PDF CV from `content.json`. Requires `reportlab`.
- `scripts/build_images.js`: regenerates `assets/og-image.png` (link preview) and `assets/apple-touch-icon.png`. Requires Playwright.
- `assets/styles.css`: palette, typography, layout, dark theme, print styles.
- `assets/site.js`: mobile menu, theme toggle, publication filters, BibTeX dialog, copy-bio button.

Preview locally with `python3 -m http.server 8000` and open http://localhost:8000.

## Design

The palette comes from the Verto Mind app: a sky-blue to champagne background gradient (`#EBF5FD` → `#E5F2FD` → `#FBF6EE` → `#FDF2E2`), steel-blue actions (`#3375B1`), a translucent cream header (`#F2F1E7`), and charcoal headings (`#252829`). A champagne gold (`#C8963E`, with `#8C6422` for small text) marks highlights and first-author work. Type is Newsreader for headings and Inter for text, from Google Fonts with system fallbacks. Page structure is inspired by https://yvonnexu442.github.io/research.html; the code is original.

## Deployment

GitHub Pages serves the repository root from `main`. Pushing the generated files republishes the site. `.nojekyll` enables plain static serving.

## Content sources

- Experience and education: the Jiani He Data Science Consultant resume. The phone number is intentionally left out.
- Papers: public arXiv and SSRN records listed in `content.json`, and the Google Scholar profile https://scholar.google.com/citations?user=QoV_NDIAAAAJ&hl=en.
- Conference details for shared papers (the IEOM late-delivery manuscript, ICOAI submission of the routing paper, ICECCME dates and location, AIBThings full name): co-author Yihua Xu's public website, last verified 2026-10-26.
- Verto Mind: https://testflight.apple.com/join/h7WgfPgM. The phone in the Verto Mind section is an illustration in the app's palette, not a screenshot.

Conference labels describe acceptance or presentation and do not claim final proceedings publication. Citation counts are deliberately not hardcoded. The site has no analytics, cookies, or backend; the theme preference is stored only in the visitor's browser.
