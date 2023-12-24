from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import pyqtSignal

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
        # - piesa este una ghost, sourceCheckers = 1, 2, 3
            # - 1 pentru primul zar
            # - 2 pentru al doilea zar
            # - 3 pentru ambele zaruri
    def __init__(self, team, positionName, gameLogic, sourceCheckers = 0):
        super().__init__()
        self.team = team
        self.positionName = positionName
        self.gameLogic = gameLogic
        self.setObjectName(f'{team}Checker')
        self.setFixedSize(50,50)
        self.isHoverEnable = True
        self.canDeleteGhostCheckers = True
        self.sourceCheckers = sourceCheckers

        self.hovered.connect(self.hover)
        self.clicked.connect(self.click)

    # functii setter si getter
    def getTeam(self) -> str:
        return self.team
    
    def setHover(self, bool) -> None:
        self.isHoverEnable = bool
    
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
        if not self.gameLogic.isGlobalCheckerInteractiv:
            # se asteapta apasarea butonului de start pentru a indica inceperea jocului, implicit si interactiunea cu piesele
            return
        if self.gameLogic.isGlobalHoverEnable and self.team not in ['ghostFenceWhite', 'ghostFenceBlack']:
            if is_hovered and self.isHoverEnable and self.team != 'ghost':
                # cand piesa este in focusul mouse-ului se apeleaza functia care afiseaza 
                # pe pozitiile posibile dictate de ce zar a picat si adauga piesele gost
                if self.team == "white":
                    self.gameLogic.showPossibleMove(posName = self.positionName, oponentTeam = "black")
                else:
                    self.gameLogic.showPossibleMove(posName = self.positionName, oponentTeam = "white")

                # Doar de test
                print(f"Piesa {self.team} a fost selectata prin hover event: {self.positionName}")
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
                            self.gameLogic.oponentChekerVisibility(True, position)

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

        if not self.gameLogic.isGlobalCheckerInteractiv:
            # se asteapta apasarea butonului de start pentru a indica inceperea jocului, implicit si interactiunea cu piesele
            return

        # Excluderea pieselor ghost de pe gard
        if self.team not in ['ghostFenceWhite', 'ghostFenceBlack']:
            # Event de click pentru piesele ghost
            if self.team == "ghost":
                # Aici trebuie sa se inlocuiasca piesa ghost pe care s-a dat click cu o piesa a jucatorului curent
                # Iar de pe pozitia de unde s-a facut anterior click pe o piesa reala, sa se elimine piesa
            

                
                print(f'Zarul folosit pentru acest checkers ghost: {self.sourceCheckers}')
                

            
            # Event de click pentru piesele reale ale jucatorilo
            if self.team != "ghost":
                # TODO: Este o problema, ar trebui evitat spamul inutil de click pe pise deoarece poate influenta eventul click datorita incrementarii variabilei self.gameLogic.clickCounter
                oponentTeam = "black" if self.team == "white" else "white"
                self.gameLogic.showPossibleMove(posName = self.positionName, oponentTeam = oponentTeam) 

                if self.gameLogic.clickCounter % 2 != 0:
                    self.gameLogic.isGlobalHoverEnable = True
                    self.gameLogic.canDeleteGhostCheckers = True
                    self.gameLogic.deleteGhostCheckers(True)
                else:
                    self.gameLogic.isGlobalHoverEnable = False
                    self.gameLogic.canDeleteGhostCheckers = False
                
                print(f'counter click: {self.gameLogic.clickCounter}')

                self.gameLogic.clickCounter += 1

    
        # Trebuie apelata functia logic din gameLogic, pentru a gestiona logica jocului acolo

        # Piesele vor fi mutate pana dupa posibilitati pana in momentul in care toate piesele vor fi in casa
        # Dupa aceasta se va realiza eliminarea pieselor din casa, si totodata adaugarea de elemente in
        # OutCheckersLayout pentru a informa jucatorii cu privire la progresul jocului
        # IMPORTANT: Jocul se va incheia cand unul din jucatori aduna 15 piese in OutCheckersLayout



        # TODO: Trebuie creata o functia care sa verifica ca jucatorul are toate piesele in casa pentru ca sa poate scoate piesele din casa, astfel astigand jocul
        # TODO: Trebuie apelata finctia care la momentul selectarii pozitiei, piesa adversarului sa fie aruncata pe gard

        # Doar de test
        print(f"Piesa {self.team} a fost selectata prin clicked event: {self.positionName}")



