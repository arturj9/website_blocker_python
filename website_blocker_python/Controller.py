from Model import *
from DAO import SitesDAO


class ControleSites:
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(ControleSites, cls).__new__(cls)
        return cls.instance

    def __init__(self: object) -> None:
        self.__sites: list[Site] = SitesDAO().ler()

    def get_sites(self: object) -> list:
        return self.__sites

    def add_site(self: object, site) -> bool:
        if self.verifica_url_existe(site):
            self.__sites.append(site)
            SitesDAO().escrever(self.__sites)
            return True
        return False

    def verifica_url_existe(self: object, site) -> bool:
        for site_in in self.__sites:
            if site.get_url() == site_in.get_url():
                return False
        return True

    def retirar_site(self: object, site) -> bool:
        if not site.get_is_blocked():
            self.__sites.remove(site)
            SitesDAO().escrever(self.__sites)
            return True
        return False
