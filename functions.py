from PyQt6.QtWidgets import QLabel
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

        diceLayout.addWidget(createDiceObject(f"images/dice{getDice}.png"), 0, index)

    return dices