from active_alchemy import ActiveAlchemy


db = ActiveAlchemy("sqlite:///foorealtho.db")

def find_dbEntry(dbType, entryName):
    if dbType == 'website':
        site = Website.query().filter(Website.name == entryName).first()
        if site is not None:
            return site.id
        else:
            W = Website.create(name = entryName)
            return W.id
        
