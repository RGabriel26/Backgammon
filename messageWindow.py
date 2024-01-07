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

        # doar pentru teste
        self.messageBox(2)

        # self.hide()

    def messageBox(self, needMessage, playerWin = None):
        self.messageBox = QLabel(self.parent)
        self.messageBox.setGeometry(self.centerX, self.centerY, 440, 80)
        # self.messageBox.setFixedSize(450, 250)   
        self.messageBox.setStyleSheet("background-color: rgba(63, 208, 27, 0.363)")
        self.messageBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.messageBox.setFont(QFont("Times", 12, QFont.Weight.Bold.value))

        message_indisponibilMove = "Nu se pot realiza mutari cu zarurile disponibile!"
        message_win = f"Felicitari jucatorului {playerWin}. Ai castigat jocul!"

        if needMessage == 1:
            self.messageBox.setText(message_indisponibilMove)
        elif needMessage == 2:
            self.messageBox.setText(message_win)

        self.messageBox.show()

