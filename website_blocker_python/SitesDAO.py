from tinydb import TinyDB, Query
from Model import Site

class SitesDAO:

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SitesDAO, cls).__new__(cls)
        return cls.instance

    def __init__(self:object) -> None:
        self.db = TinyDB('db.json')
        self.sites_table = self.db.table('sites')

    def insert(self:object,site:Site) -> bool:
        try:
            self.sites_table.insert({'url':site.__url})
            return True
        except:
            return False
    
    def delete(self:object, site:Site) -> bool:
        self.sites_table.remove(site.__id)
    
    def get_all(self:object) -> list[Site]:
        sites:list[Site] = []
        for site in self.sites_table.all():
            sites.append(Site(site.doc_id,site['url']))
        return sites

if __name__ == '__main__':
    s = SitesDAO()
    print(s.get_all())
    print(s.insert_site())
    print(s.get_all())