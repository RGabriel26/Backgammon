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
    def __init__(self, team, positionName, gameLogic):
        super().__init__()
        self.team = team
        self.positionName = positionName
        self.gameLogic = gameLogic
        self.setObjectName(f'{team}Checker')
        self.setFixedSize(50,50)
        self.isHoverEnable = True
        
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
        if is_hovered and self.isHoverEnable:
            # cand piesa este in focusul mouse-ului se apeleaza functia care afiseaza 
            # pe pozitiile posibile dictate de ce zar a picat si adauga piesele gost
            if self.team == "white":
                self.gameLogic.showPossibleMove(posName = self.positionName, oponentTeam = "black")
            else:
                self.gameLogic.showPossibleMove(posName = self.positionName, oponentTeam = "white")

            # Doar de test
            print(f"Piesa {self.team} a fost selectata prin hover event: {self.positionName}")
        else:
            # cand piesa nu mai este in focusul mouse-ului
            # se sterg piesele gost 
            self.gameLogic.deleteGhostCheckers()
            # si se reafiseaza piesele adversarului daca acestea au fost aruncate pe gard 
            # lucru salvat in instanta gameLogic ca o lista nu numarul pozitiei de unde a fost scoasa piesa
            if len(self.gameLogic.fencedCheckers) > 0:
                while len(self.gameLogic.fencedCheckers) > 0:
                    position = self.gameLogic.fencedCheckers.pop()
                    self.gameLogic.oponentChekerVisibility(True, position)

    def click(self):
        # TODO: Trebuie creata o functia care sa verifica ca jucatorul are toate piesele in casa
        # pentru ca sa poate scoate piesele din casa, astfel astigand jocul
        # TODO: Trebuie apelata finctia care la momentul selectarii pozitiei, piesa adversarului sa fie aruncata pe gard
        
        # Doar de test
        print(f"Piesa {self.team} a fost selectata prin clicked event: {self.positionName}")



