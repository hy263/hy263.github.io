"""Build the site into _site/ from _data/*.yml and templates/. Run: python build.py
Pages: home, working papers, publications, data, CV (one folder each). The CV page shows the PDF in profile.yml
with a download button."""
import datetime
import pathlib
import shutil

import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = pathlib.Path(__file__).parent
OUT = ROOT / '_site'
p = yaml.safe_load((ROOT / '_data/profile.yml').read_text(encoding='utf-8'))
d = yaml.safe_load((ROOT / '_data/papers.yml').read_text(encoding='utf-8'))
env = Environment(loader=FileSystemLoader(ROOT / 'templates'), autoescape=select_autoescape(['html']))
today = datetime.date.today()
cv = next(l['url'] for l in p['links'] if l['label'] == 'CV')

PAGES = [  # key, menu label, folder ('' = home), template
    ('home', 'Main', '', 'index.html'),
    ('working-papers', 'Working Papers', 'working-papers/', 'working_papers.html'),
    ('publications', 'Publications', 'publications/', 'publications.html'),
    ('data', 'Data', 'data/', 'data.html'),
    ('cv', 'CV', 'cv/', 'cv.html'),
]
menu = [(k, lab, path) for k, lab, path, _ in PAGES]

shutil.rmtree(OUT, ignore_errors=True)
OUT.mkdir()
shutil.copytree(ROOT / 'assets', OUT / 'assets')
for key, label, path, tpl in PAGES:
    root = '../' * path.count('/')
    html = env.get_template(tpl).render(p=p, d=d, menu=menu, active=key, root=root or './',
                                        page_title=None if key == 'home' else label, cv=cv,
                                        year=today.year, updated=today.strftime('%B %Y'))
    (OUT / path).mkdir(parents=True, exist_ok=True)
    (OUT / path / 'index.html').write_text(html, encoding='utf-8')
(OUT / '.nojekyll').write_text('')
print('built', OUT)
