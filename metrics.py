import textdistance
from abc import ABC, abstractmethod
import re

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
        a = set(re.split(r'\s+', true))
        b = set(re.split(r'\s+', predicted))
        return len(a.intersection(b)) / len(a.union(b))

    def lower_is_better(self):
        return False


import difflib
class DiffLines(Metric):
    def name(self):
        return "DiffLines"

    def distance(self, true, predicted):
        # % of word-level diff entries that are either + or -
        diff = list(difflib.ndiff(true.split('\n'), predicted.split('\n')))
        return len([x for x in diff if x[0] != ' ']) / len(diff)

    def lower_is_better(self):
        return True


import difflib
class DiffWords(Metric):
    def name(self):
        return "DiffWords"

    def distance(self, true, predicted):
        # % of word-level diff entries that are either + or -
        diff = list(difflib.ndiff(re.split(r'\s+', true), re.split(r'\s+', predicted)))
        return len([x for x in diff if x[0] != ' ']) / len(diff)

    def lower_is_better(self):
        return True



class LineIOU(Metric):
    def name(self):
        return "Line IOU"

    def distance(self, true, predicted):
        # empty line agnostic
        true = '\n'.join([x.strip() for x in true.split('\n') if x.strip()])
        predicted = '\n'.join([x.strip() for x in predicted.split('\n') if x.strip()])
        a = set(true.split('\n'))
        b = set(predicted.split('\n'))
        return len(a.intersection(b)) / len(a.union(b))

    def lower_is_better(self):
        return False


metrics = [
    WordIOU(),
    #LineIOU(),
    #DiffLines(),
    DiffWords(),
]