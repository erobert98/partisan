from models2 import *
from find_website import find_domain
from newspaper import Article as NA

class Site():
    session = sessionmaker()
    var = session.query(Website).first()
    print(var)
    def __init__(self, name = name):
        self.name = name
        return self.name

    def add_article(self, url):
        A = NA(url)
        A.download()
        A.parse()
        A.nlp()
        self.update(text = A.text, author = A.authors, description = A.summary, title = A.title)
 
        print(Article.get(1))
        # Website = Website.get(self.id)
        # print('ok')



def main(url):
    domain = find_domain(url)
    site = Site(url = url)
    site.add_article(url)
