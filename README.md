# Jiani (Elva) He — personal website

Research and professional portfolio for GitHub Pages, written so collaborators and recommendation-letter writers can find achievements, papers, and profile links quickly.

**Live website:** https://jiani19980225.github.io/

## Pages

- `index.html`: profile links (Google Scholar, LinkedIn, GitHub, email, CV), achievement stats, a copyable short bio, highlights, research program, and selected papers.
- `research.html`: the research program: one guiding question, why the work matters (with alignment to the U.S. Critical and Emerging Technologies List), three streams (motivation, origin in practice, problems, papers), and the research journey.
- `philosophy.html`: principles for research, working with people, and life.
- `publications.html`: all papers grouped by first-author, accepted, and under review, with stream filters, DOIs, code, and BibTeX.
- `experience.html`: experience, education, service and leadership, skills.
- `cv.html` and `assets/Jiani_He_CV.pdf`: web and PDF CV.

## Edit the website

The published site is plain HTML, CSS, and JavaScript. Nothing needs to be installed to serve it.

- `content.json`: all text content: profile links, stats, bio, highlights, research streams, importance and CET mapping, philosophy, publications, experience, education, skills. `photo` points to the portrait (`assets/headshot.jpg`); leave it empty to show the monogram instead.
- `scripts/build.py`: page layouts. Run `python3 scripts/build.py` after editing content or templates, and commit the generated HTML files.
- `scripts/build_cv.py`: regenerates the PDF CV from `content.json`. Requires `reportlab`.
- `scripts/build_images.js`: regenerates `assets/og-image.png` (link preview) and `assets/apple-touch-icon.png`. Requires Playwright.
- `assets/styles.css`: palette, typography, layout, dark theme, print styles.
- `assets/site.js`: mobile menu, theme toggle, publication filters, BibTeX dialog, copy-bio button.

Preview locally with `python3 -m http.server 8000` and open http://localhost:8000.

## Design

Colors are applied by section: a warm cream page (`#FBF8F2`) with white cards; a sky-blue wash (`#E5F2FD` → `#EBF5FD`) at the top of each page and on alternating sections; a deep steel-navy band (`#17375C`) with champagne-gold figures (`#E4BB68`) for achievements and service; a champagne section (`#FBF6EE` → `#FDF2E2`) for selected papers; a cream header and footer (`#F2F1E7`); steel-blue actions (`#3375B1`); and charcoal headings (`#252829`). Gold (`#C8963E`, with `#8C6422` for small text) marks highlights and first-author work. Type is Newsreader for headings and Inter for text, from Google Fonts with system fallbacks. Page structure is inspired by https://yvonnexu442.github.io/research.html; the code is original.

## Deployment

GitHub Pages serves the repository root from `main`. Pushing the generated files republishes the site. `.nojekyll` enables plain static serving.

## Content sources

- Experience and education: the Jiani He Data Science Consultant resume. The phone number is intentionally left out.
- Portrait: supplied by Jiani He; cropped to a square with image metadata removed.
- Papers: public arXiv and SSRN records listed in `content.json`, and the Google Scholar profile https://scholar.google.com/citations?user=QoV_NDIAAAAJ&hl=en.
- CET alignment: the February 2024 Critical and Emerging Technologies List Update (NSTC/OSTP) for AI subfield names, and Appendix A of the August 2026 National Security Science and Technology Strategy. The mapping to papers is the author's own.
- Conference details for shared papers (the IEOM late-delivery manuscript, ICOAI submission of the routing paper, ICECCME dates and location, AIBThings full name): co-author Yihua Xu's public website, last verified 2026-10-26.

Accepted papers were accepted at conferences that have already taken place; proceedings are forthcoming, and the site does not claim final publication. Citation counts are deliberately not hardcoded. The site has no analytics, cookies, or backend; the theme preference is stored only in the visitor's browser.
