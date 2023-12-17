from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QLabel, QWidget, QHBoxLayout, QGridLayout, QLayout, QSpacerItem
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import QPoint, QSize, Qt
from PyQt6 import QtWidgets
import sys

from functions import *
from gameLogic import *
from checkers import *
from layouts import *


class UInterface(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BackGammon")
        self.setWindowIcon(QIcon("images/white-checker.png"))
        self.layouts = UILayouts()
        self.gameLogic = GameLogic()
        self.initGUI()

    def initGUI(self):
        self.width = 1366
        self.height = 768
        # self.setGeometry(0, 0, self.width, self.height)
        # self.showFullScreen()
        self.setFixedSize(self.width, self.height)

        # folosit pentru a grupa cele trei containere principala ale ferestrei intr-un mod de afisare orizolntala
        parentLayout = QHBoxLayout()

        # #contaier pentru elementele din stanga
        leftLayoutContainer = self.layouts.leftContainer()

        # containerul din mijlocul ferestrei
        middleLayoutContainer = self.layouts.middleLayout()
        
        # containerul elementelor din stanga
        rightLayoutContainer = self.layouts.rightContainer(self.gameLogic)

        # folosit pentru a aduna containerele intr un singur loc pentru a putea fi gestionate
        parentLayout.addWidget(leftLayoutContainer, 20)
        parentLayout.addWidget(middleLayoutContainer, 70)
        parentLayout.addWidget(rightLayoutContainer, 10)

        # centrarea layout ului parinte in centrul ferestrei
        centralWidget = QWidget()  
        centralWidget.setLayout(parentLayout)
        self.setCentralWidget(centralWidget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    with open('style/styleSheet.css', 'r') as file:
        stylesheet = file.read()
    app.setStyleSheet(stylesheet)

    game = UInterface()
    game.show()

    sys.exit(app.exec())