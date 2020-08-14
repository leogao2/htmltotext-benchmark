import requests
import justext
import os
import shutil
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('lang', help="target language")
parser.add_argument('editor', help="text editor to use, default is vim", default="vim")
args = parser.parse_args()

lang = args.lang
editor = args.editor

while True:
    url = input("enter url: ").strip()
    slug = input("enter name for data in format 'websitetype-title',\ni.e forum-aialignmentforum-FoiiRDC3E$

    html = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit$
    all_paras = [para.text for para in justext.justext(html, justext.get_stoplist("English"))]

    with open('tmp', 'w') as fh:
        fh.write('\n\n'.join(all_paras))
    with open('html', 'wb') as fh:
        fh.write(html)

    os.system(f'{editor} tmp')

    shutil.move('tmp', f'benchmarkdata/{lang}/text/{slug}.txt')
    shutil.move('html', f'benchmarkdata/{lang}/html/{slug}.html')
