import platform


class Site:
    def __init__(self: object, url: str) -> None:
        self.__url: str = url
        self.__set_is_blocked__()

    def __set_is_blocked__(self: object) -> None:
        self.__is_blocked = self.verifica_is_blocked()

    def __str__(self) -> str:
        return f"url: {self.__url}, is_blocked: {self.__is_blocked};"

    def __repr__(self) -> str:
        return f"url: {self.__url}, is_blocked: {self.__is_blocked};"

    def get_is_blocked(self: object) -> bool:
        return self.__is_blocked

    def get_url(self: object) -> str:
        return self.__url

    def verifica_is_blocked(self: object) -> bool:
        with open(Host().get_path(), "r+") as hostsfile:
            lines = hostsfile.readlines()
            hostsfile.seek(0)
            for line in lines:
                if self.__url == str(line.replace("\n", "")[10:]):
                    return True
        return False

    def bloquear(self: object) -> bool:
        with open(Host().get_path(), "r+") as hostsfile:
            hosts_content = hostsfile.read()
            if not self.get_is_blocked():
                hostsfile.write(Host().get_redirect() + " " + self.__url + "\n")
            return True
        return False

    def desbloquear(self: object) -> bool:
        with open(Host().get_path(), "r+") as hostsfile:
            lines = hostsfile.readlines()
            hostsfile.seek(0)
            for line in lines:
                if not self.__url == line.replace("\n", "")[10:]:
                    hostsfile.write(line)
            hostsfile.truncate()
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

    def get_path(self: object) -> str:
        return self.__path

    def get_redirect(self: object) -> str:
        return self.__redirect
