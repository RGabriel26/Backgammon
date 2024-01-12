from PyQt6.QtWidgets import (QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QGridLayout,
                             QStackedLayout, QLineEdit)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

class BoxInfoWindow():
    """Clasa care creeaza fereastra de la inceputul jocului."""
    def __init__(self, parent, gameLogic):
        super().__init__()
        self.parent = parent
        self.gameLogic = gameLogic
        centerMainWindow = self.parent.geometry().center()
        self.centerX = centerMainWindow.x() - 157
        self.centerY = centerMainWindow.y() - 130

        self.initInfoBox()
        
    def initInfoBox(self):
        """Functia care inglobeaza ferestrele si gestioneaza paginile de informatii."""
        # Adăugarea QFrame-ului in care vor fi adaugate toate elementele ce contin informatiile
        # de la inceputul jocului
        self.infoBox = QWidget(self.parent, objectName = "infoBox")
        self.infoBox.setGeometry(self.centerX, self.centerY, 450, 250)

        # butoane din QFrame
        previeousButton = QPushButton(objectName = "previousButton")
        previeousButton.setFixedSize(100,50)
        previeousButton.clicked.connect(lambda: self.setPageBox("previous"))

        self.startButton = QPushButton("START", objectName = "startButton")
        self.startButton.setFixedSize(100,50)
        self.startButton.clicked.connect(lambda: self.startButtonAction())
        self.startButton.setFont(QFont("Times", 12, QFont.Weight.Bold.value))

        nextButton = QPushButton(objectName = "nextButton")
        nextButton.setFixedSize(100,50)
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
        Bun venit in Backgammon!"""
        info = QLabel(text)
        info.setAlignment(Qt.AlignmentFlag.AlignCenter)
        info.setWordWrap(True)
        info.setFont(QFont("Times", 10, QFont.Weight.Bold))
        info.setContentsMargins(0, 0, 0, 0)

        # Butoane pentru selectia tipului de joc
        # adica joc 1 vs 1 sau joc 1 vs PC
        # defaul va fi selectat jocul 1v1

        self.button1v1 = QPushButton("1 vs 1", objectName = "button1v1")
        self.button1v1.setFixedSize(100,50)
        self.button1v1.clicked.connect(lambda: self.setGameType("1v1"))
        self.button1v1.setFont(QFont("Times", 12, QFont.Weight.Bold.value))
        self.button1v1.setEnabled(False)

        self.button1vPC = QPushButton("1 vs PC", objectName = "button1vPC")
        self.button1vPC.setFixedSize(100,50)
        self.button1vPC.clicked.connect(lambda: self.setGameType("1vPC"))
        self.button1vPC.setFont(QFont("Times", 12, QFont.Weight.Bold.value))
        self.button1vPC.setEnabled(True)


        textPlayer1 = QLabel("Player W: ")
        textPlayer1.setAlignment(Qt.AlignmentFlag.AlignLeft)
        textPlayer1.setFont(QFont("Times", 10, QFont.Weight.Bold))
        textPlayer1.setContentsMargins(0, 0, 0, 0)

        textPlayer2 = QLabel("Player B: ")
        textPlayer2.setAlignment(Qt.AlignmentFlag.AlignLeft)
        textPlayer2.setFont(QFont("Times", 10, QFont.Weight.Bold))
        textPlayer2.setContentsMargins(0, 0, 0, 0)

        self.inputPlayer1 = QLineEdit(objectName = "inputPlayerNickname")
        self.inputPlayer1.setPlaceholderText("Nickname-ul jucatorului White...")
        self.inputPlayer1.setFixedSize(350, 20)
        self.inputPlayer1.setMaxLength(15)
        self.inputPlayer1.setStyleSheet("border: none; margin: 0px; background-color: rgba(0,0,0,0); color: black")
        self.inputPlayer1.setFont(QFont("Times", 10, QFont.Weight.Bold))
        self.inputPlayer1.setContentsMargins(0, 0, 0, 0)


        self.inputPlayer2 = QLineEdit(objectName = "inputPlayerNickname")
        self.inputPlayer2.setPlaceholderText("Nickname-ul jucatorului Black...")
        self.inputPlayer2.setMaxLength(10)
        self.inputPlayer2.setStyleSheet("border: none; padding: 0px; margin: 0px; background-color: rgba(0,0,0,0); color: black")
        self.inputPlayer2.setFixedSize(350, 20)
        self.inputPlayer2.setFont(QFont("Times", 10, QFont.Weight.Bold))
        self.inputPlayer2.setContentsMargins(0, 0, 0, 0)

        layoutSetSelectGame = QGridLayout()
        layoutSetSelectGame.setContentsMargins(0, 0, 0, 0)
        layoutSetSelectGame.addWidget(self.button1v1, 0, 0)
        layoutSetSelectGame.addWidget(self.button1vPC, 0, 1)
        layoutSetSelectGame.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layoutSetSelectGame.setSpacing(50)

        layoutSetSelectGameContainer = QWidget()
        layoutSetSelectGameContainer.setLayout(layoutSetSelectGame)

        layout.addWidget(info, 0, 0, 1, 2)
        layout.addWidget(layoutSetSelectGameContainer, 1, 0, 1, 2)
        layout.addWidget(textPlayer1, 2, 0)
        layout.addWidget(self.inputPlayer1, 2, 1)
        layout.addWidget(textPlayer2, 3, 0)
        layout.addWidget(self.inputPlayer2, 3, 1)

        container.setLayout(layout)

        self.startButton.show()

        return container
    
    def infoGame(self) -> QLabel:
        """Functie utilizata pentru a crea un QLabel cu informatii despre joc.\n
        QLabel ce va fi adaugat in QFrame printr-un layout de tip QStackedLayout."""
        text = """
        Informatii despre joc:\n
        - Backgammon este un joc unde norocul unde si skill-ul conteaza.
        - Ai posibilitatea atat de a te juca cu un prieten, cat si cu calculatorul.
        - Jocul se termina cand primul jucator reuseste sa-si scoata toate piesele de pe tabla.
        - Multa bafta tuturor! Fie ca cel mai bun sa castige!"""
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
        - Fiecare jucator TREBUIE sa-si respecte randul si sa nu-si saboteze adversarul.
         """
        rules.setText(reguli)
        rules.setAlignment(Qt.AlignmentFlag.AlignLeft)
        rules.setWordWrap(True)
        rules.setFont(QFont("Times", 10, QFont.Weight.Bold))

        return rules

    def startButtonAction(self):
        """Functie utilizata la apasarea butonului de start.\n"""
        print("Start game!")
        self.infoBox.deleteLater()
        self.gameLogic.setDefaultPosition()
        self.gameLogic.logic()

        if self.inputPlayer1.text() != "":
            self.gameLogic.layouts.labelPlayerWhite.setText(self.inputPlayer1.text())
            self.gameLogic.nicknamePlayerWhite = self.inputPlayer1.text()

        if self.inputPlayer2.text() != "":
            self.gameLogic.layouts.labelPlayerBlack.setText(self.inputPlayer2.text())
            self.gameLogic.nicknamePlayerBlack = self.inputPlayer2.text()

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

    def setGameType(self, gameType) -> None:
        """Functia care seteaza tipul de joc."""
        if gameType == "1v1":
            # a fost selectat jocul 1 vs 1
            self.button1v1.setStyleSheet("image: url(images/activeButton.png); background-color: rgba(0, 0, 0, 0); outline: none; color: black;")
            self.button1vPC.setStyleSheet("image: url(images/inactiveButton.png); background-color: rgba(0, 0, 0, 0); outline: none; color: black;")
            self.gameLogic.setGameType("1v1")
            self.button1v1.setEnabled(False)
            self.button1vPC.setEnabled(True)
            self.inputPlayer1.setEnabled(True)
            self.inputPlayer1.setText("")
        elif gameType == "1vPC":
            # a fost selectat jocul 1 vs PC
            self.button1v1.setStyleSheet("image: url(images/inactiveButton.png); background-color: rgba(0, 0, 0, 0); outline: none; color: black;")
            self.button1vPC.setStyleSheet("image: url(images/activeButton.png); background-color: rgba(0, 0, 0, 0); outline: none; color: black;")
            self.gameLogic.setGameType("1vPC")
            self.button1v1.setEnabled(True)
            self.button1vPC.setEnabled(False)
            self.inputPlayer1.setText("Computer")
            self.inputPlayer1.setEnabled(False)