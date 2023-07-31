import sys
from PySide6 import QtCore, QtWidgets, QtGui
from Controller import ControleSites
from Model import Site


class AreaInput(QtWidgets.QWidget):
    def __init__(self: object, janela_principal) -> None:
        super().__init__()

        self.__set_atributos__(janela_principal)
        self.__set_button__()
        self.__set_layout__()

    def __set_atributos__(self: object, janela_principal) -> None:
        self.__button = QtWidgets.QPushButton("Adicionar")
        self.__input = QtWidgets.QLineEdit()
        self.__janela_principal = janela_principal
        self.__layout = QtWidgets.QHBoxLayout(self)

    def __set_layout__(self: object) -> None:
        self.__layout.addWidget(self.__input)
        self.__layout.addWidget(self.__button)

    def __set_button__(self: object) -> None:
        self.__button.setStyleSheet("color:gray;")
        self.__button.clicked.connect(self.__adicionar__)

    @QtCore.Slot()
    def __adicionar__(self: object) -> None:
        if self.__input.text():
            site = Site(self.__input.text())
            self.__janela_principal.get_controle_sites().add_site(site)
            self.__janela_principal.get_area_sites().add_site_label(site)
            self.__input.clear()


class AreaSites(QtWidgets.QWidget):
    def __init__(self: object, janela_principal) -> None:
        super().__init__()

        self.__set_atributos__(janela_principal)

        for site in self.__janela_principal.get_controle_sites().get_sites():
            self.add_site_label(site)

    def __set_atributos__(self: object, janela_principal) -> None:
        self.__janela_principal = janela_principal
        self.__layout = QtWidgets.QVBoxLayout(self)

    def add_site_label(self: object, site: Site) -> bool:
        self.__layout.addWidget(
            SiteLabel(site, self.__janela_principal.get_controle_sites())
        )


class SiteLabel(QtWidgets.QWidget):
    def __init__(self: object, site: Site, controle_sites: ControleSites):
        super().__init__()

        self.__set_atributos___(site, controle_sites)
        self.__set_button_status__()
        self.__set_layout__()
        self.__set_buttons__()

    def __set_atributos___(
        self: object, site: Site, controle_sites: ControleSites
    ) -> None:
        self.__site = site
        self.__controle_sites = controle_sites
        self.__layout = QtWidgets.QHBoxLayout(self)
        self.__text = QtWidgets.QLabel(self.__site.get_url())
        self.__button_remover = QtWidgets.QPushButton("Remover")
        self.__button_status = QtWidgets.QPushButton("")

    def __set_layout__(self: object) -> None:
        self.__layout.addWidget(self.__text)
        self.__layout.addWidget(self.__button_status)
        self.__layout.addWidget(self.__button_remover)

    def __set_button_status__(self: object) -> None:
        if self.__site.get_is_blocked():
            self.__button_status.setText("Bloqueado")
            self.__button_status.setStyleSheet("background-color: black; color: white;")
            self.__button_remover.setEnabled(False)
            self.__button_remover.setStyleSheet("background-color: gray;")
        else:
            self.__button_status.setText("Desbloqueado")
            self.__button_status.setStyleSheet("background-color: white; color: black;")
            self.__button_remover.setEnabled(True)
            self.__button_remover.setStyleSheet("background-color: red;")

    def __set_buttons__(self: object) -> None:
        self.__button_remover.clicked.connect(self.__remover__)
        self.__button_status.clicked.connect(self.__change_status__)

    @QtCore.Slot()
    def __change_status__(self: object) -> None:
        if self.__site.get_is_blocked():
            self.__site.desbloquear()
        else:
            self.__site.bloquear()
        self.__site.__set_is_blocked__()
        self.__set_button_status__()

    @QtCore.Slot()
    def __remover__(self: object) -> None:
        self.__controle_sites.retirar_site(self.__site)
        self.setParent(None)
        self.deleteLater()


class JanelaPrincipal(QtWidgets.QWidget):
    def __init__(self: object, w: int, h: int) -> None:
        super().__init__()

        self.setFixedSize(w, h)
        self.setWindowTitle("Bloqueador de Sites")

        self.__set_atributos__()
        self.__set_layout__()

        self.show()

    def __set_atributos__(self: object) -> None:
        self.__controle_sites = ControleSites()
        self.__area_input = AreaInput(self)
        self.__area_sites = AreaSites(self)
        self.__layout = QtWidgets.QVBoxLayout(self)

    def __set_layout__(self: object) -> None:
        self.__layout.addWidget(self.__area_input, alignment=QtCore.Qt.AlignVCenter)
        self.__layout.addWidget(self.__area_sites, alignment=QtCore.Qt.AlignTop)

    def get_controle_sites(self: object) -> ControleSites:
        return self.__controle_sites

    def get_area_input(self: object) -> AreaInput:
        return self.__area_input

    def get_area_sites(self: object) -> AreaSites:
        return self.__area_sites

    def get_layout(self: object) -> QtWidgets.QVBoxLayout:
        return self.__layout


class App:
    def iniciar(self: object) -> None:
        app = QtWidgets.QApplication([])

        janela = JanelaPrincipal(600, 700)

        sys.exit(app.exec())


if __name__ == "__main__":
    App().iniciar()
