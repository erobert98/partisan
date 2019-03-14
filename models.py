from active_alchemy import ActiveAlchemy
from sqlalchemy import ForeignKey
from article_grabber import load_info
from find_website import find_site


db = ActiveAlchemy("sqlite:///foorealtho.db")

class Website(db.Model):

    name = db.Column(db.String(50))
    description = db.Column(db.String(50))
    leaning = db.Column(db.String(50))
    articles = db.relationship('Article')



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
        siteID = find_dbEntry('website', websiteName)
        print(siteID)
        

db.create_all()

def find_dbEntry(dbType, entryName):
    if dbType == 'website':
        site = Website.query().filter(Website.name == entryName).first()
        if site is not None:
            return site.id
        else:
            W = Website.create(name = entryName)
            return W.id
        


