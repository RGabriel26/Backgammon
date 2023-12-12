from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QLabel, QWidget, QHBoxLayout, QGridLayout, QSizePolicy
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import QPoint, QSize
import sys

from functions import *
from gameLogic import *


class UInterface(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BackGammon")
        self.setWindowIcon(QIcon("images/white-checker.png"))
        # instanta a clasie GameLogic
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
        middleLayout = QVBoxLayout()
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
        self.centralWidget = QWidget()  
        self.centralWidget.setLayout(parentLayout)
        self.setCentralWidget(self.centralWidget)


        # adaugarea de elemente in fiecare container
            # adaugarea elementelor din stanga
        leftLayout.addWidget(QLabel("Player1", objectName = "labelPlayer1"))
        leftLayout.addWidget(diceContainer)
        leftLayout.addWidget(QLabel("Player2", objectName = "labelPlayer2"))

            # adaugarea elementelor din mijloc
        middleLayout.addWidget(QLabel())

            # adaugarea elementelor din dreapta
                # adaugarea containerului pentru piesele albe in containerul drept
        rightLayout.addWidget(whiteCheckersContainer)
                # crearea butonului de Roll
        self.rollButton = QPushButton(self)
        self.rollButton.setObjectName("rollButton")
        self.rollButton.setFixedSize(QSize(90, 90))
        # self.rollButton.clicked.connect(self.show_andStoreDices)
        # test
        self.rollButton.clicked.connect(lambda: self.gameLogic.setDices(dices=roll(self.diceLayout)))
        rightLayout.addWidget(self.rollButton)
                # adaugarea containerului pentru piesele negre in containerul drept
        rightLayout.addWidget(blackCheckersContainer) 
    
    def show_andStoreDices(self):
        # TODO: de cautat o modalitate de a sterge lavelul anterior, aici sau in functia roll
        self.gameLogic.setDices(dices=roll(self.diceLayout))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    with open('style/styleSheet.css', 'r') as file:
        stylesheet = file.read()
    app.setStyleSheet(stylesheet)

    game = UInterface()
    game.show()

    sys.exit(app.exec())