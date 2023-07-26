import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui

class AreaInput(QtWidgets.QWidget):
    def __init__(self, w: int, h: int):
        super().__init__()

        self.resize(w,h)
        self.input = QtWidgets.QLineEdit()




class JanelaPrincipal(QtWidgets.QWidget):
    def __init__(self, w: int, h: int):
        super().__init__()

        self.resize(w,h)

        self.button = QtWidgets.QPushButton("Adicionar")
        self.input = QtWidgets.QLineEdit()
        self.input.resize(2,5)
        self.text = QtWidgets.QLabel("", alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.input)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

        self.show()

    @QtCore.Slot()
    def magic(self):
        # self.button.setText("Desbloqueado")
        self.text.setText(self.input.text())
        self.input.clear()

class App:

    def iniciar(self) -> None:
        app = QtWidgets.QApplication([])

        janela = JanelaPrincipal(800,600)

        sys.exit(app.exec())


if __name__ == "__main__":
    App().iniciar()
