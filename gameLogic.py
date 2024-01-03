from PyQt6.QtGui import QPixmap
from random import randint

from layouts import *

class GameLogic():
    """Clasa care va gestiona toata logica jocului.\n
    Metodele disponibile acestei clase:
        - saveDices(dices) -> None
        - getDices() -> list
        - createDiceObject(urlImage, usedDice) -> QLabel
        - roll(diceLayout) -> list
        - funcStartButton() -> None
        - enableRollButton(isEnable) -> None
        - logic() -> None
        - stylePlayerTurn() -> None
        - addOutCheker(team) -> None
        - addGhostCheckerToFence(team) -> None
        - addCheckerToFence(team) -> None
        - addCheckerToPosition(toPos_name, team, useDice = 0, replaceCheckers = False) -> None
        - getPosID(posName) -> int
        - getUsedDice(possibleMove, posID, team) -> int
        - showPossibleMove(posName, team) -> None
        - oponentChekerVisibility(visibility, numberOfPos, oponentTeam) -> None
        - deleteGhostCheckers(canDeleteGhostCheckers) -> None
        - deleteCheckerFromPosition(fromPosNumber) -> None
        - deleteDiceFromLayout(deleteDice = None, deteleAll = False) -> None
        - setDefaultPosition() -> None
        """
    # TODO: IMPORTANT: Daca dai roll si primesti un zar pe care nu l poti face, jucatorul at rebui informat, sa se mentina un timp piesele pe dice layout, si sa se primeasca mesajul de informare



    # TODO: Task: BUG MARE: daca o piesa a fost scoasa pe gard, nu culoarea se schimba dar, team ul ramane la fel
    # implementeaza sistemul de pozitionare a pieselor de pe gard, asta genereaza probleme
    # CRED CA ESTE REZOLVAT - NU S-A MAI REPETAT
    
    # TODO: Task: De implementat un sistem care sa afiseze toate pozitiile posibile de pe piesa selectata folosind 
    # zarurile sau zarul disponibil pe pozitiile care permit mutari si de adaugat piesele ghost in locurile corespunzatoare

    # TODO: Task: De gestionat cazul cand jucatorul are doar piese in casa, atuci ar trebui sa fie capabil sa scoata piese
    # este un bug care face sa se treaca peste jucator daca are doar piese in caas si da un zar, iar pe pozitia respectiva zarului nu are nici o piese
    # jocul trece mai departe

    def __init__(self):
        print("initializare gameLogic...")
        # folosit pentru a stoca zarurile generate in functia roll din RollFunctionalities
        self.dices = []
        self.layouts = UILayouts(self)
        self.lastClickedChecker = None # folosit pentru a stoca ultima piesa selectata
        self.usedDiceForOutCheckers = None # folosit pentru a stoca zarul folosit pentru a scoate piesa din joc
        self.fencedCheckers = [] # lista folosita pentru a stoca pozitiile de unde au fost aruncate piesele pe gard
        self.clickCounter = 0  # folosit pentru a numara cate click-uri au fost realizate pe piesa selectata
        self.turnsCounter = 0 # face pozibila trecerea de la un jucator la altul in functia logic
        self.isGlobalCheckerInteractiv = False # folosit doar pentru a bloca piesele la inceputul jocului
        self.canDeleteGhostCheckers = True # ia valoarea False cand se apasa pe o piesa pentru a pastra piesele ghost
        self.isGlobalHoverEnable = True 
        self.isBlackCheckerEnable = True
        self.isWhiteCheckerEnable = True
        self.canTakeOut = True # variabila care activeaza si dezactiveaza interactiunea cu "butonul" care scoate piesele din joc
        self.possibleMove = []# lista de pozitii posibile corespunzatoare selectarii unei piese: podID + dice
        self.teamTurn = "white" # variabila care stocheaza tipul jucatorului al carui ii este randul sa face actiuni in joc
    
    def saveDices(self,dices) -> QLabel:
        self.dices = dices

    def getDices(self) -> list:
        """Functie care returneaza zarurile salvate in cadrul instantei gameLogic.\n
        Apela in functia:
            - roll(diceLayout) din gameLogic.py\n
        Return: list"""
        return self.dices

    def createDiceObject(self, urlImage, usedDice) -> QLabel:
        """Functie care creeaza obiectele zarurilor.\n
        Creaza obiecte de tip QLabel cu objectName = 'dice{usedDice}'
        - usedDice -> numarul corespunzator zarurilor generate\n
        Apelata in functia:
            - roll(diceLayout) din gameLogic.py\n
        Return: QLabel"""
        pixmap = QPixmap(urlImage)
        dice = QLabel()
        dice.setPixmap(pixmap)
        dice.setFixedSize(70,70)
        dice.setScaledContents(True)
        dice.setObjectName(f"dice{usedDice}")
        return dice

    def roll(self, diceLayout) -> None:
        """Functia care genereaza cu randint cele 2 zaruri care sunt salvate in self.dices.\n
        Pe langa generarea zarurilor, functia are rolul de a afisa grafic zarurile generate in diceLayout.\n
        Daca exista deja un zar afisat in gridLayout, acesta este sters pentru a nu se suprapune.\n
        Daca zarurile generate sunt egale, atunci se vor afisa 4 zaruri corespunzatoare dublurii.\n
        Apelata in functia:
            - rollDice() din RollFunctionalities.py\n
        Return: list"""
        dices = []
        # gemerarea celor 2 zaruri
        for index in range(2):
            getDice = randint(1,6)
            dices.append(getDice)
        # stergerea zarului alfat in gridul diceLayout de pe pozitia 0 index pentru a nu se suprapune
        if diceLayout.count() > 0:
            self.deleteDiceFromLayout(deleteAll = True) # daca exista deja zaruri afisate, atunci se sterg zarurile din latyout
        
        # se salveaza zarurile generate in self.dices prin apelarea functiei saveDices
        if dices[0] == dices[1]:
            dices = [dices[0], dices[0], dices[0], dices[0]] # daca au fost generate zaruri duble, atuci se vor salva 4 zaruri corespunzatoare dublei
            # daca nu, se vor salva doar cele 2 zaruri generate
        self.saveDices(dices)
        
        # afisarea obiectelor corespunzatoare zarurilor generate
        for index, getDice in enumerate(dices):
            position = [0,1,0,1]
            diceLayout.addWidget(self.createDiceObject(f'images/dice{getDice}', getDice) , 0 if index < 2 else 1, position[index])
        
        # TODO: enableRollButton trebuie sa fie setat pe false
        self.enableRollButton(True) # dezactivarea buronului de roll 
        self.isGlobalCheckerInteractiv = True # activarea pieselor de pe tabla

        # RESTRICTII
        # Verificare daca jucatorul poate realiza mutari cu zarurile primite
        print(f"Jucatorul {self.teamTurn} a primit zarurile: {self.dices}")
        if self.layouts.fenceWhiteCheckersLayout.count() > 0 and self.teamTurn == "white" or self.layouts.fenceBlackCheckersLayout.count() > 0 and self.teamTurn == "black" :
            if self.canMakeMove(fromFence = True) == False:
                print('Nu se pot face mutari cu zarurile primite.\nSe va trece la jucatorul urmator')
                self.dices.clear()
                self.deleteDiceFromLayout(deleteAll = True)
                self.isGlobalCheckerInteractiv = False
                self.logic()
        else:
            if self.canMakeMove() == False:
                print('Nu se pot face mutari cu zarurile primite.\nSe va trece la jucatorul urmator')
                self.dices.clear()
                self.deleteDiceFromLayout(deleteAll = True)
                self.isGlobalCheckerInteractiv = False
                self.logic()

    def funcStartButton(self) -> None:
        """Functie apelata de butonul Start.\n
        Aceasta ascunde butonul de start si apeleaza functia logic.\n"""
        self.layouts.startButton.hide()
        self.logic()

    def enableRollButton(self, isEnable) -> None:
        """Functie care activeaza sau dezactiveaza butonul de roll.\n
        Activeaza sau dezactiveaza butonul de roll in functie de ce primeste ca parametru.\n
        Apelata in functia:
            - logic() din gameLogic.py"""
        self.layouts.rollButton.setEnabled(isEnable)

    def logic(self) -> None:
        """Functia care va gestiona logica jocului.\n
        Functia va fi apelata la apasarea butonului de start.\n
        Apelata in functia:
            - funcStartButton() din gameLogic.py\n
            - roll() din gameLogic.py\n
            - click() din checkers.py\n

        """
        print("Start game!")
        print(f"Este randul jucatorului {self.teamTurn}!")

        # Conditia de win:
        if self.countOutCheckers() == 15:
            print(f"Jucatorul {self.teamTurn} a castigat!")
            return
        
        # initial butonul de dice este dezactivat, dar devine activ dupa apasare btonului de start
        self.enableRollButton(True) # si se ve dezactiva dupa apasarea butonului de rollDice in functia roll
        # TODO: Verifica care e treaba cu self.isGlobalCheckerInteractiv si de ce este comentat
        # self.isGlobalCheckerInteractiv = False # variabila care va activa/dezactiva piesele de pe tabla

        if self.turnsCounter % 2 == 0:
            self.teamTurn = "white"
            self.isWhiteCheckerEnable = True
            self.isBlackCheckerEnable = False
            # verificare daca jucatorul are piese pe gard
            if self.checkFence("white") > 0:
                self.disponibilityPlayerCheckers("white", False)
            
        else:
            self.teamTurn = "black"
            self.isWhiteCheckerEnable = False
            self.isBlackCheckerEnable = True
            # verificare daca jucatorul are piese pe gard
            if self.checkFence("black") > 0: 
                self.disponibilityPlayerCheckers("black", False)
            

        self.stylePlayerTurn()
        self.turnsCounter += 1

        print("A iesit din functia logic")
        
    def disponibilityPlayerCheckers(self, team, disponibility) -> None:
        """Functia care face disponibile sau nu piesele jucatorului.\n
        Folosit cand este nevoie de indeplinirea unei conditii pentru ca jucatorul sa poata continua jocul.\n"""
        for pos in self.layouts.positions[:-2]:
            if pos.count() > 0:
                if pos.itemAt(0).widget().objectName() == f"{team}Checker":
                    for index in range(pos.count()):
                        layoutPosition = pos.itemAt(index).widget()
                        layoutPosition.setEnabled(disponibility)
                        layoutPosition.isHoverEnable = disponibility

    def checkFence(self, team) -> int:
        if team == "white":
            return self.layouts.fenceWhiteCheckersLayout.count()
        else:
            return self.layouts.fenceBlackCheckersLayout.count()

    def restrictionFence(self, anteriorPosition) -> None:
        # verificarea restrictiilor
        if anteriorPosition == 0:
            # mentinerea restrictiei cand jucatorul are piese pe gard
            if self.checkFence("white") > 0:
                self.disponibilityPlayerCheckers("white", False)
            else:
                self.disponibilityPlayerCheckers("white", True)
        elif anteriorPosition == 25:
            # mentinerea restrictiei cand jucatorul are piese pe gard
            if self.checkFence("black") > 0: 
                self.disponibilityPlayerCheckers("black", False)
            else:
                self.disponibilityPlayerCheckers("black", True)

    def stylePlayerTurn(self) -> None:
        """Functie care seteaza styleSheet-ul pentru label-urile unde sunt afisate numele jucatorilor, pentru a indica al cui este randul sa realizaze mutari.\n"""
        highlightColor = "rgba(67, 200, 176, 0.8)"
        turnStylePlayerWhite = f"""
    background-color:  {highlightColor};
    color: white;
    font-weight: bold;
    font-size: 25px;
    margin: 60% 0% 45% 0%;
    border-radius: 25%;"""
        
        defaultTurnStylePlayerWhite = """
    color: white;
    font-weight: bold;
    font-size: 25px;
    margin: 60% 0% 45% 0%;
    border-radius: 25%;"""
        
        turnStylePlayerBlack = f"""
    background-color:  {highlightColor};
    color: white;
    font-weight: bold;
    font-size: 25px;
    margin: 45% 0% 60% 0%;
    border-radius: 25%;"""
        
        defaultTurnStylePlayerBlack = """
    color: white;
    font-weight: bold;
    font-size: 25px;
    margin: 45% 0% 60% 0%;
    border-radius: 25%;"""
        
        if self.teamTurn == "white":
            self.layouts.labelPlayerWhite.setStyleSheet(turnStylePlayerWhite)
            self.layouts.labelPlayerBlack.setStyleSheet(defaultTurnStylePlayerBlack)
        else:
            self.layouts.labelPlayerBlack.setStyleSheet(turnStylePlayerBlack)
            self.layouts.labelPlayerWhite.setStyleSheet(defaultTurnStylePlayerWhite)

    def addOutCheker(self) -> None:
        """Adauga piesele scoase din joc in layout-urile corespunzatoare in functie de jucatorul care care posibilitatea de a realiza mutari pe tabla.\n"""
        if self.teamTurn == 'white':
            self.layouts.outWhiteCheckersLayout.addWidget(QLabel(objectName = "outWhiteChecker"))
        else:
            self.layouts.outBlackCheckersLayout.addWidget(QLabel(objectName = "outBlackChecker"))
    
    def manageOutCheker(self) -> None:
        self.highlightOutPosibility(False)
        posID = self.getPosID(self.lastClickedChecker)
        self.deleteCheckerFromPosition(posID)
        self.deleteGhostCheckers(True)

        # stergerea zarului folosit din lista de zaruri
        print(f'zarul folosit pentru scoaterea piesei din joc: {self.usedDiceForOutCheckers}')
        self.dices.remove(self.usedDiceForOutCheckers)
        print(f'lista de zaruri dupa stergerea zarului folosit: {self.dices}')
        # stergerea zarului folosit din diceLayout
        self.deleteDiceFromLayout(deleteDice = self.usedDiceForOutCheckers)
        # dupa plasarea unei piese reale, se va reactiva eventul de hover pentru a putea fi afisate piesele gost
        self.isGlobalHoverEnable = True
        self.canDeleteGhostCheckers = True
        self.clickCounter = 0

        self.addOutCheker()

        # stergerea datelor folosite
        self.lastClickedChecker = None
        self.usedDiceForOutCheckers = None

        # TODO: De folosit sistemul de verificare a mutarilor posibile cu canMakeMove
        if not self.dices:
            self.enableRollButton(True)
            self.isGlobalCheckerInteractiv = False
            self.logic()
            
    def createBlurEffect(self, active) -> QGraphicsDropShadowEffect:
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(100)
        shadow.setOffset(0) 
        shadow.setColor(QColor(49, 191, 103))
        shadow.setEnabled(active)
        return shadow
    
    def highlightOutPosibility(self, show = True) -> None:
        """Funtia care seteaza interactiunea cu zonele de iesirea a pieselor jucatorului si evidentierea acestora."""
        if show:
            if self.teamTurn == "white":
                self.layouts.outWhiteCheckersContainer.setEnabled(True)
                self.layouts.outBlackCheckersContainer.setEnabled(False)
                self.layouts.outWhiteCheckersContainer.setGraphicsEffect(self.createBlurEffect(True))
                self.layouts.outBlackCheckersContainer.setGraphicsEffect(self.createBlurEffect(False))
            else:
                self.layouts.outWhiteCheckersContainer.setEnabled(False)
                self.layouts.outBlackCheckersContainer.setEnabled(True)
                self.layouts.outWhiteCheckersContainer.setGraphicsEffect(self.createBlurEffect(False))
                self.layouts.outBlackCheckersContainer.setGraphicsEffect(self.createBlurEffect(True))
        else:
            self.layouts.outWhiteCheckersContainer.setEnabled(False)
            self.layouts.outBlackCheckersContainer.setEnabled(False)
            self.layouts.outWhiteCheckersContainer.setGraphicsEffect(self.createBlurEffect(False))
            self.layouts.outBlackCheckersContainer.setGraphicsEffect(self.createBlurEffect(False))
        
    # TODO: Nu ar fi rau o fuziune intre urmatoarele 2 functii
    def addGhostCheckerToFence(self, team) -> None:
        """Folosita pentru a informa jucatorul atunci cand o mutare de a sa, arunca piese de ale adversarului pe gard, adaugand pe gard piese ghost.\n
        Apelata in functia:
            - showPosibleMove(posName, oponentTeam = "black") din gameLogic.py
            - hover(is_hovered) din checkers.py
            """
        if team == "white":
            layout = self.layouts.fenceWhiteCheckersLayout
            layout.addWidget(Checkers(team="ghostFenceWhite", positionName = layout.objectName(), gameLogic = self))
        else:
            layout = self.layouts.fenceBlackCheckersLayout
            layout.addWidget(Checkers(team="ghostFenceBlack", positionName = layout.objectName(), gameLogic = self))

    def addCheckerToFence(self, team) -> None:
        """Adauga piesele aruncate pe gard in layout-urile corespunzatoare in functie de variabila team data ca parametru.\n
        Apelata in functia:
            - showPosibleMove(posName, oponentTeam = "black") din gameLogic.py
            - hover(is_hovered) din checkers.py
            """
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
            - showPosibleMove(posName, oponentTeam = "black") din gameLogic.py
            - hover(is_hovered) din checkers.py
        """
        for pos in self.layouts.positions:
             if toPos_name == pos.objectName():
                pos.addWidget(Checkers(team = team, positionName = pos.objectName(), gameLogic = self, usedDice = useDice, replaceCheckers = replaceCheckers))

    def getPosID(self, posName) -> int:
        """
        posID -> int-ul care este in numele layout ului selectat\n
        posName -> string corespunzator numelui layout-ului, de preferat un layout corespunzator unei poztitii( pos1 - pos24)\n"""
        tempStr = ''
        for char in posName:
            if char.isdigit():
                tempStr = tempStr + char
        return int(tempStr)

    def getUsedDice(self, possibleMove, posID, team) -> int:
        """Functie care returneaza zarul folosit pentru a ajunge pe pozitia respectiva mutarii.\n"""
        if team == "white":
            return abs(possibleMove - posID)
        else:
            return abs(posID - possibleMove)

    # TODO: optimizeaza
    # TODO: de implementat sistemul de afisare a tuturor pozitiilor posibile
    def showPossibleMove(self, posName, team) -> None:
        """Functia este responsabila de informarea jucatorilor cu privire la pozitiile posibile pe care se pot folosi.\n
        Pozitiile posibile sunt calculate in functie de zarurile generate.\n
        Pentru a informa jucatorii, pozitiile posibile sunt marcate cu piese ghost, care apar cand una din piesele jucatorului este selectata
        prin eveniment de tip hover peste piesa sa, si dispar o data cu incetarea hover-ului asupra piesei.\n
        Apelata in functia:
            - hover(is_hovered) din checkers.py
            - click() din checkers.py
            """
        oponentTeam = "black" if team == "white" else "white"
        if self.dices:
            # obtinerea numarului pozitiei din numele layout-ului
            posID = self.getPosID(posName)
            self.possibleMove.clear() 
            # TODO: Ar trebui implementat un sistem care sa calculeze toate pozitiile posibile inclusiv cele prin adunarea zarurilor intre ele pentru toate combinatiile posibile
            # de ex, pentru 2 2, pozitiile posivile sunt 4 pozitii incepand cu pozitia de pe care se doreste mutarea
            # de ex, pentru 3 3, de pe poziia 1, pozitiile posibile sunt poziaita 4, 6, 9, 12, daca acest lucru este posibil
            # cat timp exista zar, se adauga la pozitia curenta si se afiseaza pozitiile posibile
            # pentru zarurile neperechi, zarurile se adauga pe rand la pozitia curenta si se afiseaza pozitiile posibile, inclusiv pozitia rezultata prin adunarea zarurilor: pozitia curenta + zar 1 + zar 2
            
            # directionarea pieselor in functie de culoarea jucatorului
            # directionarea pieselor jucatorului white
            if team == "white":
                # jucatorul white face mutari de la 1 la 24
                for dice in self.getDices():
                    self.possibleMove.append(posID + dice)
            else:
                # jucatorl black face mutari de la 24 la 1
                for dice in self.getDices():
                    self.possibleMove.append(posID - dice)

            # print(f"Posibilele mutari pentru pozitia {posID} sunt: {self.possibleMove}")
        
            for move in self.possibleMove:
                useDice = self.getUsedDice(move, posID, team)
                if move >= 1 and move <= 24:
                    layoutPosition = getattr(self.layouts, f'pos{move}')
                    # verificare daca se poate afisa pozitia rezultata prin adunarea zarurilor
                    # pentru ca piesa sa poata fi afisata pe pozitia rezultata prin adunarea zarurilor
                    # trebuie ca macar unul din zaruri sa fie folosit pentru a ajunge pe pozitia respectiva
                # cazul in care pe pozitia posibila exista alte piese
                    if layoutPosition.count() > 0:
                        # verificare daca adversarul are cel putin o piesa pe pozitia posibila 
                            # veificam ca pe pozitia respectica sa existe doar o piesa
                        if layoutPosition.count() == 1:
                            # daca exista doar o piesa, atunci se verifica daca acesta este a adversarului
                            if layoutPosition.itemAt(0).widget().objectName() == f'{oponentTeam}Checker':
                                # daca piesa este a adversarului, atunci se poate muta pe pozitia respectiva
                                    # aici, piesa ghost ar trebui sa inlocuiasca piesa adversarului si
                                    # piesa adversarului ar trebui sa fie aruncata pe gard
                                self.oponentChekerVisibility(visibility = False, numberOfPos = move, oponentTeam = oponentTeam)
                                # lista folosita pentrtu a stica pozitiile de unde au fost aruncate piesele pe gad
                                self.addCheckerToPosition(f'pos{move}', "ghost", useDice, True)
                                self.fencedCheckers.append(move)
                                self.addGhostCheckerToFence(oponentTeam)
                                # piesa adversarului devine din nou vizibila prin apelarea functiei oponentChekerVisibility in functia hover
                        # excluderea pozitiilor unde exista piese ale opentului si sunt mai mult de 1 piese
                        lastChecker = layoutPosition.count() - 1
                        if layoutPosition.itemAt(lastChecker).widget().objectName() not in [f'{oponentTeam}Checker', 'ghostChecker']:
                            # pentru pozitiile 1 12, piesele se vor adauga pe pozitia 0
                            if layoutPosition in self.layouts.buttonPositions:
                                if layoutPosition.itemAt(0).widget().objectName() != 'ghostChecker':
                                    layoutPosition.insertWidget(0, Checkers(team = "ghost", positionName = layoutPosition.objectName(), gameLogic = self, usedDice = useDice))
                            else:
                                # pentru pozitiile 13 24, piesele se vor adauga pe ultima pozitie
                                self.addCheckerToPosition(f'pos{move}', "ghost", useDice)
                    else:
                        # cazul in cere pe pozitia posibila nu exista alte piese
                        self.addCheckerToPosition(f'pos{move}', "ghost", useDice)
                else:
                    # momentul cand zona de scoatere a pieselor devine activa
                    # TODO: De implementat conditica ca doar atunci cand jucatorul are toate piesele in casa acesta sa poate raliza mutari pentru a scoate piesele
                    if self.allCheckersHouse():
                        print(f'Se pot realiza mutari pentru a scoate piese din joc, zarul folosit pentru aceasta mutare: {useDice}')
                        self.usedDiceForOutCheckers = useDice
                        self.highlightOutPosibility(True)

    def canMakeMove(self, fromFence = False) -> bool:
        oponentTeam = "black" if self.teamTurn == "white" else "white"
        possibleMove = []
        realizableMove = False
        positions = []
        if self.dices:
            if fromFence:
                positions = self.layouts.positions[-2:]
            else: 
                positions = self.layouts.positions
            for pos in positions:
                if pos.count() > 0:
                    print(f'aici 1 - {realizableMove} {pos.objectName()}')
                    if realizableMove == False: # daca se gaseste anterior o mutare posibila, realozableMove este True si nu se mai verifica daca mai sunt mutari posibile
                        print(f'aici 2 - {realizableMove}')
                        if pos.itemAt(0).widget().objectName() == f"{self.teamTurn}Checker":
                            posID = self.getPosID(pos.objectName())
                            possibleMove.clear()
                            # crearea listei cu mutari posibile de pe pozitia n
                            if self.teamTurn == "white":
                                for dice in self.getDices():
                                    possibleMove.append(posID + dice)
                                # print('jucator alb')
                            else:
                                for dice in self.getDices():
                                    possibleMove.append(posID - dice)
                                # print('jucator negru')
                            # verificarea fiecarei mutari daca este posibila
                            for move in possibleMove:
                                if move >= 1 and move <= 24:
                                    layoutPosition = getattr(self.layouts, f'pos{move}')
                                    if layoutPosition.count() > 0:
                                        if layoutPosition.count() == 1:
                                            if layoutPosition.itemAt(0).widget().objectName() == f'{oponentTeam}Checker':
                                                realizableMove = True
                                                break
                                        lastChecker = layoutPosition.count() - 1
                                        if layoutPosition.itemAt(lastChecker).widget().objectName() not in [f'{oponentTeam}Checker', 'ghostChecker']:
                                            if layoutPosition in self.layouts.buttonPositions:
                                                if layoutPosition.itemAt(0).widget().objectName() != 'ghostChecker':
                                                    realizableMove = True
                                                    break
                                            else:
                                                realizableMove = True
                                                break
                                    else:
                                        realizableMove = True
                                        break
                else:
                    # TODO: de pus conditie pentru a calcula mutarea doar atunci cand jucatorul are toate piesele in casa
                    if self.allCheckersHouse():
                        realizableMove = True
                        break
        print(f"canMakeMove - Jucatorul {self.teamTurn} poate face mutari: {realizableMove}")
        return realizableMove
    
    def countOutCheckers(self) -> int:
        if self.teamTurn == "white":
            return self.layouts.outWhiteCheckersLayout.count()
        else:
            return self.layouts.outBlackCheckersLayout.count()
        
    def allCheckersHouse(self) -> bool:
        if self.teamTurn == "white":
            for pos in self.layouts.positions:
                if pos not in [self.layouts.pos19, self.layouts.pos20, self.layouts.pos21, self.layouts.pos22, self.layouts.pos23, self.layouts.pos24]:
                    if pos.count() > 0:
                        if pos.itemAt(0).widget().objectName() == "whiteChecker":
                            return False
        if self.teamTurn == "black":
            for pos in self.layouts.positions:
                if pos not in [self.layouts.pos1, self.layouts.pos2, self.layouts.pos3, self.layouts.pos4, self.layouts.pos5, self.layouts.pos6]:
                    if pos.count() > 0:
                        if pos.itemAt(0).widget().objectName() == "blackChecker":
                            return False
        return True

    # TODO: schimba denumirea functiei in ceva mai intuitiv
    def oponentChekerVisibility(self, visibility, numberOfPos, oponentTeam) -> None:
        """Functie care face vizibila/invizibila piesa adversarului.\n
        Folosita la momentul in care pe o posibila pozitie, jucatorul poate face mutare peste adversarul sau.\n
        Conditia este ca adversarul sa aiba doar o piesa pe pozitia respectiva.\n
        Acest lucru arunca piesa adversarului pe gard, iar o piesa ghost inlocuieste piesa adversarului pana la incetarea eventului hover.\n
        cand se readuce piesa 'aruncata' pe gard, inapoi in pozitia initiala prin incetarea eventului hover, daca locatia nu este ocupata de jucatorul in curs\n
        Apelata in functia:
            - showPosibleMove(posName, oponentTeam = "black") din gameLogic.py
            - hover(is_hovered) din checkers.py
            """
        if visibility:
            self.addCheckerToPosition(f'pos{numberOfPos}', oponentTeam)
        else:
            checker = getattr(self.layouts, f"pos{numberOfPos}").itemAt(0).widget()
            checker.deleteLater()

    def deleteGhostCheckers(self, canDeleteGhostCheckers) -> None:
        """Functie care sterge piesele ghost de pe tabla.\n
        Apelata in functiile: 
            - hover(is_hovered) din checkers.py
            - click() din checkers.py
            """
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
        """Folosita pentru a sterge piese reale de pe anumite pozitii in fucntie de parametrul fromPosNumber.\n
        Apelata in functia:
            - click() din checkers.py
        """
        for pos in self.layouts.positions:
            if pos.objectName() == f"pos{fromPosNumber}":
                pos.itemAt(0).widget().deleteLater()

    def deleteDiceFromLayout(self, deleteDice = None, deleteAll = False) -> None:
        """Functie care sterge obiecte zarurilor din self.diceLayout .\n
        Daca parametrul deleteAll = True, atunci se sterg toate obiectele din self.diceLayout.\n
        Daca parametrul deleteDice = int, corespunzator unui zar folosit pentru realizarea mutari, atunci se sterge zarul respectiv din diceLayout.\n
        Apelata in functia:
            - roll(diceLayout) din gameLogic.py
            """
        if deleteAll:
            countDiceObject = self.layouts.diceLayout.count()
            if countDiceObject > 0:
                for index in range(countDiceObject):
                    self.layouts.diceLayout.itemAt(index).widget().deleteLater()
        if deleteDice:
            for index in range(self.layouts.diceLayout.count()):
                diceForDelete = self.layouts.diceLayout.itemAt(index).widget()
                if diceForDelete.objectName() == f"dice{deleteDice}":
                    diceForDelete.deleteLater()
                    break

    def setDefaultPosition(self) -> None:
        """Este apelata pentru a crea piesele la inceputul jocului pe pozitiile default ale jocului.\n
        Apelata in functia middleLayout() din layouts.py dupa crearea layout-urilor pentru pozitiile pieselor."""
        defaulPosition = {"black" : [(self.layouts.pos6, 5), (self.layouts.pos13, 5), (self.layouts.pos8, 3), (self.layouts.pos24, 2)],
                          "white" : [(self.layouts.pos12, 5),(self.layouts.pos19, 5),(self.layouts.pos17, 3),(self.layouts.pos1, 2)]}
        for team, posAndCaunt in defaulPosition.items():
            for position, numberOfPieces in posAndCaunt:
                for i in range(numberOfPieces):
                    position.addWidget(Checkers(team = team, positionName = position.objectName(), gameLogic = self, usedDice = 0))