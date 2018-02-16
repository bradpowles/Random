from PyQt5.QtCore import QSize
from PyQt5 import QtWidgets, QtCore
import sys
from PyQt5.QtWidgets import *
import random


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
        '22':'W', '23':'X', '24':'Y', '25':'Z', '26':'EXIT'}

        self.lblwordtoguess = QLabel("Loading...", self)
        self.lblwordtoguess.setAlignment(QtCore.Qt.AlignCenter)
        # self.lblwordtoguess.move(50, 35)
        hozbox.addWidget(self.lblwordtoguess)

        self.lbllettersguessed = QLabel("Click a button to start.", self)
        self.lbllettersguessed.setAlignment(QtCore.Qt.AlignCenter)
        # self.lbllettersguessed.move(150, 55)
        hozbox.addWidget(self.lbllettersguessed)

        self.word = self.wordgenerator()
        self.allowedguesses = len(self.word) + len(self.word) // 3
        self.numofguesses = 0
        self.lettersguessed = []

        self.complete = QLabel("{} / {}".format(self.numofguesses, self.allowedguesses), self)
        self.complete.setAlignment(QtCore.Qt.AlignCenter)
        hozbox.addWidget(self.complete)

        positions = [(i,j) for i in range(9) for j in range(3)]

        for position, aletter in zip(positions, range(0,27)):
            pybutton = QPushButton(self.dictofletters[str(aletter)], self)
            pybutton.resize(35, 35)
            pybutton.clicked.connect(self.clickMethod)
            gridLayout.addWidget(pybutton, *position)

    def clickMethod(self):
        newguess = self.sender()
        # newguess.text()
        if newguess.text() == 'EXIT':
            sys.exit(app.exec_())
        else:
            self.main(newguess.text())

    def wordguessing(self, word, guessed):
        string = ""
        letters = ""
        for i in word:
            if i in guessed:
                string += i
            else:
                string += "- "
        self.lblwordtoguess.setText(string)
        for x in guessed:
            letters += x + " "
        self.lbllettersguessed.setText(letters)

    def wordgenerator(self):
        words = ['COMPUTING', 'WARWICK', 'GOOGLE']
        word = random.choice(words)
        "".split(word)
        self.wordguessing(word, [])
        return word

    def end(self, bool):
        if bool == True:
            self.complete.setText("GG! Well Done!")
        else:
            self.complete.setText("You lost!!!")

    def main(self, guess):
        self.lettersguessed.append(guess)
        self.wordguessing(self.word, self.lettersguessed)
        if self.numofguesses == self.allowedguesses:
            self.end(False)
        else:
            if guess in self.word:
                complete = False
                for i in self.word:
                    if i not in self.lettersguessed:
                        complete = False
                        break
                    else:
                        complete = True
                if complete:
                    self.end(True)
            else:
                self.numofguesses += 1
                self.complete.setText("{} / {}".format(self.numofguesses, self.allowedguesses))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    mainwin = Hangman()
    mainwin.show()

    sys.exit( app.exec_() )