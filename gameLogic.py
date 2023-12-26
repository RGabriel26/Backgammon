from PyQt6.QtGui import QPixmap
from random import randint

from layouts import *

class GameLogic():
    """Clasa care va gestiona toata logica jocului.\n
    Metodele disponibile acestei clase:
        - saveDices(dices)
        - getDices()
        - createDiceObject(urlImage)
        - roll(diceLayout)
        - logic()
        - addOutCheker(team) 
        - addCheckerToFence(team)
        - addCheckerToPosition(toPos_name, team)
        - showPossibleMove(posName, oponentTeam = "black")
        - oponentChekerVisibility(visibility, numberOfPos)
        - checkersDisponibility(team, disponibility)
        - deleteGhostCheckers()
        - funcStartButton()
        - enableRollButton(isEnable)
        - setDefaultPosition()
        """
    # TODO: TASK:
    # - imlementarea jogicii jocului, astfel ca jucatorii sa poata accesa piesele pe rand
    def __init__(self):
        print("initializare gameLogic...")
        # folosit pentru a stoca zarurile generate in functia roll din RollFunctionalities
        self.dices = []
        self.layouts = UILayouts(self)
        self.fencedCheckers = []
        self.clickCounter = 0
        self.isGlobalCheckerInteractiv = False
        self.isGlobalHoverEnable = True
        self.canDeleteGhostCheckers = True
        self.possibleMove = []
        
        self.teamTurn = "white"
    
    def saveDices(self,dices) -> QLabel:
        if dices[0] == dices[1]:
            self.dices = [dices[0] for i in range(4)]
            print(self.dices)
        else:
            self.dices = dices

    def getDices(self) -> list:
        """Functie care returneaza zarurile salvate in cadrul instantei gameLogic.\n
        Apela in functia:
            - showPosibleMove(posName, oponentTeam = "black") din gameLogic.py
        Return: list"""
        return self.dices

    def createDiceObject(self, urlImage) -> QLabel:
        """Functie care creeaza obiectele zarurilor.\n
        Setari aduse obiectelor:
            - dimensiunea
            - setarea imaginii
            - setarea continutului
        Apelata in functia:
            - roll(diceLayout) din gameLogic.py
        Return: QLabel"""
        pixmap = QPixmap(urlImage)
        dice = QLabel()
        dice.setPixmap(pixmap)
        dice.setFixedSize(70,70)
        dice.setScaledContents(True)
        return dice


    def roll(self, diceLayout) -> list:
        """Functia care genereaza cu randint cele 2 zaruri care sunt salvate in self.dices.\n
        Pe langa generarea zarurilor, functia are rolul de a afisa grafic zarurile generate.\n
        Zarurile sunt afisate in gridLayout-ul diceLayout.\n
        Daca exista deja un zar afisat in gridLayout, acesta este sters pentru a nu se suprapune.\n
        Apelata in functia:
            - funcStartButton() din gameLogic.py
        Return: list"""
        dices = [0, 0]
        for index in range(2):
            getDice = randint(1,6)
            dices[index] = getDice
            # stergerea zarului alfat in gridul diceLayout de pe pozitia 0 index pentru a nu se suprapune
            # .itemAtPosition returneaza un QLayoutItem si se foloseste .widget pentru al conveti intr ul widget pentru a permite stergerea
            curentDice = diceLayout.itemAtPosition(0, index)
            if curentDice:
                diceLayout.removeWidget(curentDice.widget())
            diceLayout.addWidget(self.createDiceObject(f"images/dice{getDice}.png"), 0, index)
        return dices
    
    def logic(self) -> None:
        """Functia care va gestiona logica jocului.\n
        Functia va fi apelata la apasarea butonului de start.\n
        Apelata in functia:
            - funcStartButton() din gameLogic.py    
        """

        print("Start game!")
        # initial butonul de dice este dezactivat, dar devine activ dupa apasare btonului de start
        self.enableRollButton(True) # si se ve dezactiva dupa apasarea butonului de rollDice
        self.isGlobalCheckerInteractiv = True # variabila care va activa/dezactiva piesele de pe tabla

        # de test pentru a verifica disponibilitatea butoanelor
        # aceasta functie trebuie utilizatat la diferentierea jucatorilor
        self.checkersDisponibility(team = "black", disponibility = False)
        self.checkersDisponibility(team = "white", disponibility = True)

        print("A iesit din functia logic")

    # functii pentru adaugarea de piese in layout-uri
    def addOutCheker(self, team) -> None:
        """Adauga piesele scoase din joc in layout-urile corespunzatoare in functie de variabila team data ca parametru.\n"""
        if team == "white":
            self.layouts.whiteCheckersLayout.addWidget(QLabel(objectName = "outWhiteChecker"))
        else:
            self.layouts.blackCheckersLayout.addWidget(QLabel(objectName = "outBlackChecker"))

    def addGhostCheckerToFence(self, team) -> None:
        """Adauga piesele aruncate pe gard in layout-urile corespunzatoare in functie de variabila team data ca parametru.\n
        Apelata in functia:
            - showPosibleMove(posName, oponentTeam = "black") din gameLogic.py"""
        if team == "white":
            layout = self.layouts.fenceWhiteCheckersLayout
            layout.addWidget(Checkers(team="ghostFenceWhite", positionName = layout.objectName(), gameLogic = self))
        else:
            layout = self.layouts.fenceBlackCheckersLayout
            layout.addWidget(Checkers(team="ghostFenceBlack", positionName = layout.objectName(), gameLogic = self))

    def addCheckerToFence(self, team) -> None:
        """Adauga piesele aruncate pe gard in layout-urile corespunzatoare in functie de variabila team data ca parametru.\n
        Apelata in functia:
            - showPosibleMove(posName, oponentTeam = "black") din gameLogic.py"""
        if team == "white":
            layout = self.layouts.fenceWhiteCheckersLayout
            layout.addWidget(Checkers(team="white", positionName = layout.objectName(), gameLogic = self))
        else:
            layout = self.layouts.fenceBlackCheckersLayout
            layout.addWidget(Checkers(team="black", positionName = layout.objectName(), gameLogic = self))

    def addCheckerToPosition(self, toPos_name, team, useDice = 0, replaceCheckers = False) -> None:
        """Adauga piesele pe pozitiile corespunzatoare in functie de variabila team data ca parametru.\n
        Pozitionarea pieselor se face in functie de variabila toPos_name data ca parametru.\n
        Apelata in functia:
            - showPosibleMove(posName, oponentTeam = "black") din gameLogic.py"""
        for pos in self.layouts.positions:
             if toPos_name == pos.objectName():
                  pos.addWidget(Checkers(team = team, positionName = pos.objectName(), gameLogic = self, usedDice= useDice, replaceCheckers = replaceCheckers))
   
    def getPosID(self, posName) -> int:
        tempStr = ''
        for char in posName:
            if char.isdigit():
                tempStr = tempStr + char
        return int(tempStr)

    # functie pentru afisarea pozitiilor posibile
    def showPossibleMove(self, posName, oponentTeam) -> None:
        """Functia este responsabila de informarea jucatorilor cu privire la pozitiile posibile pe care se pot folosi.\n
        Pozitiile posibile sunt calculate in functie de zarurile generate.\n
        Pentru a informa jucatorii, pozitiile posibile sunt marcate cu piese ghost, care apar cand una din piesele jucatorului este selectata
        atat cu event de tip hover, cat si cu event de tip click\n
        Apelata in functia:
            - hover(is_hovered) din checkers.py"""
        # obtinerea numarului pozitiei din numele layout-ului
       
        if self.possibleMove or self.dices:
            posID = self.getPosID(posName)
            self.possibleMove.clear() 
            
            # TODO: Ar trebui implementat un sistem care sa calculeze toate pozitiile posibile inclusiv cele prin adunarea zarurilor intre ele
            for dice in self.getDices():
                self.possibleMove.append(posID + dice)

            print(f"Posibile mutari: {self.possibleMove}")

            placedGhostCheckers = 0
            for move in self.possibleMove:
                # zarul folosit pentru a ajunge la pozitia respectiva
                useDice = move - posID
                if move < 24:
                    # verificare daca se poate afisa pozitia rezultata prin adunarea zarurilor
                    # pentru ca piesa sa poata fi afisata pe pozitia rezultata prin adunarea zarurilor
                    # trebuie ca macar unul din zaruri sa fie folosit pentru a ajunge pe pozitia respectiva
                   
                    # if placedGhostCheckers == 0 and move == self.possibleMove[2]:
                    #     break
                # cazul in care pe pozitia posibila exista alte piese
                    if getattr(self.layouts, f'pos{move}').count() > 0:
                        # verificare daca adversarul are cel putin o piesa pe pozitia posibila 
                            # veificam ca pe pozitia respectica sa existe doar o piesa
                        if getattr(self.layouts, f'pos{move}').count() == 1:
                            # daca exista doar o piesa, atunci se verifica daca acesta este a adversarului
                            if getattr(self.layouts, f'pos{move}').itemAt(0).widget().objectName() == f'{oponentTeam}Checker':
                                # daca piesa este a adversarului, atunci se poate muta pe pozitia respectiva
                                    # aici, piesa ghost ar trebui sa inlocuiasca piesa adversarului si
                                    # piesa adversarului ar trebui sa fie aruncata pe gard
                                self.oponentChekerVisibility(visibility = False, numberOfPos = move, oponentTeam = oponentTeam)
                                # lista folosita pentrtu a stica pozitiile de unde au fost aruncate piesele pe gad
                                self.addCheckerToPosition(f'pos{move}', "ghost", useDice, True)
                                self.fencedCheckers.append(move)
                                self.addGhostCheckerToFence(oponentTeam)
                                print(f"piesa adversarului a fost aruncata pe gard de pe pozitia {move}")
                                placedGhostCheckers += 1
                                # piesa adversarului devine din nou vizibila prin apelarea functiei oponentChekerVisibility in functia hover
                        # excluderea pozitiilor unde exista piese ale opentului si sunt mai mult de 1 piese
                        lastChecker = getattr(self.layouts, f'pos{move}').count() - 1
                        if getattr(self.layouts, f'pos{move}').itemAt(lastChecker).widget().objectName() not in [f'{oponentTeam}Checker', 'ghostChecker']:
                            self.addCheckerToPosition(f'pos{move}', "ghost", useDice)
                            placedGhostCheckers += 1
                    else:
                        # cazul in cere pe pozitia posibila nu exista alte piese
                        self.addCheckerToPosition(f'pos{move}', "ghost", useDice)
                        placedGhostCheckers += 1

    # functie pemntru stergerea pieselor adversarului
    def oponentChekerVisibility(self, visibility, numberOfPos, oponentTeam) -> None:
        """Functie care face vizibila/invizibila piesa adversarului.\n
        Folosita la momentul in care pe o posibila pozitie, jucatorul poate face mutare peste adversarul sau.\n
        Conditia este ca adversarul sa aiba doar o piesa pe pozitia respectiva.\n
        Acest lucru arunca piesa adversarului pe gard, iar o piesa ghost inlocuieste piesa adversarului pana la incetarea eventului hover.\n
        Apelata in functia:
            - showPosibleMove(posName, oponentTeam = "black") din gameLogic.py"""
        # cauzeaza probleme cand se face o mutare concreata peste piesa care este aruncata pe gard
        # if visibility:
        #     checker = getattr(self.layouts, f"pos{numberOfPos}").itemAt(0).widget()
        #     checker.show()
        # else:
        #     checker = getattr(self.layouts, f"pos{numberOfPos}").itemAt(0).widget()
        #     checker.hide()
        
        # incercare de a sterge piesa adversarului de pe pozitia respectiva si sau de a o aduga in functie de visibility
        if visibility:
            self.addCheckerToPosition(f'pos{numberOfPos}', oponentTeam)
        else:
            checker = getattr(self.layouts, f"pos{numberOfPos}").itemAt(0).widget()
            checker.deleteLater()

    # functie pentru activarea/dezactivarea pieselor
    def checkersDisponibility(self, team, disponibility) -> None:
        """Functia care face active sau inactive piesele de pe tabla.\n
        In functie de progresul jocului\n
        Daca este randul jucatorului white, atunci piesele black sunt inactive si invers.
        Apelata in functiile:
            - logic() din gameLogic.py
            - hover(is_hovered) din checkers.py"""
        for pos in self.layouts.positions:   
            count = pos.count()
            if count > 0:
                for index in range(count):
                    checker = pos.itemAt(index).widget()
                    if checker.getTeam() == team:
                        checker.setEnabled(disponibility)
                        checker.setHover(disponibility)
                        index -= 1
    # functie pentru stergerea pieselor de pe tabla
    def deleteGhostCheckers(self, canDeleteGhostCheckers) -> None:
        """Functie care sterge piesele ghost de pe tabla.\n
        Apelata in functiile: 
            - hover(is_hovered) din checkers.py
            - roll(diceLayout) din gameLogic.py"""
        if canDeleteGhostCheckers:
            for pos in self.layouts.positions:
                count = pos.count()
                if count > 0:
                    for index in range(count):
                        checker = pos.itemAt(index).widget()
                        if checker.objectName() in ["ghostChecker", "ghostFenceWhiteChecker", "ghostFenceBlackChecker"]:
                            pos.itemAt(index).widget().deleteLater()
                            index -= 1

    def deleteCheckerFromPosition(self, fromPosNumber) -> None:
        for pos in self.layouts.positions:
            if pos.objectName() == f"pos{fromPosNumber}":
                pos.itemAt(0).widget().deleteLater()

    # functie apelata de butonul Start
    def funcStartButton(self) -> None:
        """Functie apelata de butonul Start.\n
        Aceasta ascunde butonul de start si apeleaza functia logic.\n
        Apelata in functia:
            - funcStartButton() din gameLogic.py"""
        self.layouts.startButton.hide()
        self.logic()

    # dunctie pentru activarea/dezactivarea butonului de roll
    def enableRollButton(self, isEnable) -> None:
        """Functie care activeaza sau dezactiveaza butonul de roll.\n
        Activeaza sau dezactiveaza butonul de roll in functie de ce primeste ca parametru.\n
        Apelata in functia:
            - logic() din gameLogic.py"""
        self.layouts.rollButton.setEnabled(isEnable)

    # functie pentru setarea pozitiei default a pieselor
    def setDefaultPosition(self) -> None:
        """Este apelata pentru a crea piesele la inceputul jocului pe pozitiile default ale jocului.\n
        Apelata in functia middleLayout() din layouts.py dupa crearea layout-urilor pentru pozitiile pieselor."""
        defaulPosition = {"black" : [(self.layouts.pos6, 5), (self.layouts.pos13, 5), (self.layouts.pos8, 3), (self.layouts.pos24, 2)],
                          "white" : [(self.layouts.pos12, 5),(self.layouts.pos19, 5),(self.layouts.pos17, 3),(self.layouts.pos1, 2)]}
        for team, posAndCaunt in defaulPosition.items():
            for position, numberOfPieces in posAndCaunt:
                for i in range(numberOfPieces):
                    position.addWidget(Checkers(team = team, positionName = position.objectName(), gameLogic = self, usedDice = 0))

