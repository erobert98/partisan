from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class Website(Base):
    __tablename__ = 'website'

    id = Column(Integer, primary_key=True)
    title = Column(String(50), unique=True)
    description = Column(String(50))
    leaning = Column(String(50))
    articles = relationship('Article')


    def __init__(self, domain):
        self.title = domain
        Base.__init__(self)


    print()
    def __str__(self):
        return f"{self.id} {self.title} hello"
    # def __init__(self): #does this work 
    #     find_stuff()
    #     update_code()


class Article(Base):
    __tablename__ = 'article'

    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    description = Column(String(50))
    tag = Column(String(50))
    text = Column(String(50))
    url = Column(String(50), unique=True, nullable = False)
    website_id = Column(Integer, ForeignKey('website.id'))


def setup():
    engine = create_engine('sqlite:///foorealtho.db')
    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)
    Base.metadata.create_all(engine)
    print('ok')


def connect():
    engine = create_engine('sqlite:///foorealtho.db',connect_args={'check_same_thread':False})
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

