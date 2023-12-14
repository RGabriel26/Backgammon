from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QLabel, QWidget, QHBoxLayout, QGridLayout, QLayout, QSpacerItem
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import QPoint, QSize, Qt
from PyQt6 import QtWidgets
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
        # self.setGeometry(0, 0, 1600, 900)
        # self.showFullScreen()
        self.setFixedSize(1600, 900)

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
        #container principal
        middleContainer = QWidget()
        middleContainer.setObjectName("middleContainer")

        # container pentru grid principal
        # middlePrincipalGridContainer = QWidget()
        middlePrincipalGrid = QGridLayout()
############################################ zona din STANGA ###############################################################
        middleSecundarGridContainer_left = QWidget()
        middleSecundarGridContainer_left.setObjectName("middleSecundarGridContainer_left")
        middleSecundarGrid_left = QGridLayout()
        positionTopLeftContainer = QWidget()
        positionTopLeftContainer.setObjectName("positionTopLeftContainer")
        positionTopLeft = QHBoxLayout()
        pos11Container = QWidget()
        pos11Container.setObjectName("pos11Container")
        pos12Container = QWidget()
        pos12Container.setObjectName("pos12Container")
        pos13Container = QWidget()
        pos13Container.setObjectName("pos13Container")
        pos14Container = QWidget()
        pos14Container.setObjectName("pos14Container")
        pos15Container = QWidget()
        pos15Container.setObjectName("pos15Container")
        pos11 = QVBoxLayout()
        pos12 = QVBoxLayout()
        pos13 = QVBoxLayout()
        pos14 = QVBoxLayout()
        pos15 = QVBoxLayout()
        pos11Container.setLayout(pos11)
        pos11Container.setFixedSize(80,pos12Container.size().height())
        pos12Container.setLayout(pos12)
        pos13Container.setLayout(pos13)
        pos14Container.setLayout(pos14)
        pos15Container.setLayout(pos15)
        positionTopLeft.addWidget(pos11Container)
        positionTopLeft.addWidget(pos12Container)
        positionTopLeft.addWidget(pos13Container)
        positionTopLeft.addWidget(pos14Container)
        positionTopLeft.addWidget(pos15Container)
        positionTopLeftContainer.setLayout(positionTopLeft)
        middleSecundarGrid_left.addWidget(positionTopLeftContainer,0,0)

        positionButtonLeftContainer = QWidget()
        positionButtonLeftContainer.setObjectName("positionButtonLeftContainer")
        positionButtonLeft = QHBoxLayout()
        pos6Container = QWidget()
        pos6Container.setObjectName("pos6Container")
        pos7Container = QWidget()
        pos7Container.setObjectName("pos7Container")
        pos8Container = QWidget()
        pos8Container.setObjectName("pos8Container")
        pos9Container = QWidget()
        pos9Container.setObjectName("pos9Container")
        pos10Container = QWidget()
        pos10Container.setObjectName("pos10Container")
        pos6 = QVBoxLayout()
        pos7 = QVBoxLayout()
        pos8 = QVBoxLayout()
        pos9 = QVBoxLayout()
        pos10 = QVBoxLayout()
        pos6Container.setLayout(pos6)
        pos7Container.setLayout(pos7)
        pos7Container.setFixedSize(80,pos8Container.size().height())
        pos8Container.setLayout(pos8)
        pos9Container.setLayout(pos9)
        pos10Container.setLayout(pos10)
        positionButtonLeft.addWidget(pos10Container)
        positionButtonLeft.addWidget(pos9Container)
        positionButtonLeft.addWidget(pos8Container)
        positionButtonLeft.addWidget(pos7Container)
        positionButtonLeft.addWidget(pos6Container)
        positionButtonLeftContainer.setLayout(positionButtonLeft) 

        middleSecundarGrid_left.addWidget(positionButtonLeftContainer, 1, 0)
        middleSecundarGridContainer_left.setLayout(middleSecundarGrid_left)

####################################### zona din MIJLOC ############################################
        middleSecundarGridContainer_middle = QWidget()
        middleSecundarGridContainer_middle.setObjectName("middleSecundarGridContainer_middle")
        
        middleSecundarGrid_middle = QGridLayout()
        
        middleSecundarGridContainer_middle.setLayout(middleSecundarGrid_middle)

####################################### zona din DREAPTA ###########################################
        middleSecundarGridContainer_right = QWidget()
        # middleSecundarGridContainer_right.setSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed,QtWidgets.QSizePolicy.Policy.Fixed)
        middleSecundarGridContainer_right.setObjectName("middleSecundarGridContainer_right")
        middleSecundarGrid_right = QGridLayout()
        # middleSecundarGrid_right.setVerticalSpacing(330)
        positionTopRightContainer = QWidget()
        # positionTopRightContainer.setSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed,QtWidgets.QSizePolicy.Policy.Fixed)
        positionTopRightContainer.setObjectName("positionTopRightContainer")
        positionTopRight = QHBoxLayout()
        pos16Container = QWidget()
        pos16Container.setObjectName("pos16Container")
        pos17Container = QWidget()
        pos17Container.setObjectName("pos17Container")
        pos18Container = QWidget()
        pos18Container.setObjectName("pos18Container")
        pos19Container = QWidget()
        pos19Container.setObjectName("pos19Container")
        pos20Container = QWidget()
        pos20Container.setObjectName("pos20Container")
        pos16 = QVBoxLayout()
        pos17 = QVBoxLayout()
        pos18 = QVBoxLayout()
        pos19 = QVBoxLayout()
        pos20 = QVBoxLayout()
        pos16Container.setLayout(pos16)
        pos16Container.setFixedSize(80,pos8Container.size().height())
        pos17Container.setLayout(pos17)
        pos18Container.setLayout(pos18)
        pos19Container.setLayout(pos19)
        pos20Container.setLayout(pos20)
        positionTopRight.addWidget(pos16Container)
        positionTopRight.addWidget(pos17Container)
        positionTopRight.addWidget(pos18Container)
        positionTopRight.addWidget(pos19Container)
        positionTopRight.addWidget(pos20Container)
        positionTopRightContainer.setLayout(positionTopRight)
        middleSecundarGrid_right.addWidget(positionTopRightContainer,0,0)

        positionButtonRightContainer = QWidget()
        positionButtonRightContainer.setObjectName("positionButtonRightContainer")
        positionButtonRight = QHBoxLayout()
        pos1Container = QWidget()
        pos1Container.setObjectName("pos1Container")
        pos2Container = QWidget()
        pos2Container.setObjectName("pos2Container")
        pos3Container = QWidget()
        pos3Container.setObjectName("pos3Container")
        pos4Container = QWidget()
        pos4Container.setObjectName("pos4Container")
        pos5Container = QWidget()
        pos5Container.setObjectName("pos5Container")
        pos1 = QVBoxLayout()
        pos2 = QVBoxLayout()
        pos3 = QVBoxLayout()
        pos4 = QVBoxLayout()
        pos5 = QVBoxLayout()
        pos1Container.setLayout(pos5)
        pos1Container.setFixedSize(80,pos8Container.size().height())
        pos2Container.setLayout(pos4)
        pos3Container.setLayout(pos3)
        pos4Container.setLayout(pos2)
        pos5Container.setLayout(pos1)
        positionButtonRight.addWidget(pos1Container)
        positionButtonRight.addWidget(pos2Container)
        positionButtonRight.addWidget(pos3Container)
        positionButtonRight.addWidget(pos4Container)
        positionButtonRight.addWidget(pos5Container)
        positionButtonRightContainer.setLayout(positionButtonRight) 
        middleSecundarGrid_right.addWidget(positionButtonRightContainer, 1, 0)
        middleSecundarGridContainer_right.setLayout(middleSecundarGrid_right)

            # grid uri secundare(cele trei pe coloane)
        middlePrincipalGrid.addWidget(middleSecundarGridContainer_left, 0, 0)
        middlePrincipalGrid.addWidget(middleSecundarGridContainer_middle, 0, 1)
        middlePrincipalGrid.addWidget(middleSecundarGridContainer_right, 0, 2)
        middleContainer.setLayout(middlePrincipalGrid)
#########################################################################################################################################################
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
                # doar pentru a cauta pozitii


        bchecker1 = Checkers("black")
        bchecker2 = Checkers("black")
        bchecker3 = Checkers("black")
        bchecker4 = Checkers("black")
        bchecker5 = Checkers("black")
        bchecker6 = Checkers("black")
        bchecker7 = Checkers("black")
        bchecker8 = Checkers("black")
        bchecker9 = Checkers("black")
        bchecker10 = Checkers("black")
        bchecker11 = Checkers("black")
        bchecker12 = Checkers("black")
        bchecker13 = Checkers("black")
        bchecker14 = Checkers("black")
        bchecker15 = Checkers("black")
        
        pos15.addWidget(Checkers("black"))
        pos15.addWidget(bchecker15)
        
        pos14.setSpacing(0)
        pos14.setAlignment(Qt.AlignmentFlag.AlignTop)
        pos14.addWidget(Checkers("black"))
        pos14.addWidget(Checkers("black"))
        pos14.addWidget(Checkers("black"))
        pos14.addWidget(Checkers("black"))
        pos14.addWidget(Checkers("black"))
        pos14.addWidget(Checkers("black"))
        pos14.addWidget(Checkers("black"))
        pos14.addWidget(Checkers("black"))
        pos14.addWidget(Checkers("black"))
        pos14.addWidget(Checkers("black"))
        pos14.addWidget(Checkers("black"))
        pos14.addWidget(Checkers("black"))
        pos14.addWidget(Checkers("black"))
        pos14.addWidget(Checkers("black"))
        pos14.addWidget(Checkers("black"))

        pos13.addWidget(bchecker13)
        pos12.addWidget(bchecker12)
        pos11.addWidget(bchecker11)
        pos10.addWidget(bchecker10)
        pos9.addWidget(bchecker9)
        pos8.addWidget(bchecker8)

        pos7.setSpacing(0)
        pos7.setAlignment(Qt.AlignmentFlag.AlignBottom)
        pos7.addWidget(Checkers("black"))
        pos7.addWidget(Checkers("black"))
        pos7.addWidget(Checkers("black"))
        pos7.addWidget(Checkers("black"))
        pos7.addWidget(Checkers("black"))
        pos7.addWidget(Checkers("black"))
        pos7.addWidget(Checkers("black"))
        pos7.addWidget(Checkers("black"))
        pos7.addWidget(Checkers("black"))
        pos7.addWidget(Checkers("black"))
        pos7.addWidget(Checkers("black"))
        pos7.addWidget(Checkers("black"))
        pos7.addWidget(Checkers("black"))
        pos7.addWidget(Checkers("black"))
        pos7.addWidget(Checkers("black"))
        
        pos6.addWidget(bchecker6)

        pos1.addWidget(bchecker5)
        pos1.addWidget(bchecker4)
        pos1.addWidget(bchecker3)
        pos1.addWidget(bchecker2)
        pos1.addWidget(bchecker1)
        pos1.addWidget(Checkers("white"))
        pos1.addWidget(Checkers("white"))
        pos1.addWidget(Checkers("white"))
        pos1.addWidget(Checkers("white"))
        pos1.addWidget(Checkers("white"))
        pos1.addWidget(Checkers("white"))
        pos1.addWidget(Checkers("white"))
        pos1.addWidget(Checkers("white"))
        pos1.addWidget(Checkers("white"))
        pos1.addWidget(Checkers("white"))

        wchecker1 = Checkers("white")
        wchecker2 = Checkers("white")
        wchecker3 = Checkers("white")
        wchecker4 = Checkers("white")
        wchecker5 = Checkers("white")
        wchecker6 = Checkers("white")
        wchecker7 = Checkers("white")
        wchecker8 = Checkers("white")
        wchecker9 = Checkers("white")
        wchecker10 = Checkers("white")
        wchecker11 = Checkers("white")
        wchecker12 = Checkers("white")
        wchecker13 = Checkers("white")
        wchecker14 = Checkers("white")
        wchecker15 = Checkers("white")
        pos16.addWidget(wchecker15)
        pos17.addWidget(wchecker14)
        pos18.addWidget(wchecker13)
        pos19.addWidget(wchecker12)
        pos20.addWidget(wchecker11)

            # adaugarea elementelor din dreapta
                # adaugarea containerului pentru piesele albe in containerul drept
        rightLayout.addWidget(whiteCheckersContainer)
                # crearea butonului de Roll
        rollButton = QPushButton(self)
        rollButton.setObjectName("rollButton")
        rollButton.setFixedSize(QSize(100, 100))
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