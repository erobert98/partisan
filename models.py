from active_alchemy import ActiveAlchemy
from sqlalchemy import ForeignKey
from article_grabber import load_info
from find_website import find_site
from db_utility import find_dbEntry


db = ActiveAlchemy("sqlite:///foorealtho.db")

class Website(db.Model):

    name = db.Column(db.String(50))
    description = db.Column(db.String(50))
    leaning = db.Column(db.String(50))
    articles = db.relationship('Article')
    
    # def __init__(self): #does this work 
    #     find_stuff()
    #     update_code()


class Article(db.Model):

    title = db.Column(db.String(50))
    description = db.Column(db.String(50))
    tag = db.Column(db.String(50))
    text = db.Column(db.String(50))
    url = db.Column(db.String(50))
    website_id = db.Column(db.Integer, ForeignKey('website.id'))

    # @classmethod
    def load_info(self):
        text, authors, description, title = load_info(self)
        self.update(text = text, author = authors, description = description, title = title)

    def load_website(self):
        websiteName = find_site(self.url)
        siteID = find_dbEntry('website', websiteName)  #HERE LIES THE PROBLEM 
        if siteID is False:  
            W = Website.create(name = websiteName) #how do i make every website do something upon creation
            self.website_id = W.id
        else:
            self.website_id = siteID
            
        

db.create_all()


