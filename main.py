from models import *
from find_website import find_domain

class Site(Website):
    def add_article(self):
        '1'.ok()
        print(Article.get(1))
        # Website = Website.get(self.id)
        # print('ok')



def main(url):
    domain = find_domain(url)
    site = Site(url = url)
    site.add_article(url)
