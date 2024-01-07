from PyQt6.QtWidgets import QPushButton, QFrame, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QGridLayout, QStackedLayout, QLineEdit, QMainWindow
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont 

class BoxInfoWindow():
    def __init__(self, parent, gameLogic):
        super().__init__()
        self.parent = parent
        self.gameLogic = gameLogic
        centerMainWindow = self.parent.geometry().center()
        self.centerX = centerMainWindow.x() - 157
        self.centerY = centerMainWindow.y() - 135

        self.initInfoBox()
        
    def initInfoBox(self):
        # Adăugarea QFrame-ului in care vor fi adaugate toate elementele ce contin informatiile
        # de la inceputul jocului
        self.infoBox = QFrame(self.parent, objectName = "infoBox")
        self.infoBox.setGeometry(self.centerX, self.centerY, 450, 250)
        # self.infoBox.setFixedSize(450, 250)        
        # self.infoBox.setFrameStyle(QFrame.Shape.Box)

        # butoane din QFrame
        previeousButton = QPushButton("PREVIOUS", objectName = "previousButton")
        previeousButton.setFixedSize(150,50)
        previeousButton.clicked.connect(lambda: self.setPageBox("previous"))

        self.startButton = QPushButton("START", objectName = "startButton")
        self.startButton.setFixedSize(150,50)
        self.startButton.clicked.connect(lambda: self.startButtonAction())
        self.startButton.hide

        nextButton = QPushButton("NEXT", objectName = "nextButton")
        nextButton.setFixedSize(150,50)
        nextButton.clicked.connect(lambda: self.setPageBox("next"))

        # Adăugarea layout-ului pentru QFrame
        boxLayout = QVBoxLayout()
        boxLayout.setContentsMargins(5,5,5,5)

        topBoxContainer = QWidget(objectName = "topFrameContainer")

        buttomBoxContainer = QWidget(objectName = "buttomFrameContainer")

        self.topBoxContainerLayout = QStackedLayout()
        self.topBoxContainerLayout.setContentsMargins(0, 0, 0, 0)
        buttomBoxContainerLayout = QHBoxLayout()
        buttomBoxContainerLayout.setContentsMargins(0, 0, 0, 0)

        self.topBoxContainerLayout.addWidget(self.setNicknames())
        self.topBoxContainerLayout.addWidget(self.infoGame())
        self.topBoxContainerLayout.addWidget(self.rulesGame())

        buttomBoxContainerLayout.addWidget(previeousButton)
        buttomBoxContainerLayout.addWidget(self.startButton)
        buttomBoxContainerLayout.addWidget(nextButton)

        topBoxContainer.setLayout(self.topBoxContainerLayout)
        buttomBoxContainer.setLayout(buttomBoxContainerLayout)

        boxLayout.addWidget(topBoxContainer, 90)
        boxLayout.addWidget(buttomBoxContainer, 10)
    
        self.infoBox.setLayout(boxLayout)
    
    def setNicknames(self):
        """Functie utilizata pentru a crea un QWidget cu doua QLineEdit-uri pentru a seta numele jucatorilor.\n
        QWidget ce va fi adaugat in QFrame printr-un layout de tip QStackedLayout."""
        container = QWidget()

        layout = QGridLayout()
        
        text = """
        Bun venit in Backgammon!\n
        Pentru inceput, jucatorii sunt rugati sa-si inregistreze numele de joc."""
        info = QLabel(text)
        info.setAlignment(Qt.AlignmentFlag.AlignCenter)
        info.setWordWrap(True)
        info.setFont(QFont("Times", 10, QFont.Weight.Bold))
        info.setContentsMargins(0, 0, 0, 0)

        textPlayer1 = QLabel("Player W: ")
        textPlayer1.setAlignment(Qt.AlignmentFlag.AlignLeft)
        textPlayer1.setFont(QFont("Times", 10, QFont.Weight.Bold))
        textPlayer1.setContentsMargins(0, 0, 0, 0)

        textPlayer2 = QLabel("Player B: ")
        textPlayer2.setAlignment(Qt.AlignmentFlag.AlignLeft)
        textPlayer2.setFont(QFont("Times", 10, QFont.Weight.Bold))
        textPlayer2.setContentsMargins(0, 0, 0, 0)

        self.inputPlayer1 = QLineEdit()
        self.inputPlayer1.setPlaceholderText("Nickname-ul jucatorului White...")
        self.inputPlayer1.setMaxLength(15)
        self.inputPlayer1.setStyleSheet("border: none; background: none; padding: 0px; margin: 0px; background-color: rgba(0,0,0,0)")


        self.inputPlayer2 = QLineEdit()
        self.inputPlayer2.setPlaceholderText("Nickname-ul jucatorului Black...")
        self.inputPlayer2.setMaxLength(10)
        self.inputPlayer2.setStyleSheet("border: none; background: none; padding: 0px; margin: 0px; background-color: rgba(0,0,0,0)")

        layout.addWidget(info, 0, 0, 1, 2)
        layout.addWidget(textPlayer1, 1, 0)
        layout.addWidget(self.inputPlayer1, 1, 1)
        layout.addWidget(textPlayer2, 2, 0)
        layout.addWidget(self.inputPlayer2, 2, 1)

        container.setLayout(layout)

        self.startButton.show()

        return container
    
    def infoGame(self) -> QLabel:
        """Functie utilizata pentru a crea un QLabel cu informatii despre joc.\n
        QLabel ce va fi adaugat in QFrame printr-un layout de tip QStackedLayout."""
        text = """
        Backgammon este un joc unde norocul unde si skill-ul conteaza.
        Jocul se termina cand primul jucator reuseste sa-si scoata toate piesele de pe tabla.
        Multa bafta tuturor!"""
        infoLabel = QLabel(text, objectName = "infoLabel")
        infoLabel.setAlignment(Qt.AlignmentFlag.AlignLeft)
        infoLabel.setWordWrap(True)
        infoLabel.setFont(QFont("Times", 10, QFont.Weight.Bold))
        infoLabel.setContentsMargins(0, 0, 0, 0)

        return infoLabel
    
    def rulesGame(self) -> QLabel:
        """Functie utilizata pentru a crea un QLabel cu regulile jocului.\n
        QLabel ce va fi adaugat in QFrame printr-un layout de tip QStackedLayout."""
        rules = QLabel()
        reguli = """
        Reguli si restrictii:\n
        - Majoritatea restrictiilor clasice ale jocului sunt restrictionate de catre joc.
        - Doar de regulile bunului simt trebuie sa tina cont jucatorii. 
        - Dupa terminarea jocului, fereastra trebuie redeschisa pentru inca un joc nou.
         """
        rules.setText(reguli)
        rules.setAlignment(Qt.AlignmentFlag.AlignLeft)
        rules.setWordWrap(True)
        rules.setFont(QFont("Times", 10, QFont.Weight.Bold))

        return rules

    def startButtonAction(self):
        """Functie utilizata la apasarea butonului de start.\n"""
        print("Start game!")
        # TODO: De catat o modalitate de a sterge cu totutl Qframe-ul dupa apasarea butonului de start
        self.infoBox.hide()
        self.gameLogic.setDefaultPosition()
        self.gameLogic.logic()

        if self.inputPlayer1.text() != "":
            self.gameLogic.layouts.labelPlayerWhite.setText(self.inputPlayer1.text())

        if self.inputPlayer2.text() != "":
            self.gameLogic.layouts.labelPlayerBlack.setText(self.inputPlayer2.text())

    def setPageBox(self, direction) -> None: 
        """Functia care schimba paginile din QFrame-ul destinat informatiilor de la inceputul jocului.\n
        Aici jucatori pot citi regulile jocului sau sa isi seteze nickname-urile de joc, dar si sa citeasca cateva informatii depre joc."""
        numberOfPages = self.topBoxContainerLayout.count()
        curentPage = self.topBoxContainerLayout.currentIndex()
        if direction == "previous":
            if curentPage == 0:
                page =  numberOfPages- 1
            else:
                page = curentPage - 1
        elif direction == "next":
            if curentPage == 2:
                page = 0
            else:
                page = curentPage + 1

        self.topBoxContainerLayout.setCurrentIndex(page)