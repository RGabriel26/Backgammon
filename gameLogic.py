
class GameLogic():
    def __init__(self):
        # folosit pentru a stoca zarurile generate in functia roll din RollFunctionalities
        self.dices = []
    
    def setDices(self,dices) -> None:
        self.dices = dices
        print(self.dices)

    #TODO:  cand este randul unui jucator, piesele celiolalt ar trebui dezactivate cu .setEnabled()

