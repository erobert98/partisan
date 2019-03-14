from active_alchemy import ActiveAlchemy
from sqlalchemy import ForeignKey


db = ActiveAlchemy("sqlite:///foo2.db")

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
    website_id = db.Column(db.Integer, ForeignKey('website.id'))

    @classmethod
    def load_text(self):
        print(self.title)

db.create_all()



