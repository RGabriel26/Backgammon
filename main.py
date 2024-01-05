from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QFrame, QSizePolicy
from PyQt6.QtGui import QIcon, QFont
import sys

from gameLogic import *


class UInterface(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BackGammon")
        self.setWindowIcon(QIcon("images/white-checker.png"))
        self.gameLogic = GameLogic()
        self.initGUI()

    def initGUI(self):
        self.width = 1366
        self.height = 768
        # self.setGeometry(0, 0, self.width, self.height)
        # self.showFullScreen()
        self.setFixedSize(self.width, self.height)

        winCenter = self.geometry().center()
        centerX = winCenter.x() - 109
        centerY = winCenter.y() - 125

        # folosit pentru a grupa cele trei containere principala ale ferestrei intr-un mod de afisare orizolntala
        parentLayout = QHBoxLayout()

        # #contaier pentru elementele din stanga
        leftLayoutContainer = self.gameLogic.layouts.leftContainer()
        # conta inerul din mijlocul ferestrei
        middleLayoutContainer = self.gameLogic.layouts.middleLayout()
        # containerul elementelor din stanga
        rightLayoutContainer = self.gameLogic.layouts.rightContainer()
    
        # folosit pentru a aduna    containerele intr un singur loc pentru a putea fi gestionate
        parentLayout.addWidget(leftLayoutContainer, 20)
        parentLayout.addWidget(middleLayoutContainer, 70)   
        parentLayout.addWidget(rightLayoutContainer, 10)

        # centrareas layout ului parinte in centrul ferestrei
        centralWidget = QWidget()  
        centralWidget.setLayout(parentLayout)
        self.setCentralWidget(centralWidget)

############## Info Frame ##############################

        # Adăugarea QFrame-ului pentru centrare
        self.infoFrame = QFrame(self)
        self.infoFrame.setGeometry(centerX, centerY, 350, 250)
        self.infoFrame.setFrameStyle(QFrame.Shape.Box)

        # QLabel cu informații despre joc
        text = """
        Backgammon este un joc unde norocul si skill-ul conteaza. \n
        Jocul se termina cand primul jucator reuseste sa-si scoata toate piesele de pe tabla. \n
        "Multa bafta tuturor!"""
        infoLabel = QLabel(text, objectName = "infoLabel")
        infoLabel.setAlignment(Qt.AlignmentFlag.AlignLeft)
        infoLabel.setFont(QFont("Times", 10, QFont.Weight.Bold))
        infoLabel.setContentsMargins(0, 0, 0, 0)

        # butoane din QFrame
        previeousButton = QPushButton("PREVIOUS", objectName = "previousButton")
        previeousButton.setFixedSize(50,50)

        startButton = QPushButton("START", objectName = "startButton")
        startButton.setFixedSize(50,50)
        startButton.clicked.connect(lambda: self.startButtonAction())

        nextButton = QPushButton("NEXT", objectName = "nextButton")
        nextButton.setFixedSize(50,50)

        # Adăugarea layout-ului pentru GFrame
        infoLayout = QVBoxLayout()
        infoLayout.setContentsMargins(0, 0, 0, 0)

        topFrameContainer = QWidget()
        topFrameContainer.setStyleSheet("background-color: rgba(63, 208, 27, 0.4)")
        buttonFrameContainer = QWidget()
        buttonFrameContainer.setStyleSheet("background-color: rgba(63, 208, 27, 0.4)")

        topFrameContainerLayout = QHBoxLayout()
        topFrameContainerLayout.setContentsMargins(0, 0, 0, 0)
        buttonFrameContainerLayout = QHBoxLayout()
        buttonFrameContainerLayout.setContentsMargins(0, 0, 0, 0)

        topFrameContainerLayout.addWidget(infoLabel)
        buttonFrameContainerLayout.addWidget(previeousButton)
        buttonFrameContainerLayout.addWidget(startButton)
        buttonFrameContainerLayout.addWidget(nextButton)

        topFrameContainer.setLayout(topFrameContainerLayout)
        buttonFrameContainer.setLayout(buttonFrameContainerLayout)

        infoLayout.addWidget(topFrameContainer)
        infoLayout.addWidget(buttonFrameContainer)
    
        self.infoFrame.setLayout(infoLayout)

    def startButtonAction(self):
        self.infoFrame.hide()
        self.gameLogic.setDefaultPosition()
        self.gameLogic.logic()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    with open('style/styleSheet.css', 'r') as file:
        stylesheet = file.read()
    app.setStyleSheet(stylesheet)

    game = UInterface()
    game.show()

    sys.exit(app.exec())