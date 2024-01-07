from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon
import sys

from gameLogic import *
from boxInfoWindow import *
from messageWindow import *


class UInterface(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BackGammon")
        self.setWindowIcon(QIcon("images/white-checker.png"))
        self.gameLogic = GameLogic(self)
        self.initGUI()

    def initGUI(self):
        self.width = 1366
        self.height = 768
        # self.setGeometry(0, 0, self.width, self.height)
        # self.showFullScreen()
        self.setFixedSize(self.width, self.height)
        # creat pentru a stoca coordonatele centru ferestrei
        winCenter = self.geometry().center()

        # folosit pentru a grupa cele trei containere principala ale ferestrei intr-un mod de afisare orizolntala
        parentLayout = QHBoxLayout()

        # #contaier pentru elementele din stanga
        leftLayoutContainer = self.gameLogic.layouts.leftContainer()
        # conta inerul din mijlocul ferestrei
        middleLayoutContainer = self.gameLogic.layouts.middleLayout()
        # containerul elementelor din stanga
        rightLayoutContainer = self.gameLogic.layouts.rightContainer()
    
        # folosit pentru a aduna containerele intr un singur loc pentru a putea fi gestionate
        parentLayout.addWidget(leftLayoutContainer, 20)
        parentLayout.addWidget(middleLayoutContainer, 70)   
        parentLayout.addWidget(rightLayoutContainer, 10)

        # centrareas layout ului parinte in centrul ferestrei
        centralWidget = QWidget()  
        centralWidget.setLayout(parentLayout)
        self.setCentralWidget(centralWidget)

        # Initializarea ferestrei de informatii de la inceputul jocului
        infoWindow = BoxInfoWindow(self, self.gameLogic)


        # TODO: Task: Creaza ca in cazulanterior, o clasa care sa ofere ferestre cu informatii pe parcursul jocului:
        # - mesaj cand jucatorul nu poate muta cu zarurile date
        # - mesaj cand jucatorul a castigat

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    with open('style/styleSheet.css', 'r') as file:
        stylesheet = file.read()
    app.setStyleSheet(stylesheet)

    game = UInterface()
    game.show()

    sys.exit(app.exec())