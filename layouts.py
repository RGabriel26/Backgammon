from PyQt6.QtWidgets import QWidget, QGridLayout, QVBoxLayout, QHBoxLayout, QLabel
from PyQt6.QtCore import Qt, QSize, QTimer

from checkers import *
from functions import *

class UILayouts():
    def __init__(self) -> None:
        super().__init__()

    def middleLayout(self, heightWindow):
        heightPositionContainer = 330
        widhtPositionContainer = 50

        middleContainer = QWidget()
        middleContainer.setObjectName("middleContainer")

        # container pentru grid principal
        # middlePrincipalGridContainer = QWidget()
        middlePrincipalGrid = QHBoxLayout()
        ############################################ zona din STANGA ###############################################################
        #TODO: De regandit layout ul pentru pos, poate ne mai folosind grid
        # incearca sa faci ca in cazul layout ului di centru pentru piesele 
        # pentru gard, acolo ele sunt puse la mijloc by defaul, poate daca
        # in loc de grid pentru containerele pozitiilor ai folosi QHBoxLayout
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
        middleSecundarContainer_middle = QWidget()
        middleSecundarContainer_middle.setObjectName("middleSecundarContainer_middle")

        middleSecundarLayout = QVBoxLayout()

        fenceWhiteCheckersContainer = QWidget()
        fenceWhiteCheckersContainer.setObjectName("fenceWhiteCheckersContainer")
        fenceWhiteCheckers = QVBoxLayout()
        fenceWhiteCheckers.setObjectName("fenceWhiteCheckers")
        fenceWhiteCheckers.addWidget(Checkers("white", fenceWhiteCheckers))
        fenceWhiteCheckersContainer.setLayout(fenceWhiteCheckers)

        fenceBlackCheckersContainer = QWidget()
        fenceBlackCheckersContainer.setObjectName("fenceBlackCheckersContainer")
        fenceBlackCheckers = QVBoxLayout()
        fenceBlackCheckers.setObjectName("fenceBlackCheckers")
        fenceBlackCheckers.addWidget(Checkers("black", fenceBlackCheckers))

        fenceBlackCheckersContainer.setLayout(fenceBlackCheckers)
        middleSecundarLayout.addWidget(fenceWhiteCheckersContainer)
        middleSecundarLayout.addWidget(fenceBlackCheckersContainer)

        middleSecundarContainer_middle.setLayout(middleSecundarLayout)

        ####################################### zona din DREAPTA ###########################################
        middleSecundarGridContainer_right = QWidget()
        middleSecundarGridContainer_right.setObjectName("middleSecundarGridContainer_right")
        middleSecundarGrid_right = QGridLayout()
        positionTopRightContainer = QWidget()
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
        middlePrincipalGrid.addWidget(middleSecundarGridContainer_left,45)
        middlePrincipalGrid.addWidget(middleSecundarContainer_middle,10)
        middlePrincipalGrid.addWidget(middleSecundarGridContainer_right,45)
        middleContainer.setLayout(middlePrincipalGrid)

        #setup containerelor
        middleSecundarGrid_left.setContentsMargins(0,8,0,8)
        middleSecundarGrid_right.setContentsMargins(0,8,0,8)

        positionTopLeftContainer.setContentsMargins(0,0,0,0)
        positionTopRightContainer.setContentsMargins(0,0,0,0)
        positionButtonLeftContainer.setContentsMargins(0,0,0,0)
        positionButtonRightContainer.setContentsMargins(0,0,0,0)

        positionTopLeft.setContentsMargins(0,0,0,0)
        positionButtonLeft.setContentsMargins(0,0,0,0)
        positionTopRight.setContentsMargins(0,0,0,0)
        positionButtonRight.setContentsMargins(0,0,0,0)

        pos1.setObjectName("pos1")
        pos2.setObjectName("pos2")
        pos3.setObjectName("pos3")
        pos4.setObjectName("pos4")
        pos5.setObjectName("pos5")
        pos6.setObjectName("pos6")
        pos7.setObjectName("pos7")
        pos8.setObjectName("pos8")
        pos9.setObjectName("pos9")
        pos10.setObjectName("pos10")
        pos11.setObjectName("pos11")
        pos12.setObjectName("pos12")
        pos13.setObjectName("pos13")
        pos14.setObjectName("pos14")
        pos15.setObjectName("pos15")
        pos16.setObjectName("pos16")
        pos17.setObjectName("pos17")
        pos18.setObjectName("pos18")
        pos19.setObjectName("pos19")
        pos20.setObjectName("pos20")

        #setarea proprietailor layout-urilor de pozitionare a pieselor
        positions = [pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9, pos10,
        pos11, pos12, pos13, pos14, pos15, pos16, pos17, pos18, pos19, pos20]

        for i in range(10):
                positions[i].setSpacing(0)
                positions[i].setAlignment(Qt.AlignmentFlag.AlignBottom)
                positions[i].setContentsMargins(0, 0, 0, 0)

        for i in range(10, 20):
                positions[i].setSpacing(0)
                positions[i].setAlignment(Qt.AlignmentFlag.AlignTop)
                positions[i].setContentsMargins(0, 0, 0, 0)

        # QTimer.singleShot(0, lambda: rollButton.setFixedSize(whiteCheckersContainer.width(), whiteCheckersContainer.width()))

        
        fenceWhiteCheckers.setSpacing(0)
        fenceWhiteCheckers.setAlignment(Qt.AlignmentFlag.AlignCenter)
        fenceWhiteCheckers.setContentsMargins(0, 0, 0, 0)

        fenceBlackCheckers.setSpacing(0)
        fenceBlackCheckers.setAlignment(Qt.AlignmentFlag.AlignCenter)
        fenceBlackCheckers.setContentsMargins(0, 0, 0, 0)
        #creara pieselor in locurile default
                #piesele negre
                        #pisele de pe pozitia 5 si 11
        #TODO: foloseste un tuple pentru stocarea pozitiilor defaul ale pieselor
        for elem in range(5):
                pos5.addWidget(Checkers("black", pos5))
                pos11.addWidget(Checkers("black", pos11))
                        #piesele de pe pozitia 7
        for elem in range(3):
                pos7.addWidget(Checkers("black", pos7))
                        #piesele de pe pozita 20
        for elem in range(2):
                pos20.addWidget(Checkers("black", pos20))
                        #pisele de pe pozitia 10 si 16
        for elem in range(5):
                pos10.addWidget(Checkers("white", pos10))
                pos16.addWidget(Checkers("white", pos16))
                        #piesele de pe pozitia 14
        for elem in range(3):
                pos14.addWidget(Checkers("white", pos14))
                        #piesele de pe pozita 1
        for elem in range(2):
                pos1.addWidget(Checkers("white",pos1))

        QTimer.singleShot(0, lambda: print(f"middleContainer: {middleContainer.width()}"))

        return middleContainer

    def leftContainer(self):

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

        # adaugarea de elemente in fiecare container
        # adaugarea elementelor din stanga
        leftLayout.addWidget(QLabel("Player1", objectName = "labelPlayer1"))
        leftLayout.addWidget(diceContainer)
        leftLayout.addWidget(QLabel("Player2", objectName = "labelPlayer2"))

        QTimer.singleShot(0, lambda: print(f"leftContainer: {leftContainer.width()}"))

        return leftContainer

    def rightContainer(self, gameLogic):
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
            # adaugarea elementelor din dreapta
                # adaugarea containerului pentru piesele albe in containerul drept
        rightLayout.addWidget(whiteCheckersContainer)
                # crearea butonului de Roll
        rollButton = QPushButton()
        rollButton.setObjectName("rollButton")
        #PENTRU A PUTEA OBTINE MARIMEA REALA A  WIDGET ULUI
        QTimer.singleShot(0, lambda: rollButton.setFixedSize(whiteCheckersContainer.width(), whiteCheckersContainer.width()))
                # functia roll care adauga widgetul in diceLayout si returneaza lista cu raruri, care sunt loate de clasa gamoLogic si stocate prin setDices
        rollButton.clicked.connect(lambda: gameLogic.setDices(dices=roll(self.diceLayout)))
        rightLayout.addWidget(rollButton)
                # adaugarea containerului pentru piesele negre in containerul drept
        rightLayout.addWidget(blackCheckersContainer)

        QTimer.singleShot(0, lambda: print(f"rightContainer: {rightContainer.width()}"))
        return rightContainer