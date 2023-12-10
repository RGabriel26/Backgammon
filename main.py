from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QLabel, QWidget, QHBoxLayout, QGridLayout, QSizePolicy
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import QPoint
import sys

from DiceObjects import *


class GameLogic(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BackGammon")
        self.setWindowIcon(QIcon("images/white-checker.png"))
        self.initGUI()

    def initGUI(self):
        # self.setGeometry(0, 0, 1366, 768)
        # self.showFullScreen()
        self.setFixedSize(1366, 768)

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
        diceLayout = QGridLayout()
        diceLayout.setObjectName("diceLayout")
        diceContainer.setLayout(diceLayout)

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
        whiteCheckersContainer = QWidget()
        whiteCheckersContainer.setObjectName("whiteCheckersContainer")
        whiteCheckersLayout = QHBoxLayout()
        whiteCheckersContainer.setLayout(whiteCheckersLayout)

        blackCheckersContainer = QWidget()
        blackCheckersContainer.setObjectName("blackCheckersContainer")
        blackCheckersLayout = QHBoxLayout()
        blackCheckersContainer.setLayout(blackCheckersLayout)

        # folosit pentru a aduna containerele intr un singur loc pentru a putea fi gestionate
        parentLayout.addWidget(leftContainer, 28)
        parentLayout.addWidget(middleContainer, 68)
        parentLayout.addWidget(rightContainer, 9)

        self.centralWidget = QWidget()  
        self.centralWidget.setLayout(parentLayout)
        self.setCentralWidget(self.centralWidget)


        # adaugarea de elemente in fiecare container
            # adaugarea elementelor din stanga
        leftLayout.addWidget(QLabel("Player1", objectName = "labelPlayer1"))

        dice1 = "images/dice1.png"
        diceLayout.addWidget(createDiceObject("%s" %dice1), 0, 0)
        diceLayout.addWidget(createDiceObject("images/dice2.png"), 0, 1)
        diceLayout.addWidget(createDiceObject("images/dice3.png"), 1, 0)
        diceLayout.addWidget(createDiceObject("images/dice4.png"), 1, 1)
        diceLayout.addWidget(createDiceObject("images/dice5.png"), 2, 0)
        diceLayout.addWidget(createDiceObject("images/dice6.png"), 2, 1)

        leftLayout.addWidget(diceContainer)

        leftLayout.addWidget(QLabel("Player2", objectName = "labelPlayer2"))

            # adaugarea elementelor din mijloc
        middleLayout.addWidget(QLabel())

            # adaugarea elementelor din dreapta
        rightLayout.addWidget(whiteCheckersContainer)
        self.rollButton = QPushButton(self)
        self.rollButton.setObjectName("rollButton")
        self.rollButton.setFixedSize(100,100)
        self.rollButton.clicked.connect(self.moveRollDice)
        rightLayout.addWidget(self.rollButton)
        rightLayout.addWidget(blackCheckersContainer)

    def moveRollDice(self):
        self.rollButton.move(0,50)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    with open('style/styleSheet.css', 'r') as file:
        stylesheet = file.read()
    app.setStyleSheet(stylesheet)

    game = GameLogic()
    game.show()

    sys.exit(app.exec())