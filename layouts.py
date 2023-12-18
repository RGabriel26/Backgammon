from PyQt6.QtWidgets import QWidget, QGridLayout, QVBoxLayout, QHBoxLayout, QLabel
from PyQt6.QtCore import Qt, QTimer

from checkers import *
from functions import *

class UILayouts():
    def __init__(self) -> None:
        super().__init__()

    def setDefaultPosition(self) -> None:
        defaulPosition = {"black" : [(self.pos6, 5), (self.pos13, 5), (self.pos8, 3), (self.pos24, 2)],
                        "white" : [(self.pos12, 5),(self.pos19, 5),(self.pos17, 3),(self.pos1, 2)]}
        for team, posAndCaunt in defaulPosition.items():
            for position, numberOfPieces in posAndCaunt:
                print(position.objectName())
                for i in range(numberOfPieces):
                    position.addWidget(Checkers(team, position))

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
        self.fenceWhiteCheckersLayout = QVBoxLayout(objectName = "fenceWhiteChekersLayout")
        fenceWhiteCheckersContainer.setLayout(self.fenceWhiteCheckersLayout)

        fenceBlackCheckersContainer = QWidget(objectName = "fenceBlackCheckersContainer")
        self.fenceBlackCheckersLayout = QVBoxLayout(objectName = "fenceBlackCheckersLayout")
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
        self.setDefaultPosition()
        
        # adaugare de test a pieselor pe gard
        self.fenceWhiteCheckersLayout.addWidget(Checkers("white", self.fenceWhiteCheckersLayout))
        self.fenceBlackCheckersLayout.addWidget(Checkers("black", self.fenceBlackCheckersLayout))
             
        
        # pentru a testa incadrarea -> afisarea a n piese de joc pe fiecare pozitie

        # positions = [pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9, pos10, pos11, pos12, pos13, pos14, pos15, pos16, pos17, pos18, pos19, pos20, pos21, pos22, pos23, pos24]
        # for pos in positions:
        #         for i in range(5):
        #                 pos.addWidget(Checkers("black", pos))      

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

        # adaugarea de elemente in fiecare container
        # adaugarea elementelor din stanga
        leftLayout.addWidget(QLabel("Player1", objectName = "labelPlayer1"))
        leftLayout.addWidget(diceContainer)
        leftLayout.addWidget(QLabel("Player2", objectName = "labelPlayer2"))

        # QTimer.singleShot(0, lambda: print(f"leftContainer: {leftContainer.size()}"))
        return leftContainer

    def rightContainer(self, gameLogic):
        # piesele scoase de jucatori
            #creara containerului in care se fa crea layout-ul din partea dreapta
        rightContainer = QWidget()
        rightContainer.setObjectName("rightContainer")
        rightLayout = QVBoxLayout()
        rightContainer.setLayout(rightLayout)
            # setarea containerelor pentru piesele care vor fi scoase din joc
                # crearea containerului pentru piesele ce vor fi scoase de jucatorul WHITE
        whiteCheckersContainer = QWidget()
        whiteCheckersContainer.setObjectName("whiteCheckersContainer")
        self.whiteCheckersLayout = QVBoxLayout()
        whiteCheckersContainer.setLayout(self.whiteCheckersLayout)
                # crearea containerului pentru piesele ce vor fi scoase de jucatorul BLACK
        blackCheckersContainer = QWidget()
        blackCheckersContainer.setObjectName("blackCheckersContainer")
        self.blackCheckersLayout = QVBoxLayout()
        blackCheckersContainer.setLayout(self.blackCheckersLayout)
                # crearea butonului de Roll
        rollButton = QPushButton()
        rollButton.setObjectName("rollButton")
        #PENTRU A PUTEA OBTINE MARIMEA REALA A WIDGET ULUI 
        QTimer.singleShot(0, lambda: rollButton.setFixedSize(whiteCheckersContainer.width(), whiteCheckersContainer.width()))
                # functia roll care adauga widgetul in diceLayout si returneaza lista cu raruri, care sunt salvate in clasa gamoLogic si stocate prin setDices
        rollButton.clicked.connect(lambda: gameLogic.setDices(roll(self.diceLayout)))

            # adaugarea elementelor din dreapta
        rightLayout.addWidget(whiteCheckersContainer)
        rightLayout.addWidget(rollButton)
        rightLayout.addWidget(blackCheckersContainer)

        self.whiteCheckersLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.whiteCheckersLayout.setContentsMargins(0, 5, 0, 5)

        self.blackCheckersLayout.setAlignment(Qt.AlignmentFlag.AlignBottom)
        self.blackCheckersLayout.setContentsMargins(0, 5, 0, 5)

        # adaugarea de test a pieselor scoase
        for i in range(6):
            outCheker  = QLabel(objectName = "outWhiteChecker")
            self.whiteCheckersLayout.addWidget(outCheker)

        for i in range(6):
            outCheker  = QLabel(objectName = "outBlackChecker")
            self.blackCheckersLayout.addWidget(outCheker)

        QTimer.singleShot(0, lambda: print(f"blackCheckersContainer: {outCheker.size()}"))
        return rightContainer
    
    # TODO: De creat functii care sa afauge elemente in partea grafica
            #aici ma refer pe toate layoutuirle, atat pe pozitii, pe gard cat si in exterior, cand 
            #acestea sunt scoase le finalul jocului