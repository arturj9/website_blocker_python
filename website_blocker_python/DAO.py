from Model import Site


class SitesDAO:
    def __new__(cls) -> None:
        if not hasattr(cls, "instance"):
            cls.instance = super(SitesDAO, cls).__new__(cls)
        return cls.instance

    def __init__(self: object) -> None:
        self.__arquivo = "dados/sites.txt"

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
