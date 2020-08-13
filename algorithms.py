from abc import ABC, abstractmethod

class Algorithm(ABC):
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def extract(self, html):
        pass


from newspaper import Article
class Newspaper(Algorithm):
    def name(self):
        return "Newspaper"

    def extract(self, html):
        article = Article('', fetch_images=False, memoize_articles=False)
        article.set_html(html)
        article.parse()

        return article.text


from justext import justext, get_stoplist
class JusText(Algorithm):
    def name(self):
        return "JusText"

    def extract(self, html):
        return '\n\n'.join([x.text for x in justext(html, get_stoplist('English')) if not x.is_boilerplate])


import trafilatura
class Trafilatura(Algorithm):
    def name(self):
        return "Trafilatura"

    def extract(self, html):
        return trafilatura.extract(html)


from goose3 import Goose
class Goose3(Algorithm):
    def name(self):
        return "Goose3"

    def extract(self, html):
        g = Goose()
        return g.extract(raw_html=html).cleaned_text


import dragnet
class DragNet(Algorithm):
    def name(self):
        return "DragNet"

    def extract(self, html):
        return dragnet.extract_content_and_comments(html)



class DoNothing(ABC):
    def name(self):
        return "DoNothing"

    def extract(self, html):
        return html


algorithms = [
    Newspaper(),
    JusText(),
    Trafilatura(),
    Goose3(),
    DragNet(),
    DoNothing(),
]