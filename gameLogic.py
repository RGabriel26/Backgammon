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
        # self.layouts.enableRollButton(False)
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
    def showPosibleMove(self, posName, oponentTeam = "black"):
        # obtinerea numarului pozitiei
        posID = 0
        tempStr = ''
        for char in posName:
            if char.isdigit():
                tempStr = tempStr + char
        posID = int(tempStr)
        if self.dices:
            # prima mutare posibila
            firtMove = posID + self.dices[0]
            # a doua mutare posibila
            secondMove = posID + self.dices[1]
            # mutare posibila realizata prin combinarea pieselor
            combinedMove = posID + self.dices[0] + self.dices[1]
            possibleMove = [firtMove, secondMove, combinedMove]

            for move in possibleMove:
                if move < 24:
                    print(move)
                # cazul in care pe pozitia posibila exista alte piese
                    if getattr(self.layouts, f'pos{move}').count() > 0:
                        # verificare daca adversarul are cel putin o piesa pe pozitia posibila 
                            # veificam ca pe pozitia respectica sa existe doar o piesa
                        if getattr(self.layouts, f'pos{move}').count() == 1:
                            print("exista o piesa")
                            # daca exista doar o piesa, atunci se verifica daca acesta este a adversarului
                            if getattr(self.layouts, f'pos{move}').itemAt(0).widget().objectName() == f'{oponentTeam}Checker':
                                print("piesa adversarului")
                                # daca piesa este a adversarului, atunci se poate muta pe pozitia respectiva
                                    # aici, piesa gost ar trebui sa inlocuiasca piesa adversarului si
                                    # piesa adversarului ar trebui sa fie aruncata pe gard
                                self.layouts.deleteOponentCheker(move)
                                self.layouts.addCheckerToPosition(f'pos{move}', "gost")
                                self.layouts.addCheckersToFence(oponentTeam)
                                # TODO: Trebuie apelata finctia care la momentul selectarii pozitiei, piesa adversarului sa fie aruncata pe gard
                        # # excluderea pozitiilor unde exista piese ale opentului
                        if getattr(self.layouts, f'pos{move}').itemAt(0).widget().objectName() != f'{oponentTeam}Checker':
                            self.layouts.addCheckerToPosition(f'pos{move}', "gost")
                    else:
                        # cazul in cere pe pozitia posibila nu exista alte piese
                        self.layouts.addCheckerToPosition(f'pos{move}', "gost")

                # TODO: Trebuie creata o functia care sa verifica ca jucatorul are toate piesele in casa
                        # pentru ca sa poate scoate piesele din casa, astfel castigand jocul