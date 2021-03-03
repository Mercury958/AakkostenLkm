import sys

from PyQt5.QtWidgets import QApplication, QPushButton, QHBoxLayout, QLabel, QMainWindow, \
    QVBoxLayout, QWidget, QLineEdit

from dict_aakkoset import aakk  # importataan aakk dictionary main.py tiedostosta


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.laskenappi = QPushButton('Laske')
        self.txtBox = QLineEdit()
        self.title = 'Aakkosten lukumäärä laskuri'
        # left ja top attribuuteilla määrätään sovelluksen etäisyys pikseleinä näytön vasemmasta ja yläreunasta
        self.left = 100
        self.top = 100
        self.width = 500
        self.height = 200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        txtsyöteLo = QHBoxLayout()
        nappilayout = QHBoxLayout()
        Aakklayout = QHBoxLayout()
        Hlayout = QVBoxLayout()

        self.txtBox.resize(100, 100)
        txtsyöteLo.addWidget(self.txtBox)
        Hlayout.addLayout(txtsyöteLo)

        self.laskenappi.clicked.connect(self.LaskeLkm)
        nappilayout.addWidget(self.laskenappi)
        Hlayout.addLayout(nappilayout)

        lA = QLabel('aA', self)
        lB = QLabel('bB', self)
        lC = QLabel('cC', self)
        lD = QLabel('dD', self)
        lE = QLabel('eE', self)
        lF = QLabel('fF', self)
        lG = QLabel('gG', self)
        lH = QLabel('hH', self)
        lI = QLabel('iI', self)
        lJ = QLabel('jJ', self)
        lK = QLabel('kK', self)
        lL = QLabel('lL', self)
        lM = QLabel('mM', self)
        lN = QLabel('nN', self)
        lO = QLabel('oO', self)
        lP = QLabel('pP', self)
        lQ = QLabel('qQ', self)
        lR = QLabel('rR', self)
        lS = QLabel('sS', self)
        lT = QLabel('tT', self)
        lU = QLabel('uU', self)
        lV = QLabel('vV', self)
        lW = QLabel('wW', self)
        lX = QLabel('xX', self)
        lY = QLabel('tT', self)
        lZ = QLabel('zZ', self)
        lÅ = QLabel('åÅ', self)
        lÄ = QLabel('äÄ', self)
        lÖ = QLabel('öÖ', self)

        Aakklayout.addWidget(lA)
        Aakklayout.addWidget(lB)
        Aakklayout.addWidget(lC)
        Aakklayout.addWidget(lD)
        Aakklayout.addWidget(lE)
        Aakklayout.addWidget(lF)
        Aakklayout.addWidget(lG)
        Aakklayout.addWidget(lH)
        Aakklayout.addWidget(lI)
        Aakklayout.addWidget(lJ)
        Aakklayout.addWidget(lK)
        Aakklayout.addWidget(lL)
        Aakklayout.addWidget(lM)
        Aakklayout.addWidget(lN)
        Aakklayout.addWidget(lO)
        Aakklayout.addWidget(lP)
        Aakklayout.addWidget(lQ)
        Aakklayout.addWidget(lR)
        Aakklayout.addWidget(lS)
        Aakklayout.addWidget(lT)
        Aakklayout.addWidget(lU)
        Aakklayout.addWidget(lV)
        Aakklayout.addWidget(lW)
        Aakklayout.addWidget(lX)
        Aakklayout.addWidget(lY)
        Aakklayout.addWidget(lZ)
        Aakklayout.addWidget(lÅ)
        Aakklayout.addWidget(lÄ)
        Aakklayout.addWidget(lÖ)

        Hlayout.addLayout(Aakklayout)

        widget = QWidget()
        widget.setLayout(Hlayout)
        self.setCentralWidget(widget)

        self.show()

    def LaskeLkm(self):
        txtboxval = self.txtBox.text()  # text() metodilla luetaan syötetty teksti

        for x in txtboxval:
            for z in aakk:
                if x == z or x.upper() == z.upper():
                    aakk[z] += 1
                    break

        for kirjain, kirjLkm in aakk.items():
            print(kirjain + ", " + kirjain.upper() + ": ", kirjLkm)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())
