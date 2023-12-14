from PyQt6.QtWidgets import QPushButton

class Checkers(QPushButton):
    def __init__(self, team):
        super().__init__()
        self.setObjectName(f'{team}Checker')
        self.setFixedSize(60,60)

        # self.clicked.connect(self.test_movePosition)

