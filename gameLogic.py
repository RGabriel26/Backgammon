from layouts import *

class GameLogic():
    def __init__(self):
        print("initializare gameLogic...")
        # folosit pentru a stoca zarurile generate in functia roll din RollFunctionalities
        self.dices = []
        self.layouts = UILayouts()
    
    def setDices(self,dices) -> None:
        self.dices = dices
        # self.layouts.setDefaultPosition()
        self.layouts.addCheckerToPosition(self.layouts.pos1, "black")
        print(self.dices)

    #TODO:  cand este randul unui jucator, piesele celiolalt ar trebui dezactivate cu .setEnabled()

