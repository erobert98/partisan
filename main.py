from models2 import *
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
    def show(self):
        print('1')
        print(Website)
        print(Website.title)
        # self.name = name
        # return self.name

    # def add_article(self, url):
    #     A = NA(url)
    #     A.download()
    #     A.parse()
    #     A.nlp()
    #     self.update(text = A.text, author = A.authors, description = A.summary, title = A.title)
 
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
    Site(W).show()

if __name__ == "__main__":
    test()