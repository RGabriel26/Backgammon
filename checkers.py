from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import pyqtSignal, QTimer

class Checkers(QPushButton):
    """Clasa de creare a unui obiect de tip QPushButton care va reprezenta o piesa de joc.\n
    Metodele disponibile acestei clase:
        - getTeam()
        - setHover(bool)
        - enterEvent(event)
        - leaveEvent(event)
        - hover(is_hovered)
        - click()
    """
    # crearea instantei de semnal pentru evenimentul hover
    hovered = pyqtSignal(bool)

    # (self, culoarea piesei, numarul pozitiei pentru a identifica layout ul de pozitionare, instanta gameLogic)
    # sourceCheckers este folosit pentru diferentirea pieselor, daca:
        # - piesa este una reala, sourceCheckers = 0
        # - piesa este una ghost, sourceCheckers = 1,2,3,4,5,6 (in functie de numarul de zaruri folosite pentru crearea piesei ghost)
    def __init__(self, team, positionName, gameLogic, usedDice = 0, replaceCheckers = False):
        super().__init__()
        self.gameLogic = gameLogic
        self.setObjectName(f'{team}Checker')
        self.setFixedSize(50,50)
        
        self.team = team
        self.oponentTeam = "black" if team == "white" else "white"
        self.positionName = positionName
        self.isHoverEnable = True
        self.canDeleteGhostCheckers = True
        self.usedDice = usedDice
        self.replaceCheckers = replaceCheckers
    
        self.hovered.connect(self.hover)
        self.clicked.connect(self.click)
    
    # functii esentiale pentru evenimentele hover
    def enterEvent(self, event):
        self.hovered.emit(True)

    def leaveEvent(self, event):
        self.hovered.emit(False)
    
    # functii apelante la aparitia unui event

    def hover(self, is_hovered):
        """Functie apelata cand mouse-ul intra sau iese de pe piesa
        apeleaza functia de afisare a pieselor gost pe pozitiile posibile
        in functie de zaruri.\n
        Apeleaza functiile: 
            - showPossibleMove(positionName) din gameLogic.py
            - deleteGostCheckers() din gameLogic.py
            - oponentChekerVisibility(isVisible, position) din gameLogic.py\n
        Cand piesa nu mai este in focusul mouse-ului se sterg piesele gost 
        de pe pozitiile posibile.\n
        Daca o piesa sunt piese gost pe gard, se vor reafisa piesele adversarului
        pe pozitiile anterioare de unde au fost luate."""
        
        # verificarea restrictii: 
        if not self.gameLogic.isGlobalCheckerActive:
            # se asteapta apasarea butonului de start pentru a indica inceperea jocului, implicit si interactiunea cu piesele
            return
        # Conditie pentri a dezactiva hoverul pieselor albe
        if self.team == "white" and self.gameLogic.isWhiteCheckerEnable == False:
            return
        # Conditie pentri a dezactiva hoverul pieselor negre
        if self.team == "black" and self.gameLogic.isBlackCheckerEnable == False:
            return
        
        if self.gameLogic.isGlobalHoverEnable and self.team not in ['ghostFenceWhite', 'ghostFenceBlack']:
            if is_hovered and self.isHoverEnable and self.team != 'ghost':
                # cand piesa este in focusul mouse-ului se apeleaza functia care afiseaza 
                # pe pozitiile posibile dictate de ce zar a picat si adauga piesele gost
                self.gameLogic.showPossibleMove(posName = self.positionName, team = self.team)
                # Doar de test
                # print(f"Piesa {self.team} a fost selectata prin hover event: {self.positionName}")
            else:
                if self.team != 'ghost':
                    # cand piesa nu mai este in focusul mouse-ului
                    # se sterg piesele gost daca este permis acest lucru
                    self.gameLogic.deleteGhostCheckers(self.gameLogic.canDeleteGhostCheckers)
                    # si se reafiseaza piesele adversarului daca acestea au fost aruncate pe gard 
                    # lucru salvat in instanta gameLogic ca o lista nu numarul pozitiei de unde a fost scoasa piesa
                    if len(self.gameLogic.fencedCheckers) > 0:
                        while len(self.gameLogic.fencedCheckers) > 0:
                            position = self.gameLogic.fencedCheckers.pop()
                            self.gameLogic.oponentChekerVisibility(True, position, self.oponentTeam)

                    # dezactivarea zonei de scoatere a pieselor
                    self.gameLogic.highlightOutPosibility(False)
                    # resetara variabilei care stocheaza zarul folosit pentru scoaterea piesei din joc
                    self.gameLogic.usedDiceForOutCheckers = None
        

    def click(self):
        # RESTRICTII:
        # se asteapta apasarea butonului de start pentru a indica inceperea jocului, implicit si interactiunea cu piesele
        if not self.gameLogic.isGlobalCheckerActive:
            return
        # Conditie pentri a dezactiva piesele jucatorului  WHITE
        if self.team == "white" and self.gameLogic.isWhiteCheckerEnable == False:
            return
        # Conditie pentri a dezactiva piesele jucatorului BLACK
        if self.team == "black" and self.gameLogic.isBlackCheckerEnable == False:
            return

        anteriorPosition = None
        # Excluderea pieselor ghost de pe gard
        if self.team not in ['ghostFenceWhite', 'ghostFenceBlack']:
            # Event de click pentru piesele ghost
            if self.team == "ghost":
                # Aici trebuie sa se inlocuiasca piesa ghost pe care s-a dat click cu o piesa a jucatorului curent
                # Iar de pe pozitia de unde s-a facut anterior click pe o piesa reala, sa se elimine piesa
                # se sterg piesele ghost
                self.gameLogic.deleteGhostCheckers(True)
                # se adauga piesa reala pe pozitia de unde s-a dat click pe piesa ghost
                self.gameLogic.addCheckerToPosition(self.positionName, self.gameLogic.teamTurn)
                # stergerea piesei de pe pozitia de unde s-a initiat mutarea
                posID = self.gameLogic.getPosID(self.positionName)
                anteriorPosition = posID - self.usedDice if self.gameLogic.teamTurn == 'white' else posID + self.usedDice
                # daca anteriorPosition este == 0 sau 25, inseamna ca piesa selectata se afla pe gard, 
                # pozitia 0 este pentru piesele white de pe gard
                # pozitia 25 este pentru piesele black de pe gard
                if anteriorPosition == 0:
                    # piesa selectata de pe gard este a jucatorului white
                    self.gameLogic.layouts.fenceWhiteCheckersLayout.itemAt(0).widget().deleteLater()
                    self.gameLogic.numberWhiteFenceCheckers -= 1
                elif anteriorPosition == 25:
                    # piesa selectata de pe gard este a jucatorului black
                    self.gameLogic.layouts.fenceBlackCheckersLayout.itemAt(0).widget().deleteLater()
                    self.gameLogic.numberBlackFenceCheckers -= 1
                else:
                    self.gameLogic.deleteCheckerFromPosition(anteriorPosition)
                # se verifica daca piesa gost pe care s-a apasat a inlocuit sau nu o piesa a adversarului
                # daca da, se va elimina indexul pozititiei din lista de piese gost de pe gard, index salvat in instanta gameLogic in lista fencedCheckers
                # astfel, nu se va mai recrea piesa adversarului pe pozitia anterioara
                if self.replaceCheckers:
                    self.gameLogic.fencedCheckers.remove(self.gameLogic.getPosID(self.positionName))
                    self.gameLogic.addCheckerToFence('black' if self.gameLogic.teamTurn == 'white' else 'white')

                # stergerea zarurului folosit pentru realizarea mutarii
                self.gameLogic.dices.remove(self.usedDice)
                # stergerea zarului folosit din diceLayout
                self.gameLogic.deleteDiceFromLayout(deleteDice = self.usedDice)
                # dupa plasarea unei piese reale, se va reactiva eventul de hover pentru a putea fi afisate piesele gost
                self.gameLogic.isGlobalHoverEnable = True
                # se va activa factorul de stergere a pieselor ghost
                self.gameLogic.canDeleteGhostCheckers = True
                self.gameLogic.clickCounter = 0

                # RESTRICTII:
                # Verificare daca jucatorul poate realiza mutari cu zarurile primite
                # Tot aici este tratat si cazul cand jucatorul nu mai are zaruri disponibile pentru a realiza mutari
                if self.gameLogic.canMakeMove() == False:
                    if len(self.gameLogic.dices) > 0:
                        # cazul cand mai sunt zaruri disponibile dar nu se mai pot realiza mutari
                        self.gameLogic.messageWindow.messageBox(1)
                        QTimer.singleShot(3000, lambda: self.gameLogic.actionAfterMessage())
                    else:
                        # czul cand nu mai sunt zaruri disponibile
                        self.gameLogic.isGlobalCheckerActive = False
                        self.gameLogic.logic()

            # Event de click pentru piesele reale ale jucatorilo
            if self.team != "ghost":
                if self.gameLogic.clickCounter % 2 != 0:
                    self.gameLogic.isGlobalHoverEnable = True
                    self.gameLogic.canDeleteGhostCheckers = True
                    self.gameLogic.deleteGhostCheckers(True)
                    self.gameLogic.showPossibleMove(posName = self.positionName, team = self.team) 
                else:
                    self.gameLogic.isGlobalHoverEnable = False
                    self.gameLogic.canDeleteGhostCheckers = False
                self.gameLogic.clickCounter += 1

        # salvarea pozitiei ultimei piese selectate, folosita pentru a sterge piesele dupa ce acestea au fost scoase din joc
        self.gameLogic.lastClickedChecker = self.positionName

        # RESTRICTII:
        # Restrictia pieselor pe gard care face ca celelalte piese sa fie indisponibile pana cand toate piesele de pe gard sunt mutate inapoi in joc:
        if anteriorPosition == 0 or anteriorPosition == 25:
            # folosim QTimer pentru a astepta stergerea completa a pieselor de pe gard
            QTimer.singleShot(0, lambda: self.gameLogic.restrictionFence(anteriorPosition))
        print('click - sfarsit click event')

        # Doar de test
        # print(f"Piesa {self.team} a fost selectata prin clicked event: {self.positionName}")