import platform
from SitesDAO import SitesDAO

class ControleSites:

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ControleSites, cls).__new__(cls)
        return cls.instance

    def __init__(self: object) -> None:
        self.__sites: list = SitesDAO().get_all()
        self.__hosts_path: str = self.__get_path_hosts__()
        self.__redirect: str = "127.0.0.1"

    def get_sites(self: object) -> list:
        return self.__sites

    def add_site(self: object, site: str) -> bool:
        if site not in self.__sites:
            self.__sites.append(site)
            self.__escrever_sites__()
            return True
        return False

    def retirar_site(self: object, site: str) -> bool:
        if not self.verifica_site_is_blocked(site):
            self.__sites.remove(site)
            self.__escrever_sites__()
            return True
        return False
    
    def __get_path_hosts__(self) -> str:
        if platform.system == 'Windows':
            return r"C:\Windows\System32\drivers\etc\hosts"
        return "/etc/hosts"

class Site:

    def __init__(self:object, id:int, url:str) -> None:
        self.__id:int
        if not id is None:
            self.__id = id
        self.__url:str
        self.__is_blocked:bool = verifica_is_blocked()
    
    def verifica_is_blocked(self: object) -> bool:
        with open(ControleSites().__get_path_hosts__(), "r+") as hostsfile:
            lines = hostsfile.readlines()
            hostsfile.seek(0)
            for line in lines:
                if self.__url in line:
                    return True
        return False
    
    def bloquear(self: object) -> bool:
        if site in ControleSites().__sites:
            with open(ControleSites().__get_path_hosts__(), "r+") as hostsfile:
                hosts_content = hostsfile.read()
                if self.__url not in hosts_content:
                    hostsfile.write(ControleSites().__redirect + " " + site + "\n")
                return True
            return False
        return False

    def desbloquear(self: object) -> bool:
        if site in ControleSites().__sites:
            with open(ControleSites().__get_path_hosts__(), "r+") as hostsfile:
                lines = hostsfile.readlines()
                hostsfile.seek(0)
                for line in lines:
                    if not self.__url in line:
                        hostsfile.write(line)
                hostsfile.truncate()
                return True
            return False
        return False

if __name__ == '__main__':
    c = ControleSites()
    print(c.__get_path_hosts__())