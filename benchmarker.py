from algorithms import algorithms
from metrics import metrics

import os


def mean(x):
    return sum(x) / len(x)


def list_languages():
    return os.listdir('benchmarkdata')


def get_documents_for(lang):
    for doc in os.listdir('benchmarkdata/' + lang + '/html'):
        with open('benchmarkdata/' + lang + '/html/' + doc) as fh, open('benchmarkdata/' + lang + '/text/' + doc[:-4] + 'txt') as fh2:
            yield fh.read(), fh2.read()

for algo in algorithms:
    for metric in metrics:
        scores = []
        for html, true in get_documents_for('en'):
            extract = algo.extract(html)
            score = metric.distance(true, extract)
            scores.append(score)

        print(algo.name(), metric.name(), mean(scores))