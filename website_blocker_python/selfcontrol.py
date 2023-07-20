import platform


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
        if site not in self.__sites:
            self.__sites.append(site)
            SitesDAO().escrever(self.__sites)
            return True
        return False

    def retirar_site(self: object, site) -> bool:
        if not self.verifica_site_is_blocked(site):
            self.__sites.remove(site.get_url())
            SitesDAO().escrever(self.__sites)
            return True
        return False

   

class Host:

    def __new__(cls) -> None:
        if not hasattr(cls, "instance"):
            cls.instance = super(Host, cls).__new__(cls)
        return cls.instance

    def __init__(self) -> None:
        if platform.system == "Windows":
            self.__path: str = r"C:\Windows\System32\drivers\etc\hosts"
        else:
            self.__path: str = "/etc/hosts"
        self.__redirect: str = "127.0.0.1"
    
    def get_path(self:object) -> str:
        return self.__path
    
    def get_redirect(self:object) -> str:
        return self.__redirect
    
        


class Site:
    def __init__(self: object, url: str) -> None:
        self.__url: str = url
        self.__set_is_blocked__()

    def __set_is_blocked__(self: object) -> None:
        self.__is_blocked: bool = self.verifica_is_blocked()
    
    def get_is_blocked(self: object) -> bool:
        return self.__is_blocked
    
    def get_url(self:object) -> str:
        return self.__url

    def verifica_is_blocked(self: object) -> bool:
        with open(Host().get_path(), "r+") as hostsfile:
            lines = hostsfile.readlines()
            hostsfile.seek(0)
            for line in lines:
                if self.__url in line:
                    return True
        return False

    def bloquear(self: object) -> bool:
        if site in ControleSites().get_sites():
            with open(Host().get_path(), "r+") as hostsfile:
                hosts_content = hostsfile.read()
                if self.__url not in hosts_content:
                    hostsfile.write(Host.get_redirect() + " " + site + "\n")
                self.__set_is_blocked__()
                return True
            return False
        return False

    def desbloquear(self: object) -> bool:
        if site in ControleSites().get_sites():
            with open(Host().get_path(), "r+") as hostsfile:
                lines = hostsfile.readlines()
                hostsfile.seek(0)
                for line in lines:
                    if not self.__url in line:
                        hostsfile.write(line)
                hostsfile.truncate()
                self.__set_is_blocked__()
                return True
            return False
        return False


class SitesDAO:
    def __new__(cls) -> None:
        if not hasattr(cls, "instance"):
            cls.instance = super(SitesDAO, cls).__new__(cls)
        return cls.instance

    def __init__(self: object) -> None:
        self.__arquivo = "sites.txt"

    def ler(self: object) -> list[Site]:
        sites: list[Site] = list(
            map(
                lambda linha: Site(url=linha.replace("\n", "")),
                open(self.__arquivo, "r").readlines(),
            )
        )
        return sites

    def escrever(self: object, sites: list[Site]) -> bool:
        with open(self.__arquivo, "w") as arq:
            for site in sites:
                arq.write(site.get_url() + "\n")


if __name__ == "__main__":
    c: ControleSites = ControleSites()
    print(c.get_sites())
    c.add_site(Site('hello.com'))
