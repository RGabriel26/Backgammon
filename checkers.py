from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import pyqtSignal

class Checkers(QPushButton):
    hovered = pyqtSignal(bool)
    # TODO: Posibil ca aducerea intregului layout aici nu este cea mai eficienta optiune in cazul in care se dareste doar identificarea layout-ului
    # din care face parte obiectul
    # OPTIUNE: Sa vii direct cu numele layout-uli ca un streang sau chiar cu un integer, astfel sa optimizezi cat mai mult resursele
    def __init__(self, team, parentLayout, gameLogic):
        super().__init__()
        self.team = team
        self.parentLayout = parentLayout
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
        if is_hovered and self.isHoverEnable:
            self.gameLogic.showPosibleMove(self.parentLayout.objectName())
            print(f"Piesa {self.team} a fost selectata prin hover event: {self.parentLayout.objectName()}")
        else:
            self.gameLogic.deleteGostCheckers()
            # TODO: Trebuie readaugata piesa de pe pozitia de unde a fost mutata
                # de cautat o solutie de a salva pozitia de unde a fost mutata piesa
            self.gameLogic.oponentChekerVisibility(True, 21)

    def click(self):
        print(f"Piesa {self.team} a fost selectata prin clicked event: {self.parentLayout.objectName()}")



