from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, Session, sessionmaker

Base = declarative_base()

class Website(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    description = Column(String(50))
    leaning = Column(String(50))
    articles = relationship('Article')
    
    def __init__(self, name = None):
        self.name = name

    # def __init__(self): #does this work 
    #     find_stuff()
    #     update_code()


class Article(Base):
    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    description = Column(String(50))
    tag = Column(String(50))
    text = Column(String(50))
    url = Column(String(50), unique=True)
    website_id = Column(Integer, ForeignKey('website.id'))
 