import requests
import justext
import os
import shutil


lang = 'de'

while True:
    url = input().strip()
    slug = input().strip()

    html = requests.get(url).content
    all_paras = [para.text for para in justext.justext(html, justext.get_stoplist("English"))]

    with open('tmp', 'w') as fh:
        fh.write('\n\n'.join(all_paras))
    with open('html', 'wb') as fh:
        fh.write(html)

    os.system('vim tmp')

    shutil.move('tmp', f'benchmarkdata/{lang}/text/{slug}.txt')
    shutil.move('html', f'benchmarkdata/{lang}/html/{slug}.html')