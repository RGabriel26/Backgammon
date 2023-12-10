from PyQt6.QtWidgets import QLabel, QWidget, QPushButton
from PyQt6.QtGui import QPixmap

def createDiceObject(urlImage) -> QLabel:
    pixmap = QPixmap(urlImage)
    dice = QLabel()
    dice.setPixmap(pixmap)
    dice.setFixedSize(70,70)
    dice.setScaledContents(True)

    return dice

def createRollButton(urlImage) -> QPushButton:
    pixmap = QPixmap(urlImage)
    rollButton = QLabel()
    rollButton.setPixmap(pixmap)
    rollButton.setFixedSize(100,100)
    rollButton.setScaledContents(True)

    return rollButton