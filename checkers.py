from PyQt6.QtWidgets import QPushButton

class Checkers(QPushButton):
    def __init__(self, team, parent, x, y):
        super().__init__()
        self.setObjectName(f'{team}Checker')
        self.setFixedSize(60,60)
        self.parent = parent
        self.x = x
        self.y = y

        self.clicked.connect(self.test_movePosition)

    def test_movePosition(self):
        self.move(self.x, self.y)
        print(self.parent.size())