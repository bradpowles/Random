from PyQt5.QtCore import QSize
from PyQt5 import QtWidgets, QtCore
import sys
from PyQt5.QtWidgets import *
from random import randint


class Hangman(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(640, 480))
        self.setWindowTitle(" - - Hangman - - ")
        self.statusBar().showMessage("Welcome to PyQt Hangman")

        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)

        vertbox = QVBoxLayout()
        centralWidget.setLayout(vertbox)

        hozbox = QHBoxLayout()
        vertbox.addLayout(hozbox)

        gridLayout = QGridLayout(self)
        vertbox.addLayout(gridLayout)

        self.dictofletters = {'0':'A', '1':'B', '2':'C', '3':'D', '4':'E', '5':'F',
        '6':'G', '7':'H', '8':'I', '9':'J', '10':'K', '11':'L',
        '12':'M', '13':'N', '14':'O', '15':'P', '16':'Q',
        '17':'R', '18':'S', '19':'T', '20':'U', '21':'V',
        '22':'W', '23':'X', '24':'Y', '25':'Z', '26':'REPLAY'}


        self.lblwordtoguess = QLabel(" some text", self)
        self.lblwordtoguess.setAlignment(QtCore.Qt.AlignCenter)
        # self.lblwordtoguess.move(50, 35)
        hozbox.addWidget(self.lblwordtoguess)

        self.lbllettersguessed = QLabel(" some text", self)
        self.lbllettersguessed.setAlignment(QtCore.Qt.AlignCenter)
        # self.lbllettersguessed.move(150, 55)
        hozbox.addWidget(self.lbllettersguessed)

        positions = [(i,j) for i in range(9) for j in range(3)]

        for position, aletter in zip(positions, range(0,27)):
            pybutton = QPushButton(self.dictofletters[str(aletter)], self)
            pybutton.resize(35, 35)
            pybutton.clicked.connect(self.clickMethod)
            gridLayout.addWidget(pybutton, *position)

    def clickMethod(self):

        newguess = self.sender()  # this will get memory location of value

    # newguess.text() will then get the value of the button text




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    mainwin = Hangman()
    mainwin.show()

    sys.exit( app.exec_() )