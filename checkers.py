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
        if not self.gameLogic.isGlobalCheckerInteractiv:
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
                    # se sterg piesele gost 
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
        # Eventul de click pe o piesa va apela functia .showPossibleMove() din gameLogic.py
        # care va afisa jucatorului pozitiile disponibile in functie de zarul pe care l-a aruncat si va face in asa fel incat piesele
        # ghost sa ramana active pana la momentul selectarii uneia dintre ele

        # In momentul selectarii unei piese ghost, aceasta va fi inlocuita cu o piesa reala a jjucatorului, in fucntie de culoarea jucatorului
        # Totodata, va fi eliminata o piesa a jucatorului de pe pozitia anterioara de pe care s-a simulat mutarea
        # Dupa realizarea selectarea unei piese ghost pentru a simula mutarea, se va verifica care dintre posibilitatile oferite
        # de zaruri a fost folosita (primul zar, al doilea zar sau ambele zaruri) si se va realiza o eliminare din lista de zarur
        # deci ar trebui sa vii cu acea lista aici pentru a face verificarea.

        # Problema: Daca nu se pot face mutari cu zarurile disponibile, jocul trebuie sa si continue curusl cu urmatorul jucator
        # Ar trebui o functie care sa verifice toate pozitiile unde sunt piesele jucatorului actual si sa contorizeze numarul de mutari
        # pozibile pe care le poate face cu zarurile disponibile, iar daca nu se poate face nicio mutare, jocul sa treaca la urmatorul jucator

        # Pasi pe scurt: 
        # - Activarea eventului prin click pe piesa
        # - Afisarea pieselor ghost pe pozitiile posibile prin functia deja creata .showPossibleMove()
        # - Selectarea unei piese ghost prin click care reprezinta locul unde jucatorul doreste sa mute piesa selectata
        # - Inlocuirea piesei ghost cu o piesa reala a jucatorului
        # - Eliminarea piesei din pozitia anterioara
        # - Verificarea daca jucatorul mai poate realiza mutari cu zarurile disponibile
                    # Aici este urila functia care contorizeaza numarul de mutari posibile ale jucatorului cu zarurile disponibile
                    # pentru piesele sale de pe toate pozitiile unde acesta are piese, daca se obtin 0 mutari posibile, actiunea jocului trece la 
                    # urmatorul jucator
        # - Daca nu se mai pot face mutari, jocul trece la urmatorul jucator

        # se asteapta apasarea butonului de start pentru a indica inceperea jocului, implicit si interactiunea cu piesele
        if not self.gameLogic.isGlobalCheckerInteractiv:
            return
        # Conditie pentri a dezactiva hoverul pieselor albe
        if self.team == "white" and self.gameLogic.isWhiteCheckerEnable == False:
            return
        # Conditie pentri a dezactiva hoverul pieselor negre
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
                elif anteriorPosition == 25:
                    # piesa selectata de pe gard este a jucatorului black
                    self.gameLogic.layouts.fenceBlackCheckersLayout.itemAt(0).widget().deleteLater()
                else:
                    self.gameLogic.deleteCheckerFromPosition(anteriorPosition)

                # se verifica daca piesa gost pe care s-a apasat a inlocuit sau nu o piesa a adversarului
                # daca da, se va elimina indexul pozititiei din lista de piese gost de pe gard
                # astfel, nu se va mai recrea piesa adversarului pe pozitia anterioara
                if self.replaceCheckers:
                    self.gameLogic.fencedCheckers.remove(self.gameLogic.getPosID(self.positionName))
                    # TODO: creaza probleme
                    self.gameLogic.addCheckerToFence('black' if self.gameLogic.teamTurn == 'white' else 'white')

                # stergerea zarurului folosit pentru realizarea mutarii
                self.gameLogic.dices.remove(self.usedDice)
                # stergerea zarului folosit din diceLayout
                self.gameLogic.deleteDiceFromLayout(deleteDice = self.usedDice)
                # dupa plasarea unei piese reale, se va reactiva eventul de hover pentru a putea fi afisate piesele gost
                self.gameLogic.isGlobalHoverEnable = True
                self.gameLogic.canDeleteGhostCheckers = True
                self.gameLogic.clickCounter = 0
            
                # RESTRICTII:
                # Verificare daca jucatorul poate realiza mutari cu zarurile primite
                # Tot aici este tratat si cazul cand jucatorul a realizat mutari cu toate zarurile primite

                # countFenceWhite = self.gameLogic.layouts.fenceWhiteCheckersLayout.count()
                # countFenceBlack = self.gameLogic.layouts.fenceBlackCheckersLayout.count()
                # condition = (countFenceWhite > 0 and self.gameLogic.teamTurn == "white") or (countFenceBlack > 0 and self.gameLogic.teamTurn == "black")

                # se pot realiza mutari cu zarurile, de pe orice pozitie
                if self.gameLogic.canMakeMove() == False:
                    print('Nu se pot face mutari de pe tabla!')
                    self.gameLogic.dices.clear()
                    self.gameLogic.deleteDiceFromLayout(deleteAll = True)
                    self.gameLogic.isGlobalCheckerInteractiv = False
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

        # salvarea pozitiei ultimei piese selectate
        self.gameLogic.lastClickedChecker = self.positionName

        # RESTRICTII:
        # Restrictia pieselor pe gard care face ca celelalte piese sa fie indisponibile pana cand toate piesele de pe gard sunt mutate inapoi in joc:
        if anteriorPosition == 0 or anteriorPosition == 25:
            # folosim QTimer pentru a astepta stergerea completa a pieselor de pe gard
            QTimer.singleShot(0, lambda: self.gameLogic.restrictionFence(anteriorPosition))

        print('click - sfarsit click event')

        # Piesele vor fi mutate pana dupa posibilitati pana in momentul in care toate piesele vor fi in casa
        # Dupa aceasta se va realiza eliminarea pieselor din casa, si totodata adaugarea de elemente in
        # OutCheckersLayout pentru a informa jucatorii cu privire la progresul jocului
        # IMPORTANT: Jocul se va incheia cand unul din jucatori aduna 15 piese in OutCheckersLayout

        # TODO: Trebuie creata o functia care sa verifica ca jucatorul are toate piesele in casa pentru ca sa poate scoate piesele din casa, astfel astigand jocul

        # Doar de test
        # print(f"Zarul folosit pentru mutarea piesei: {self.usedDice}")
        # print(f"Piesa {self.team} a fost selectata prin clicked event: {self.positionName}")

    def test(self):
       self.checkersFromFence = self.gameLogic.countFenceCheckers()


