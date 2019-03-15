from active_alchemy import ActiveAlchemy


db = ActiveAlchemy("sqlite:///foorealtho.db")

def find_dbEntry(dbType, entryName):
    if dbType == 'website':
        site = Website.query().filter(Website.name == entryName).first() # HOW DO I USE WEBSITE WITHOUT THE MODEL.PY
        if site is not None:
            print('1')
            return site.id
        else:
            print('2')
            W = Website.create(name = entryName)
            return W.id
        
