from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QPixmap
from random import randint

from layouts import *

import time

class GameLogic():
    def __init__(self):
        print("initializare gameLogic...")
        # folosit pentru a stoca zarurile generate in functia roll din RollFunctionalities
        self.dices = []
        self.layouts = UILayouts(self)
    
    def saveDices(self,dices) -> None:
        self.dices = dices
        # doar de test pentru a verifica daca se salveaza corect
        print(f"Au picat zarurile {self.getDices()}")

    def createDiceObject(self, urlImage) -> QLabel:
        pixmap = QPixmap(urlImage)
        dice = QLabel()
        dice.setPixmap(pixmap)
        dice.setFixedSize(70,70)
        dice.setScaledContents(True)
        return dice

    def getDices(self) -> list:
        print(f'gameLodic dices: {self.dices}')
        return self.dices

    def roll(self, diceLayout):
        dices = [0, 0]
        for index in range(2):
            getDice = randint(1,6)
            dices[index] = getDice
            # stergerea zarului alfat in gridul diceLayout de pe pozitia 0 index pentru a nu se suprapune
            # .itemAtPosition returneaza un QLayoutItem si se foloseste .widget pentru al conveti intr ul widget pentru a permite stergerea
            curentDice = diceLayout.itemAtPosition(0, index)
            if curentDice:
                diceLayout.removeWidget(curentDice.widget())
            diceLayout.addWidget(self.createDiceObject(f"images/dice{getDice}.png"), 0, index)
        # incercare de a elimina spatiile dintre elemente
            # NU FUNCTIONEAZA
        diceLayout.setContentsMargins(0,0,0,0)
        # se dezactiveaza butonul
        self.layouts.enableRollButton(False)
        return dices

    #TODO:  cand este randul unui jucator, piesele celiolalt ar trebui dezactivate cu .setEnabled()

    # incearca sa faci o clasa separata logic(QThread) care sa realizeze in spate toata logica de care ai nevoie
        # alternativa
            # crearea unor variabile globale in gamelogic cu care sa interactioneze butoanele
                # de ex, gameProgress = "black" -> butoanele albe sunt dezactivate si invers
                # butoanele pot realiza mutari folosind combinatii din numarul zarului sau chiar unul din zaruri
                # dupa ce un buton si a realizat mutarea, acesta sa apeleze din nou functia logic
    def logic(self) -> None:
        print("Start game!")
        # initial butonul de dice este dezactivat, dar devine activ dupa apasare btonului de start
        self.layouts.enableRollButton(True) # si se ve dezactiva dupa apasarea butonului de rollDice

        # de test pentru a verifica disponibilitatea butoanelor
        # aceasta functie trebuie utilizatat la diferentierea jucatorilor
        self.layouts.checkersDisponibility(team = "black", disponibility = False)
        
        print("A iesit din functia logic")

    # TOTO: functia nu este gata, ar trebui sa verifice daca pozitiil unde urmeaza sa puna puesele sunt disponibile
        # disponibile inseamna ca pe acea pozitie sa nu existe o alta piesa a celuilalt jucator sau sa existe maxim una
            # in acest caz, piesa adversarului este scoasa pe gard
    def showPosibleMove(self, posName):
        # obtinerea numarului pozitiei
        posID = 0
        tempStr = ''
        for char in posName:
            if char.isdigit():
                tempStr = tempStr + char
        posID = int(tempStr)
        
        if self.dices:
            self.layouts.addCheckerToPosition(f'pos{posID + self.dices[0]}', "gost")
            # a doua mutare posibila 
            self.layouts.addCheckerToPosition(f'pos{posID + self.dices[1]}', "gost")
            # mutare posibila realizata prin combinarea pieselor
            self.layouts.addCheckerToPosition(f'pos{posID + self.dices[0] + self.dices[1]}', "gost")