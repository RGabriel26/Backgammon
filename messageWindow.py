from PyQt6.QtWidgets import QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

class MessageWindow():
    def __init__(self, parent, gameLogic):
        super().__init__()
        self.parent = parent
        self.gameLogic = gameLogic
        centerMainWindow = self.parent.geometry().center()
        self.centerX = centerMainWindow.x() - 430
        self.centerY = centerMainWindow.y() - 175

    def messageBox(self, needMessage, playerWin = None):
        self.messageBoxLabel = QLabel(self.parent, objectName = "messageBox")
        self.messageBoxLabel.setGeometry(self.centerX, self.centerY, 440, 80)
        # self.messageBoxLabel.setFixedSize(450, 250)   
        self.messageBoxLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.messageBoxLabel.setFont(QFont("Times", 12, QFont.Weight.Bold.value))

        message_indisponibilMove = "Nu mai exista mutari posibile!"
        message_win = f"Felicitari jucatorului {playerWin}. Ai castigat jocul!"

        if needMessage == 1:
            self.messageBoxLabel.setText(message_indisponibilMove)
        elif needMessage == 2:
            self.messageBoxLabel.setText(message_win)

        self.messageBoxLabel.show()

