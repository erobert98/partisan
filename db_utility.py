from active_alchemy import ActiveAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker




def find_dbEntry(dbType, entryName):
    some_engine = create_engine('sqlite:///foorealtho.db')
    Session = sessionmaker(bind=some_engine)
    session = Session()
    if dbType == 'website':
        try:
            site = session.query('Website').filter_by(name = entryName).first() # HOW DO I USE WEBSITE WITHOUT THE MODEL.PY
            if site is not None:
                print('1')
                return site.id
        except:
            print('2')
            # W = Website.create(name = entryName)
            return False
        
