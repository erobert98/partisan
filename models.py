from active_alchemy import ActiveAlchemy
from sqlalchemy import ForeignKey
from article_grabber import load_info


db = ActiveAlchemy("sqlite:///fooreal.db")

class Website(db.Model):

    title = db.Column(db.String(50))
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
        text, authors, description = load_info(self)
        self.update(text = text, author = authors, description = description)
        

db.create_all()
