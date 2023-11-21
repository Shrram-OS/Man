from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 

import sys
from emul.pascal import Pascal
from emul.fon import Fon_Neyman

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Man")
        self.setGeometry(550, 300, 900, 150)
        self.setStyleSheet(open("static/css/main/self.css").read())

        self.pascal_button = QPushButton(self)
        self.pascal_button.move(50, 50)
        self.pascal_button.setStyleSheet(open("static/css/main/pascal.css").read())
        self.pascal_button.setText("Pascalina")
        self.pascal_button.clicked.connect(self.hide)

        self.fon_button = QPushButton(self)
        self.fon_button.move(200, 50)
        self.fon_button.setStyleSheet(open("static/css/main/fon_neyman.css").read())
        self.fon_button.setText("Fon Neyman")
        self.fon_button.clicked.connect(self.fon)
        
    
    def fon(self):
        self.fon = Fon_Neyman()
        self.fon.show()

    def hide(self):
        self.pascal = Pascal()
        self.pascal.show()

if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec_())