from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 

import sys
from emul.pascal import Pascal
from emul.fon import Fon_Neyman
from emul.lisp import Lisp


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
        self.pascal_button.clicked.connect(self.pascal)

        self.fon_button = QPushButton(self)
        self.fon_button.move(200, 50)
        self.fon_button.setStyleSheet(open("static/css/main/fon_neyman.css").read())
        self.fon_button.setText("Fon Neyman")
        self.fon_button.clicked.connect(self.fon)

        self.lisp_button = QPushButton(self)
        self.lisp_button.move(350, 50)
        self.lisp_button.setStyleSheet(open("static/css/main/lisp.css").read())
        self.lisp_button.setText("Lisp")
        self.lisp_button.clicked.connect(self.lisp)

        
    
    def fon(self):
        self.fon = Fon_Neyman()
        self.fon.show()

    def pascal(self):
        self.pascal = Pascal()
        self.pascal.show()
    
    def lisp(self):
        self.lisp = Lisp()
        self.lisp.show()

if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec_())