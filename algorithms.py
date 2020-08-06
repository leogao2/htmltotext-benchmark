from abc import ABC, abstractmethod

class Algorithm(ABC):
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def extract(self, html):
        pass


from newspaper import Article
class Newspaper(ABC):
    def name(self):
        return "Newspaper"

    def extract(self, html):
        article = Article('', fetch_images=False, memoize_articles=False)
        article.set_html(html)
        article.parse()

        return article.text

from justext import justext, get_stoplist
class JusText(ABC):
    def name(self):
        return "JusText"

    def extract(self, html):
        return '\n\n'.join([x.text for x in justext(html, get_stoplist('English')) if not x.is_boilerplate])


algorithms = [
    Newspaper(),
    JusText(),
]