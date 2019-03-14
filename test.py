from models import *

A = Article.create(title = 'test')
aticle = Article.query().filter(Article.title =='test').first()