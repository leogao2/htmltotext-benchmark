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


metrics = [
    WordIOU()
]