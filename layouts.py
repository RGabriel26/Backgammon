from PyQt6.QtWidgets import QWidget, QGridLayout, QVBoxLayout, QHBoxLayout, QLabel, QGraphicsDropShadowEffect
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QColor

from checkers import *

# clasa este apelata de clasa gameLogic
class UILayouts():
    def __init__(self, gameLogic_instance) -> None:
        super().__init__()
        self.gameLogic = gameLogic_instance
        print("initializare layouts...")

    def middleLayout(self):
        middleContainer = QWidget(objectName = "middleContainer")
        middlePrincipalLayout = QHBoxLayout()
        ############################################ zona din STANGA ###############################################################
        middleLeftLayoutContainer = QWidget(objectName = "middleLeftLayoutContainer")
        middleLeftLayout = QVBoxLayout()

        positionTopLeftContainer = QWidget(objectName = "positionTopLeftContainer")
        positionTopLeftLayout = QHBoxLayout()
        pos13Container = QWidget(objectName="pos13Container")
        pos14Container = QWidget(objectName="pos14Container")
        pos15Container = QWidget(objectName="pos15Container")
        pos16Container = QWidget(objectName="pos16Container")
        pos17Container = QWidget(objectName="pos17Container")
        pos18Container = QWidget(objectName="pos18Container")
        self.pos13 = QVBoxLayout()
        self.pos14 = QVBoxLayout()
        self.pos15 = QVBoxLayout()
        self.pos16 = QVBoxLayout()
        self.pos17 = QVBoxLayout()
        self.pos18 = QVBoxLayout()
        pos13Container.setLayout(self.pos13)
        pos14Container.setLayout(self.pos14)
        pos15Container.setLayout(self.pos15)
        pos16Container.setLayout(self.pos16)
        pos17Container.setLayout(self.pos17)
        pos18Container.setLayout(self.pos18)
        positionTopLeftLayout.addWidget(pos13Container)
        positionTopLeftLayout.addWidget(pos14Container)
        positionTopLeftLayout.addWidget(pos15Container)
        positionTopLeftLayout.addWidget(pos16Container)
        positionTopLeftLayout.addWidget(pos17Container)
        positionTopLeftLayout.addWidget(pos18Container)
        positionTopLeftContainer.setLayout(positionTopLeftLayout)
        middleLeftLayout.addWidget(positionTopLeftContainer)

        positionButtonLeftContainer = QWidget(objectName = "positionButtonLeftContainer")
        positionButtonLeftLayout = QHBoxLayout()
        pos7Container = QWidget(objectName="pos7Container")
        pos8Container = QWidget(objectName="pos8Container")
        pos9Container = QWidget(objectName="pos9Container")
        pos10Container = QWidget(objectName="pos10Container")
        pos11Container = QWidget(objectName="pos11Container")
        pos12Container = QWidget(objectName="pos12Container")
        self.pos7 = QVBoxLayout()
        self.pos8 = QVBoxLayout()
        self.pos9 = QVBoxLayout()
        self.pos10 = QVBoxLayout()
        self.pos11 = QVBoxLayout()
        self.pos12 = QVBoxLayout()
        pos7Container.setLayout(self.pos12)
        pos8Container.setLayout(self.pos11)
        pos9Container.setLayout(self.pos10)
        pos10Container.setLayout(self.pos9)
        pos11Container.setLayout(self.pos8)
        pos12Container.setLayout(self.pos7)
        positionButtonLeftLayout.addWidget(pos7Container)
        positionButtonLeftLayout.addWidget(pos8Container)
        positionButtonLeftLayout.addWidget(pos9Container)
        positionButtonLeftLayout.addWidget(pos10Container)
        positionButtonLeftLayout.addWidget(pos11Container)
        positionButtonLeftLayout.addWidget(pos12Container)
        positionButtonLeftContainer.setLayout(positionButtonLeftLayout) 

        middleLeftLayout.addWidget(positionButtonLeftContainer)
        middleLeftLayoutContainer.setLayout(middleLeftLayout)
        ####################################### zona din MIJLOC ############################################
        middleFenceLayoutContainer = QWidget(objectName = "middleFenceLayoutContainer")
        middleFenceLayout = QVBoxLayout()

        fenceWhiteCheckersContainer = QWidget(objectName = "fenceWhiteCheckersContainer")
        self.fenceWhiteCheckersLayout = QVBoxLayout(objectName = "fenceWhiteChekersLayout0")
        fenceWhiteCheckersContainer.setLayout(self.fenceWhiteCheckersLayout)

        fenceBlackCheckersContainer = QWidget(objectName = "fenceBlackCheckersContainer")
        self.fenceBlackCheckersLayout = QVBoxLayout(objectName = "fenceBlackCheckersLayout25")
        fenceBlackCheckersContainer.setLayout(self.fenceBlackCheckersLayout)

        middleFenceLayout.addWidget(fenceWhiteCheckersContainer)
        middleFenceLayout.addWidget(fenceBlackCheckersContainer)

        middleFenceLayoutContainer.setLayout(middleFenceLayout)
        ####################################### zona din DREAPTA ###########################################
        middleRightLayoutContainer = QWidget(objectName = "middleRightLayoutContainer")
        middleRightLayout = QVBoxLayout()

        positionTopRightContainer = QWidget(objectName = "positionTopRightContainer")
        positionTopRightLayout = QHBoxLayout()
        pos19Container = QWidget(objectName="pos19Container")
        pos20Container = QWidget(objectName="pos20Container")
        pos21Container = QWidget(objectName="pos21Container")
        pos22Container = QWidget(objectName="pos22Container")
        pos23Container = QWidget(objectName="pos23Container")
        pos24Container = QWidget(objectName="pos24Container")
        self.pos19 = QVBoxLayout()
        self.pos20 = QVBoxLayout()
        self.pos21 = QVBoxLayout()
        self.pos22 = QVBoxLayout()
        self.pos23 = QVBoxLayout()
        self.pos24 = QVBoxLayout()
        pos19Container.setLayout(self.pos19)
        pos20Container.setLayout(self.pos20)
        pos21Container.setLayout(self.pos21)
        pos22Container.setLayout(self.pos22)
        pos23Container.setLayout(self.pos23)
        pos24Container.setLayout(self.pos24)
        positionTopRightLayout.addWidget(pos19Container)
        positionTopRightLayout.addWidget(pos20Container)
        positionTopRightLayout.addWidget(pos21Container)
        positionTopRightLayout.addWidget(pos22Container)
        positionTopRightLayout.addWidget(pos23Container)
        positionTopRightLayout.addWidget(pos24Container)
        positionTopRightContainer.setLayout(positionTopRightLayout)
        middleRightLayout.addWidget(positionTopRightContainer)

        positionButtonRightContainer = QWidget(objectName = "positionButtonRightContainer")
        positionButtonRightLayout = QHBoxLayout()
        pos1Container = QWidget(objectName="pos1Container")
        pos2Container = QWidget(objectName="pos2Container")
        pos3Container = QWidget(objectName="pos3Container")
        pos4Container = QWidget(objectName="pos4Container")
        pos5Container = QWidget(objectName="pos5Container")
        pos6Container = QWidget(objectName="pos6Container")
        self.pos1 = QVBoxLayout()
        self.pos2 = QVBoxLayout()
        self.pos3 = QVBoxLayout()
        self.pos4 = QVBoxLayout()
        self.pos5 = QVBoxLayout()
        self.pos6 = QVBoxLayout()
        pos1Container.setLayout(self.pos6)
        pos2Container.setLayout(self.pos5)
        pos3Container.setLayout(self.pos4)
        pos4Container.setLayout(self.pos3)
        pos5Container.setLayout(self.pos2)
        pos6Container.setLayout(self.pos1)
        positionButtonRightLayout.addWidget(pos1Container)
        positionButtonRightLayout.addWidget(pos2Container)
        positionButtonRightLayout.addWidget(pos3Container)
        positionButtonRightLayout.addWidget(pos4Container)
        positionButtonRightLayout.addWidget(pos5Container)
        positionButtonRightLayout.addWidget(pos6Container)
        positionButtonRightContainer.setLayout(positionButtonRightLayout) 

        middleRightLayout.addWidget(positionButtonRightContainer)
        middleRightLayoutContainer.setLayout(middleRightLayout)

        # grid uri secundare(cele trei pe coloane)
        middlePrincipalLayout.addWidget(middleLeftLayoutContainer,45)
        middlePrincipalLayout.addWidget(middleFenceLayoutContainer,10)
        middlePrincipalLayout.addWidget(middleRightLayoutContainer,45)

        middleContainer.setLayout(middlePrincipalLayout)

        #setup containerelor
        middleLeftLayout.setContentsMargins(10,8,0,8)
        middleRightLayout.setContentsMargins(0,8,10,8)

        positionTopLeftContainer.setContentsMargins(0,0,0,0)
        positionTopRightContainer.setContentsMargins(0,0,0,0)
        positionButtonLeftContainer.setContentsMargins(0,0,0,0)
        positionButtonRightContainer.setContentsMargins(0,0,0,0)

        positionTopLeftLayout.setContentsMargins(0,0,0,0)
        positionButtonLeftLayout.setContentsMargins(0,0,0,0)
        positionTopRightLayout.setContentsMargins(0,0,0,0)
        positionButtonRightLayout.setContentsMargins(0,0,0,0)

        # stilizarea layout ului pentru piesele de pe gard
        self.fenceWhiteCheckersLayout.setSpacing(0)
        self.fenceWhiteCheckersLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.fenceWhiteCheckersLayout.setContentsMargins(0, 0, 0, 0)

        self.fenceBlackCheckersLayout.setSpacing(0)
        self.fenceBlackCheckersLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.fenceBlackCheckersLayout.setContentsMargins(0, 0, 0, 0)

        #setarea proprietailor layout-urilor de pozitionare a pieselor
        positions = [self.pos1, self.pos2, self.pos3, self.pos4, self.pos5, self.pos6, self.pos7, self.pos8, self.pos9, self.pos10,
                        self.pos11, self.pos12, self.pos13, self.pos14, self.pos15, self.pos16, self.pos17, self.pos18,
                        self.pos19, self.pos20, self.pos21, self.pos22, self.pos23, self.pos24]

        for i in range(12):
                positions[i].setObjectName(f"pos{i+1}")
                positions[i].setSpacing(0)
                positions[i].setAlignment(Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignCenter)
                positions[i].setContentsMargins(0, 0, 0, 0)

        for i in range(12, 24):
                positions[i].setObjectName(f"pos{i+1}")
                positions[i].setSpacing(0)
                positions[i].setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignCenter)
                positions[i].setContentsMargins(0, 0, 0, 0)

        #pozitionarea pe locurile default ale pieselor
        self.gameLogic.setDefaultPosition()

        self.positions = [self.pos1, self.pos2,self.pos3, self.pos4, self.pos5,self.pos6, self.pos7, self.pos8,self.pos9,
                     self.pos10,self.pos11,self.pos12,self.pos13,self.pos14,self.pos15,self.pos16,self.pos17,self.pos18,
                     self.pos19,self.pos20,self.pos21,self.pos22,self.pos23,self.pos24,
                     self.fenceWhiteCheckersLayout, self.fenceBlackCheckersLayout]
        
        self.buttonPositions = [self.pos1, self.pos2, self.pos3, self.pos4, self.pos5, self.pos6, self.pos7, 
                          self.pos8, self.pos9, self.pos10, self.pos11, self.pos12]
        
        # doar de test
        
        # self.pos18.addWidget(Checkers(team="white", positionName=self.pos18.objectName(), gameLogic = self.gameLogic))
        # self.pos18.addWidget(Checkers(team="white", positionName=self.pos18.objectName(), gameLogic = self.gameLogic))
        # self.pos2.addWidget(Checkers(team="white", positionName=self.pos2.objectName(), gameLogic = self.gameLogic))
        # self.pos2.addWidget(Checkers(team="white", positionName=self.pos2.objectName(), gameLogic = self.gameLogic))
        # self.pos7.addWidget(Checkers(team="white", positionName=self.pos7.objectName(), gameLogic = self.gameLogic))
        # self.pos7.addWidget(Checkers(team="white", positionName=self.pos7.objectName(), gameLogic = self.gameLogic))

        # self.pos20.addWidget(Checkers(team="white", positionName=self.pos20.objectName(), gameLogic = self.gameLogic))
        # self.pos20.addWidget(Checkers(team="white", positionName=self.pos20.objectName(), gameLogic = self.gameLogic))
        # self.pos21.addWidget(Checkers(team="white", positionName=self.pos21.objectName(), gameLogic = self.gameLogic))
        # self.pos21.addWidget(Checkers(team="white", positionName=self.pos21.objectName(), gameLogic = self.gameLogic))
        # self.pos22.addWidget(Checkers(team="white", positionName=self.pos22.objectName(), gameLogic = self.gameLogic))
        # self.pos22.addWidget(Checkers(team="white", positionName=self.pos22.objectName(), gameLogic = self.gameLogic))
        # self.pos23.addWidget(Checkers(team="white", positionName=self.pos23.objectName(), gameLogic = self.gameLogic))
        # self.pos23.addWidget(Checkers(team="white", positionName=self.pos23.objectName(), gameLogic = self.gameLogic))  

        # QTimer.singleShot(0, lambda: print(f"pos10Container: {pos10Container.size()}"))
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

        #butonul de start
        self.startButton = QPushButton("START", objectName = "startButton")
        self.startButton.setFixedSize(50,50)
        self.startButton.clicked.connect(lambda: self.gameLogic.funcStartButton())

        self.diceLayout.addWidget(self.startButton)

        # adaugarea de elemente in fiecare container
        # adaugarea elementelor din stanga
        self.labelPlayerWhite = QLabel("Player1", objectName = "labelPlayer1")
        leftLayout.addWidget(self.labelPlayerWhite)
        leftLayout.addWidget(diceContainer)
        self.labelPlayerBlack = QLabel("Player2", objectName = "labelPlayer2")
        leftLayout.addWidget(self.labelPlayerBlack)

        # QTimer.singleShot(0, lambda: print(f"leftContainer: {leftContainer.size()}"))
        return leftContainer

    def rightContainer(self):
        # piesele scoase de jucatori
            #creara containerului in care se fa crea layout-ul din partea dreapta
        rightContainer = QWidget()
        rightContainer.setObjectName("rightContainer")
        rightLayout = QVBoxLayout()
        rightContainer.setLayout(rightLayout)
            # setarea containerelor pentru piesele care vor fi scoase din joc
                # crearea containerului pentru piesele ce vor fi scoase de jucatorul WHITE
        self.outWhiteCheckersContainer = QWidget()
        self.outWhiteCheckersContainer.setObjectName("whiteCheckersContainer")
        self.outWhiteCheckersLayout = QVBoxLayout()
        self.outWhiteCheckersContainer.setLayout(self.outWhiteCheckersLayout)
        self.outWhiteCheckersContainer.mousePressEvent = lambda event: self.gameLogic.manageOutCheker()
        self.outWhiteCheckersContainer.setEnabled(False)
                # crearea containerului pentru piesele ce vor fi scoase de jucatorul BLACK
        self.outBlackCheckersContainer = QWidget()
        self.outBlackCheckersContainer.setObjectName("blackCheckersContainer")
        self.outBlackCheckersLayout = QVBoxLayout()
        self.outBlackCheckersContainer.setLayout(self.outBlackCheckersLayout)
        self.outBlackCheckersContainer.mousePressEvent = lambda event: self.gameLogic.manageOutCheker()
        self.outBlackCheckersContainer.setEnabled(False)
        # crearea butonului de Roll
        self.rollButton = QPushButton()
        self.rollButton.setObjectName("rollButton")
        #QTime.singleShot(0) asteapta ca interfata grafica sa se termine de randat, dupa care executa comanda
        QTimer.singleShot(0, lambda: self.rollButton.setFixedSize(self.outWhiteCheckersContainer.width(), self.outWhiteCheckersContainer.width()))
                # functia roll care adauga widgetul in diceLayout si returneaza lista cu raruri, care sunt salvate in clasa gamoLogic si stocate prin setDices
        self.rollButton.clicked.connect(lambda: self.gameLogic.roll(self.diceLayout))
        self.gameLogic.enableRollButton(False)

            # adaugarea elementelor din dreapta
        rightLayout.addWidget(self.outWhiteCheckersContainer)
        rightLayout.addWidget(self.rollButton)
        rightLayout.addWidget(self.outBlackCheckersContainer)

        self.outWhiteCheckersLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.outWhiteCheckersLayout.setContentsMargins(0, 5, 0, 5)

        self.outBlackCheckersLayout.setAlignment(Qt.AlignmentFlag.AlignBottom)
        self.outBlackCheckersLayout.setContentsMargins(0, 5, 0, 5)

        # QTimer.singleShot(0, lambda: print(f"blackCheckersContainer: {outCheker.size()}"))
        return rightContainer