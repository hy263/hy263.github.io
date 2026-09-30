"""Build the static site into _site/ from _data/*.yml and templates/. Run: python build.py"""
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
common = {'p': p, 'd': d, 'year': today.year, 'updated': today.strftime('%B %Y')}

shutil.rmtree(OUT, ignore_errors=True)
(OUT / 'data').mkdir(parents=True)
shutil.copytree(ROOT / 'assets', OUT / 'assets')
(OUT / 'index.html').write_text(env.get_template('index.html').render(root='./', active='home', **common), encoding='utf-8')
(OUT / 'data/index.html').write_text(env.get_template('data.html').render(root='../', active='data', page_title='Data', **common),
                                     encoding='utf-8')
(OUT / '.nojekyll').write_text('')
print('built', OUT)
