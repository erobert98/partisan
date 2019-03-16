from active_alchemy import ActiveAlchemy
from sqlalchemy import ForeignKey
from find_website import find_site
from db_utility import find_dbEntry
from newspaper import Article as NA
from urllib.parse import urlparse



db = ActiveAlchemy("sqlite:///foorealtho.db")

class Website(db.Model):


    name = db.Column(db.String(50), unique=True)
    description = db.Column(db.String(50))
    leaning = db.Column(db.String(50))
    articles = db.relationship('Article')

    def scrape(self):
        scrape_site()
    
    # def __init__(self): #does this work 
    #     find_stuff()
    #     update_code()


class Article(db.Model):

    title = db.Column(db.String(50))
    description = db.Column(db.String(50))
    tag = db.Column(db.String(50))
    text = db.Column(db.String(50))
    url = db.Column(db.String(50), unique=True)
    website_id = db.Column(db.Integer, ForeignKey('website.id'))
 
    def __init__(self, url, do_update = True):
        self.url = url 
        domain = self.find_site()
        if do_update:
            self.load_info()

    # @classmethod
    def load_info(self):
        A = NA(self.url)
        A.download()
        A.parse()
        A.nlp()
        self.update(text = A.text, author = A.authors, description = A.summary, title = A.title)
   
    def check_website():

    # def get_websiteName(self):
    #     websiteName = self.find_site()
    #     siteID = find_dbEntry('website', websiteName)  #HERE LIES THE PROBLEM 
    #     if siteID is False:  
    #         W = Website.create(name = websiteName) #how do i make every website do something upon creation
    #         self.website_id = W.id
    #     else:
    #         self.website_id = W.id
    #         return W.id
            
        
    def find_site(self):
        domain = urlparse(self.url).hostname.split('.')[1]
        return domain

class repository():

    def is_site(self, name):
        result = db.session.query(Website).filter(Website.name == name).first()


db.create_all()


