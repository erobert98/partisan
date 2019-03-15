from active_alchemy import ActiveAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker




def find_dbEntry(dbType, entryName):
    '''
    Given a type of entry and entry name, search it.
    If doesnt exist, creates an entry
    returns the ID of the query

    '''
    db = ActiveAlchemy("sqlite:///foorealtho.db")

    if dbType == 'website':
        try:
            site = db.query(Website).filter(Website.name == entryName)
            for s in site:
                print(s)
            # site = session.query(Website).filter_by(name = entryName).first() # HOW DO I USE WEBSITE WITHOUT THE MODEL.PY
            print(site)            
            if site is not None:
                print('1')
                return site.id
        except Exception as e:
            print(e)
            return False
        
