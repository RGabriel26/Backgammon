from PyQt6.QtWidgets import QLabel, QWidget, QPushButton
from PyQt6.QtGui import QPixmap

def createDiceObject(urlImage) -> QLabel:
    pixmap = QPixmap(urlImage)
    dice = QLabel()
    dice.setPixmap(pixmap)
    dice.setFixedSize(70,70)
    dice.setScaledContents(True)

    return dice
