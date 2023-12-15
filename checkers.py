from PyQt6.QtWidgets import QPushButton

class Checkers(QPushButton):
    def __init__(self, team, layout):
        super().__init__()
        self.team = team
        self.layout = layout
        self.setObjectName(f'{team}Checker')
        self.setFixedSize(50,50)
        self.clicked.connect(self.test)

    def test(self):
        print(f"Piesa {self.team} a fost selectata: {self.layout.objectName()}") 


