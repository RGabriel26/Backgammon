from PyQt6.QtWidgets import QPushButton, QFrame, QLabel, QVBoxLayout, QHBoxLayout, QWidget
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont 

class MessageWindow(QFrame):
    def __init__(self, parent, gameLogic, centerCoordinates):
        self.parent = parent
        self.gameLogic = gameLogic
        centerX = centerCoordinates.x() - 109
        centerY = centerCoordinates.y() - 135

         # Adăugarea QFrame-ului pentru centrare
        self.infoFrame = QFrame(self.parent)
        self.infoFrame.setGeometry(centerX, centerY, 350, 250)
        self.infoFrame.setFrameStyle(QFrame.Shape.Box)

        # TODO: De adaugat text imput urile, care vor deveni vizibile in functie de pagina pe care esti in qframe
        # sau cu layouturi diferite de tip QStackedLayout pentru contentul din topFrameContainer
        # iar butoanele de next si previous doar vor seta ce layout este vizibil

        # primul layout din QFrame
        # cel in care se vor seta numele jucatorilor, daca acestia nu vor fi setate
        # se vor seta automat cu Player1 si Player2
        # tot aici va fi un buton de check pentru a activa posibilitatea de a juca cu CALCULATORUL
        # butonul de stat devine vizibil dupa ce sunt setate numele jucatorilor

        # al doilea layout din QFrame
        # aici vor fi cateva informatii despre joc

        # al treilea layout din QFrame
        # aici vorm fi trecute regulile jocului

        # TODO: Recomandare: 
        # - folosirea unor dimensiuni ale ferestrei mai mari


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
        startButton.show()

        nextButton = QPushButton("NEXT", objectName = "nextButton")
        nextButton.setFixedSize(50,50)

        # Adăugarea layout-ului pentru GFrame
        infoLayout = QVBoxLayout()
        infoLayout.setContentsMargins(0, 0, 0, 0)

        topFrameContainer = QWidget(objectName = "topFrameContainer")

        buttomFrameContainer = QWidget(objectName = "buttomFrameContainer")

        topFrameContainerLayout = QHBoxLayout()
        topFrameContainerLayout.setContentsMargins(0, 0, 0, 0)
        buttomFrameContainerLayout = QHBoxLayout()
        buttomFrameContainerLayout.setContentsMargins(0, 0, 0, 0)

        topFrameContainerLayout.addWidget(infoLabel)
        buttomFrameContainerLayout.addWidget(previeousButton)
        buttomFrameContainerLayout.addWidget(startButton)
        buttomFrameContainerLayout.addWidget(nextButton)

        topFrameContainer.setLayout(topFrameContainerLayout)
        buttomFrameContainer.setLayout(buttomFrameContainerLayout)

        infoLayout.addWidget(topFrameContainer, 90)
        infoLayout.addWidget(buttomFrameContainer, 10)
    
        self.infoFrame.setLayout(infoLayout)

    def startButtonAction(self):
        self.infoFrame.hide()
        self.gameLogic.setDefaultPosition()
        self.gameLogic.logic()