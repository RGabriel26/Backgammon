from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QLabel, QWidget, QHBoxLayout, QGridLayout, QLayout
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import QPoint, QSize
import sys

from functions import *
from gameLogic import *
from checkers import *


class UInterface(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BackGammon")
        self.setWindowIcon(QIcon("images/white-checker.png"))
        self.gameLogic = GameLogic()
        self.initGUI()

    def initGUI(self):
        # self.setGeometry(0, 0, 1366, 768)
        # self.showFullScreen()
        self.setFixedSize(1366, 768)

        # folosit pentru a grupa cele trei containere principala ale ferestrei intr-un mod de afisare orizolntala
        parentLayout = QHBoxLayout()

        #container pentru elementele din stanga
            # nume player1
            # nume player2
            # zona de afisare a zarurilor
        leftContainer = QWidget()
        leftContainer.setObjectName("leftContainer")
        leftLayout = QVBoxLayout()
        leftContainer.setLayout(leftLayout)
            # container pentru afisarea zarurilor
        diceContainer = QWidget()
        diceContainer.setObjectName("diceContainer")
        self.diceLayout = QGridLayout()
        self.diceLayout.setObjectName("diceLayout")
        diceContainer.setLayout(self.diceLayout)

        # containerul din mijlocul ferestrei
            # loc unde vor fi afisate piesele de joc si unde se va desfasura jocul
        middleContainer = QWidget()
        middleContainer.setObjectName("middleContainer")
        middleLayout = QGridLayout()
        middleLayout.setSpacing(0)
        middleContainer.setLayout(middleLayout)

        # containerul elementelor din stanga
            # piesele scoase de jucatori
            # butonul de roll al zarurilor
        rightContainer = QWidget()
        rightContainer.setObjectName("rightContainer")
        rightLayout = QVBoxLayout()
        rightContainer.setLayout(rightLayout)
            # setarea containerelor pentru piesele care vor fi scoase din joc
            # crearea containerului pentru piesele ce vor fi scoase de jucatorul WHITE
        whiteCheckersContainer = QWidget()
        whiteCheckersContainer.setObjectName("whiteCheckersContainer")
        whiteCheckersLayout = QHBoxLayout()
        whiteCheckersContainer.setLayout(whiteCheckersLayout)
            # crearea containerului pentru piesele ce vor fi scoase de jucatorul BLACK
        blackCheckersContainer = QWidget()
        blackCheckersContainer.setObjectName("blackCheckersContainer")
        blackCheckersLayout = QHBoxLayout()
        blackCheckersContainer.setLayout(blackCheckersLayout)

        # folosit pentru a aduna containerele intr un singur loc pentru a putea fi gestionate
        parentLayout.addWidget(leftContainer, 28)
        parentLayout.addWidget(middleContainer, 68)
        parentLayout.addWidget(rightContainer, 9)

        # centrarea layout ului parinte in centrul ferestrei
        centralWidget = QWidget()  
        centralWidget.setLayout(parentLayout)
        self.setCentralWidget(centralWidget)


        # adaugarea de elemente in fiecare container
            # adaugarea elementelor din stanga
        leftLayout.addWidget(QLabel("Player1", objectName = "labelPlayer1"))
        leftLayout.addWidget(diceContainer)
        leftLayout.addWidget(QLabel("Player2", objectName = "labelPlayer2"))

            # adaugarea elementelor din mijloc
        bchecker1 = Checkers("black", middleContainer, 785, 17)
        bchecker2 = Checkers("black", middleContainer, 785, 77)
        bchecker3 = Checkers("black", middleContainer, 30, 17)
        bchecker4 = Checkers("black", middleContainer, 30, 77)
        bchecker5 = Checkers("black", middleContainer, 30, 137)
        bchecker6 = Checkers("black", middleContainer, 30, 197)
        bchecker7 = Checkers("black", middleContainer, 30, 257)
        bchecker8 = Checkers("black", middleContainer, 258, 675)
        bchecker9 = Checkers("black", middleContainer, 258, 615)
        bchecker10 = Checkers("black", middleContainer, 258, 555)
        bchecker11 = Checkers("black", middleContainer, 478, 675)
        bchecker12 = Checkers("black", middleContainer, 478, 615)
        bchecker13 = Checkers("black", middleContainer, 478, 555)
        bchecker14 = Checkers("black", middleContainer, 478, 495)
        bchecker15 = Checkers("black", middleContainer, 478, 435)
        middleLayout.addWidget(bchecker1, 0, 0)
        middleLayout.addWidget(bchecker2, 0, 0)
        middleLayout.addWidget(bchecker3, 0, 0)
        middleLayout.addWidget(bchecker4, 0, 0)
        middleLayout.addWidget(bchecker5, 0, 0)
        middleLayout.addWidget(bchecker6, 0, 0)
        middleLayout.addWidget(bchecker7, 0, 0)
        middleLayout.addWidget(bchecker8, 0, 0)
        middleLayout.addWidget(bchecker9, 0, 0)
        middleLayout.addWidget(bchecker10, 0, 0)
        middleLayout.addWidget(bchecker11, 0, 0)
        middleLayout.addWidget(bchecker12, 0, 0)
        middleLayout.addWidget(bchecker13, 0, 0)
        middleLayout.addWidget(bchecker14, 0, 0)
        middleLayout.addWidget(bchecker15, 0, 0)

        # middleLayout.addWidget(Checkers("black", middleContainer, 785, 17), 0, 0)
        # middleLayout.addWidget(Checkers("black", middleContainer, 785, 77), 0, 0)
        # middleLayout.addWidget(Checkers("black", middleContainer, 30, 17), 0, 0)
        # middleLayout.addWidget(Checkers("black", middleContainer, 30, 77), 0, 0)
        # middleLayout.addWidget(Checkers("black", middleContainer, 30, 137), 0, 0)
        # middleLayout.addWidget(Checkers("black", middleContainer, 30, 197), 0, 0)
        # middleLayout.addWidget(Checkers("black", middleContainer, 30, 257), 0, 0)
        # middleLayout.addWidget(Checkers("black", middleContainer, 258, 675), 0, 0)
        # middleLayout.addWidget(Checkers("black", middleContainer, 258, 615), 0, 0)
        # middleLayout.addWidget(Checkers("black", middleContainer, 258, 555), 0, 0)
        # middleLayout.addWidget(Checkers("black", middleContainer, 478, 675), 0, 0)
        # middleLayout.addWidget(Checkers("black", middleContainer, 478, 615), 0, 0)
        # middleLayout.addWidget(Checkers("black", middleContainer, 478, 555), 0, 0)
        # middleLayout.addWidget(Checkers("black", middleContainer, 478, 495), 0, 0)
        # middleLayout.addWidget(Checkers("black", middleContainer, 478, 435), 0, 0)

        # middleLayout.addSpacing(2000)

        wchecker1 = Checkers("white", middleContainer, 785, 675)
        wchecker2 = Checkers("white", middleContainer, 785, 615)
        wchecker3 = Checkers("white", middleContainer, 30, 675)
        wchecker4 = Checkers("white", middleContainer, 30, 615)
        wchecker5 = Checkers("white", middleContainer, 30, 555)
        wchecker6 = Checkers("white", middleContainer, 30, 495)
        wchecker7 = Checkers("white", middleContainer, 30, 435)
        wchecker8 = Checkers("white", middleContainer, 258, 17)
        wchecker9 = Checkers("white", middleContainer, 258, 77)
        wchecker10 = Checkers("white", middleContainer, 258, 137)
        wchecker11 = Checkers("white", middleContainer, 478, 17)
        wchecker12 = Checkers("white", middleContainer, 478, 77)
        wchecker13 = Checkers("white", middleContainer, 478, 137)
        wchecker14 = Checkers("white", middleContainer, 478, 197)
        wchecker15 = Checkers("white", middleContainer, 478, 257)
        middleLayout.addWidget(wchecker15, 0, 1)
        middleLayout.addWidget(wchecker14, 0, 1)
        middleLayout.addWidget(wchecker13, 0, 1)
        middleLayout.addWidget(wchecker12, 0, 1)
        middleLayout.addWidget(wchecker11, 0, 1)
        middleLayout.addWidget(wchecker10, 0, 1)
        middleLayout.addWidget(wchecker9, 0, 1)
        middleLayout.addWidget(wchecker8, 0, 1)
        middleLayout.addWidget(wchecker7, 0, 1)
        middleLayout.addWidget(wchecker6, 0, 1)
        middleLayout.addWidget(wchecker5, 0, 1)
        middleLayout.addWidget(wchecker4, 0, 1)
        middleLayout.addWidget(wchecker3, 0, 1)
        middleLayout.addWidget(wchecker2, 0, 1)
        middleLayout.addWidget(wchecker1, 0, 1)

            # adaugarea elementelor din dreapta
                # adaugarea containerului pentru piesele albe in containerul drept
        rightLayout.addWidget(whiteCheckersContainer)
                # crearea butonului de Roll
        rollButton = QPushButton(self)
        rollButton.setObjectName("rollButton")
        rollButton.setFixedSize(QSize(90, 90))
                # functia roll care adauga widgetul in diceLayout si returneaza lista cu raruri, care sunt loate de clasa gamoLogic si stocate prin setDices
        rollButton.clicked.connect(lambda: self.gameLogic.setDices(dices=roll(self.diceLayout)))
        rightLayout.addWidget(rollButton)
                # adaugarea containerului pentru piesele negre in containerul drept
        rightLayout.addWidget(blackCheckersContainer)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    with open('style/styleSheet.css', 'r') as file:
        stylesheet = file.read()
    app.setStyleSheet(stylesheet)

    game = UInterface()
    game.show()

    sys.exit(app.exec())