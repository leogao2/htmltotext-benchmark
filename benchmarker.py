from algorithms import algorithms
from metrics import metrics
	
from pytablewriter import MarkdownTableWriter

import os


def mean(x):
    return sum(x) / len(x)


def list_languages():
    return os.listdir('benchmarkdata')


def get_documents_for(lang):
    for doc in os.listdir('benchmarkdata/' + lang + '/html'):
        with open('benchmarkdata/' + lang + '/html/' + doc) as fh, open('benchmarkdata/' + lang + '/text/' + doc[:-4] + 'txt') as fh2:
            yield fh.read(), fh2.read()

values = []

for algo in algorithms:
    row = [algo.name()]
    for metric in metrics:
        scores = []
        for html, true in get_documents_for('en'):
            extract = algo.extract(html)
            score = metric.distance(true, extract)
            scores.append(score)

        row.append(mean(scores))
        print(algo.name(), metric.name(), mean(scores))
    values.append(row)

# bold max value in each column
for col in range(1, len(metrics) + 1):
    coldata = list(map(lambda x: x[col], values))
    maxval = min(coldata) if metrics[col - 1].lower_is_better() else max(coldata)
    for row in range(len(values)):
        if values[row][col] == maxval:
            values[row][col] = '**{:.4f}**'.format(maxval)

# write table
writer = MarkdownTableWriter()
writer.table_name = "Benchmarks ({})".format('en')
writer.headers = ["Algorithm"] + list(map(lambda x: x.name() + '(' + ('L' if x.lower_is_better() else 'H') + ')', metrics))
writer.value_matrix = values

with open('benchmark.md', 'w') as fh:
    fh.write(writer.dumps())
