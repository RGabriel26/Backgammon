from PyQt6.QtWidgets import QLabel
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QFont

class MessageWindow():
    """Clasa care ofera ferestrele cu mesaje din timpul jocului:
    - mesaj pentru cand nu se poate realiza mutarea cu zarurile disponibile;
    - mesaj cand castiga unul din jucatori."""
    def __init__(self, parent, gameLogic):
        super().__init__()
        self.parent = parent
        self.gameLogic = gameLogic
        # centerMainWindow = self.parent.geometry().center()
        # TODO: Doar de test, este un bug cand centrul ferestrei main, uneori este altul.
        # TODO: BUG
        centerMainWindow = QPoint(960, 540)
        # normal ia rezolutia monitorului
        # metoade de rezolvare: 
        #  - sa se seteze rezolutia widgetului la rezolutia jocului
        #  - sa se realizeze link-uirea ferestrelor astfel incat sa se foloseasca dimensiunile ferestrei main
        print(centerMainWindow)
        self.centerX = centerMainWindow.x() - 430
        self.centerY = centerMainWindow.y() - 175

    def messageBox(self, needMessage, playerWin = None):
        self.messageBoxLabel = QLabel(self.parent, objectName = "messageBox")
        self.messageBoxLabel.setGeometry(self.centerX, self.centerY, 440, 80)
        self.messageBoxLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.messageBoxLabel.setFont(QFont("Times", 12, QFont.Weight.Bold.value))

        message_indisponibilMove = "Nu mai exista mutari posibile!"
        message_win = f"Felicitari jucatorului {playerWin}. Ai castigat jocul!"

        if needMessage == 1:
            self.messageBoxLabel.setText(message_indisponibilMove)
        elif needMessage == 2:
            self.messageBoxLabel.setText(message_win)

        self.messageBoxLabel.show()

