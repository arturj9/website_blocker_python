class ControleSites:
    def __init__(self: object) -> None:
        self.__sites: list = self.__ler_sites__()
        self.__hosts_path: str = "/etc/hosts"
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
    

    def __ler_sites__(self: object) -> list:
        sites: list = open("sites.txt", "r").readlines()
        for site in sites:
            sites[sites.index(site)] = site.replace("\n", "")
        return sites
    
    def __escrever_sites__(self:object) -> bool:
        with open("sites.txt", "w") as arq:
            for site in self.__sites:
                arq.write(site + '\n')

    def verifica_site_is_blocked(self: object, site: str) -> bool:
        with open(self.__hosts_path, "r+") as hostsfile:
            lines = hostsfile.readlines()
            hostsfile.seek(0)
            for line in lines:
                if site in line:
                    return True
        return False

    def bloquear_site(self: object, site: str) -> bool:
        if site in self.__sites:
            with open(self.__hosts_path, "r+") as hostsfile:
                hosts_content = hostsfile.read()
                if site not in hosts_content:
                    hostsfile.write(self.__redirect + " " + site + "\n")
                return True
            return False
        return False

    def desbloquear_site(self: object, site: str) -> bool:
        if site in self.__sites:
            with open(self.__hosts_path, "r+") as hostsfile:
                lines = hostsfile.readlines()
                hostsfile.seek(0)
                for line in lines:
                    if not site in line:
                        hostsfile.write(line)
                hostsfile.truncate()
                return True
            return False
        return False


if __name__ == "__main__":
    c: ControleSites = ControleSites()
    print(c.get_sites())
