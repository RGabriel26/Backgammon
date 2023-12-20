from PyQt6.QtWidgets import QApplication
from layouts import *

import time

class GameLogic():
    def __init__(self):
        print("initializare gameLogic...")
        # folosit pentru a stoca zarurile generate in functia roll din RollFunctionalities
        self.dices = []
        self.layouts = UILayouts()
    
    # incearca sa faci o clasa separata logic(QThread) care sa realizeze in spate toata logica de care ai nevoie
        # alternativa
            # crearea unor variabile globale in gamelogic cu care sa interactioneze butoanele
                # de ex, gameProgress = "black" -> butoanele albe sunt dezactivate si invers
                # butoanele pot realiza mutari folosind combinatii din numarul zarului sau chiar unul din zaruri
                # dupa ce un buton si a realizat mutarea, acesta sa apeleze din nou functia logic
    def logic(self) -> None:
        print("Start game!")

        self.layouts.disableCheckers("black")

        #prima persoana da cu zarul
        self.layouts.enableRollButton()
        
        # timp in care dai cu zaru

        self.layouts.disableRollButton()

        # asteapta pentru apasarea buronului
        # while True:
        #     QApplication.processEvents()
        #     if self.dices:
        #         # print(f"Au picat zarurile {self.dices[0]} {self.dices[1]}")
        #         # self.layouts.disableRollButton()
        #         break
        print("A iesit din functia logic")
    
    def rollDices(self,dices) -> None:
        self.dices = dices
        print(f"Au picat zarurile {self.dices[0]} {self.dices[1]}")

    #TODO:  cand este randul unui jucator, piesele celiolalt ar trebui dezactivate cu .setEnabled()

