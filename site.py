from models2 import Website, connect, setup, Article
from urllib.parse import urlparse
from newspaper import Article as NA
from sqlalchemy.exc import IntegrityError


class Site:
    
    def find_domain(self, url):
        domain = url
        # domain = urlparse(url).hostname.split('.')[0]
        return domain
    
    def __init__(self, url):
        self.url = url
        self.domain = self.find_domain(url)
        self.website = self.is_site(self.domain)
        if self.website is None:
            session = connect()
            self.website = Website(self.domain)
            session.add(self.website)
            session.commit()
    
    def add_article(self, url):
        try:
            session = connect()
            A = Article(url = url, website_id = self.website.id)
            session.add(A)
            session.commit()
            return A
        except IntegrityError:
            session.rollback()
            return False

    def parse_articles(self):
        for article in self.website.articles:
            try:
                session = connect()
                print(article.url)
                A = NA(article.url)
                A.download()
                A.parse()
                A.nlp()
                # session.query(Article).filter(Article.url == article.url).update({Article.text: A.text}) # 'author' = A.authors, 'description' = A.summary, 'title' = A.title})
                article.text = A.text
                article.author = A.authors
                article.description = A.summary
                article.title = A.title
                session.commit()
                return A.title
            except Exception as e:
                print(e)

    def __str__(self):
        return self.domain +'=' + str(self.website)

    def is_site(self, domain):
        session = connect()
        result = session.query(Website).filter(Website.title == domain).first()
        return result

def test():
    s = Site('https://www.buzzfeed.com/')
    s.add_article('https://www.buzzfeednews.com/article/richardhjames/new-zealand-christchurch-mosque-shooting-terror-attack?bftwuk=&utm_term=4ldqpgm&ref=hpsplash&ref=hpsplash')
    s.parse_articles()
    pass


if __name__ == "__main__":
    test()