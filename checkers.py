from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import pyqtSignal

class Checkers(QPushButton):
    hovered = pyqtSignal(bool)
    # TODO: Posibil ca aducerea intregului layout aici nu este cea mai eficienta optiune in cazul in care se dareste doar identificarea layout-ului
    # din care face parte obiectul
    # OPTIUNE: Sa vii direct cu numele layout-uli ca un streang sau chiar cu un integer, astfel sa optimizezi cat mai mult resursele
    def __init__(self, team, layout):
        super().__init__()
        self.team = team
        self.layout = layout
        self.setObjectName(f'{team}Checker')
        self.setFixedSize(50,50)
        self.isHoverEnable = True
        
        self.hovered.connect(self.testHover)
        self.clicked.connect(self.testClick)
    
    def enterEvent(self, event):
        self.hovered.emit(True)

    def leaveEvent(self, event):
        self.hovered.emit(False)

    def testHover(self, is_hovered):
        if is_hovered and self.isHoverEnable:
            print(f"Piesa {self.team} a fost selectata prin hover event: {self.layout.objectName()}")

    def testClick(self):
        print(f"Piesa {self.team} a fost selectata prin clicked event: {self.layout.objectName()}")

    def setHover(self, bool) -> None:
        self.isHoverEnable = bool

    def getTeam(self) -> str:
        return self.team



