from models2 import connect, Website
from find_website import find_domain
from newspaper import Article as NA


def add_site():
    session = connect()
    # W = Website(name = 'test3')
    # session.add(W)
    # session.commit()
    w1 = session.query(Website).all()
    for w in w1:
        print(w.name)


class Site(Website):
    def __init__(self, Website): #do i need to pull the attributes from db and make a new object to work from?
        self.id = Website.id
        self.title = Website.title
        self.description = Website.description
        self.articles = Website.articles

    def show(self):
        print('showing')
        print(self.id)
        # self.name = name
        # return self.name

    def parse_articles(self):
        for article in self.articles:
            print(article.url)
            A = NA(article.url)
            A.download()
            A.parse()
            A.nlp()
            self.update(text = A.text, author = A.authors, description = A.summary, title = A.title) #how this
    

    #     print(Article.get(1))
    #     # Website = Website.get(self.id)
        # print('ok')



# def main(url):
#     session = connect()
#     W = session.query(Website).first()
#     W.add_article(url)

def test():
    session = connect()
    W = session.query(Website).first()
    site = Site(W)
    site.show()
    site.add_articles()
    pass
if __name__ == "__main__":
    test()


def main(url):
    site = Site(url = url)	
    site.add_article(url)


