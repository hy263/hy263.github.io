# hy263.github.io

Personal academic website of Hyunjoo Yang: https://hy263.github.io

## How to update
- Papers and data sets: edit `_data/papers.yml` (copy an existing entry). On push, GitHub Actions rebuilds and
  publishes the site (about one minute). This also works when editing the file on github.com.
- Name, bio, links, education: edit `_data/profile.yml`.
- CV: edit `cv/cv.tex`, run `latexmk -pdf cv.tex` in `cv/`, and copy `cv/cv.pdf` to `assets/cv.pdf`.
  Keep the working papers in the CV in line with `_data/papers.yml`.
- Layout and style: `templates/` (Jinja2) and `assets/style.css`.
- Local preview: `pip install jinja2 pyyaml && python build.py`, then open `_site/index.html`.
