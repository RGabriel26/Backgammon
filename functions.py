from PyQt6.QtWidgets import QLabel, QPushButton
from PyQt6.QtGui import QPixmap

from random import randint

def createDiceObject(urlImage) -> QLabel:
    pixmap = QPixmap(urlImage)
    dice = QLabel()
    dice.setPixmap(pixmap)
    dice.setFixedSize(70,70)
    dice.setScaledContents(True)

    return dice

def roll(diceLayout):
    dices = [0, 0]

    for index in range(2):
        getDice = randint(1,6)
        dices[index] = getDice
        # stergerea zarului alfat in gridul diceLayout de pe pozitia 0 index pentru a nu se suprapune
        # .itemAtPosition returneaza un QLayoutItem si se foloseste .widget pentru al conveti intr ul widget pentru a permite stergerea
        curentDice = diceLayout.itemAtPosition(0, index)
        if curentDice:
            diceLayout.removeWidget(curentDice.widget())

        diceLayout.addWidget(createDiceObject(f"images/dice{getDice}.png"), 0, index)

    return dices

