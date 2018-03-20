'''
Base Game taken from Tom Bell, https://github.com/tomedwardbell
Refined, and added Client and Server components.
'''
from PyQt5 import QtWidgets, QtTest
import sys, socket, threading


class Server:
    def __init__(self):
        self.connect("127.0.0.1")
        self.sessions = {}

    def connect(self, ip):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((ip, 8080))
        while True:
            s.listen(1)
            print('Server Started.')
            conn, addr = s.accept()
            lobby = {}
            lobby['ip'] = '127.0.0.1'
            lobby['port'] = '9001'
            s.send(lobby)
            instance = threading.Thread(target=self.instance, args=(lobby))
            instance.start()

    def instance(self, lobby):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((lobby['ip'], lobby['port']))
        s.send("welcome")

class Coord:
        def __init__(self, game):
            self.btn = QtWidgets.QPushButton(game)
            self.value = " "

        def setValue(self, tochangeto):
            self.value = tochangeto
            self.btn.setText(self.value)
            self.btn.setStyleSheet("font-size: 50pt")

        def setColor(self, tochangeto):
            self.btn.setStyleSheet("background-color: {}" % tochangeto)


class Grid(QtWidgets.QMainWindow):
    def __init__(self):
        super(Grid, self).__init__()
        self.currentturn = "O"
        self.board = {}
        self.won = False
        self.initUI()

    def initUI(self):
        boardx = 650
        boardy = 650
        border = 0
        xcount = 3
        ycount = 3

        self.resize(boardx + border * (xcount + 1), boardy + border * (xcount + 1))
        for x in range(xcount):
            for y in range(ycount):
                self.board[x, y] = Coord(self)
                self.board[x, y].coordinates = [x, y]
                xpercoord = (boardx / xcount)
                ypercoord = (boardy / ycount)
                xloc = (x*xpercoord + (x+1)*border)
                yloc = (y*ypercoord + (y+1)*border)
                self.board[x, y].btn.move(xloc, yloc)
                self.board[x, y].btn.resize(boardx/xcount, boardy/ycount)

        for x in range(xcount):
            for y in range(ycount):
                self.board[x, y].btn.clicked.connect(lambda state, c=(x, y): self.doturn(c))

    def doturn(self, coordnumbers):
        if self.board[coordnumbers].value == " " and self.won == False:
            if self.currentturn == "O":
                self.currentturn = "X"
            elif self.currentturn == "X":
                self.currentturn = "O"
            self.board[coordnumbers].setValue(self.currentturn)
            self.checkboard()

    def checkboard(self):
        possiblewins = [
            [[0, 0], [0, 1], [0, 2]],
            [[1, 0], [1, 1], [1, 2]],
            [[2, 0], [2, 1], [2, 2]],

            [[0, 0], [1, 0], [2, 0]],
            [[0, 1], [1, 1], [2, 1]],
            [[0, 2], [1, 2], [2, 2]],

            [[0, 0], [1, 1], [2, 2]],
            [[0, 2], [1, 1], [2, 0]]
        ]
        drawn = True
        for player in ["O", "X"]:
            for winningboard in possiblewins:
                wonyet = True
                for coord in winningboard:
                    x, y = coord
                    if not (self.board[x, y].value == player) or self.board[x, y].value == " ":
                        wonyet = False
                    if self.board[x, y].value == " ":
                        drawn = False
                if wonyet:
                    winner = player
                    self.win(winner, winningboard)
        if drawn == True and self.won == False:
            self.win("draw", [])

    def win(self, winner, winningboard):
        if winner == "draw":
            for x in range(3):
                for y in range(3):
                    self.board[x, y].btn.setColor("#DDDD11")
        else:
            self.won = True
            for i in winningboard:
                QtTest.QTest.qWait(100)
                x, y = i
                self.board[x, y].btn.setColor("#DDDD11")


def main():
    app = QtWidgets.QApplication(sys.argv)
    game = Grid()
    game.show()
    app.exec_()

if __name__ == '__main__':
    main()