from PyQt6.QtWidgets import QMainWindow, QFrame, QApplication

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Crearea unui obiect QFrame
        frame = QFrame(self)
        frame.setGeometry(50, 50, 200, 200)  # Setarea dimensiunilor și poziției ferestrei

        # Adăugarea QFrame la MainWindow
        self.setCentralWidget(frame)

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()
