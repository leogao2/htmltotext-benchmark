import textdistance
from abc import ABC, abstractmethod

class Metric(ABC):
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def distance(self, true, predicted):
        pass

    @abstractmethod
    def lower_is_better(self):
        pass


class WordIOU(Metric):
    def name(self):
        return "Word IOU"

    def distance(self, true, predicted):
        a = set(true.split(' '))
        b = set(predicted.split(' '))
        return len(a.intersection(b)) / len(a.union(b))

    def lower_is_better(self):
        return False


import difflib
class DiffWords(Metric):
    def name(self):
        return "DiffWords"

    def distance(self, true, predicted):
        # % of word-level diff entries that are either + or -
        diff = list(difflib.ndiff(true.split(' '), predicted.split(' ')))
        return len([x for x in diff if x[0] != ' ']) / len(diff)

    def lower_is_better(self):
        return True


metrics = [
    WordIOU(),
    DiffWords()
]