import time
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer
import sys

class Fon_Neyman(QMainWindow):
    def __init__(self):
        super().__init__()

        self.operands = []
        self.operations = []

        self.setStyleSheet(open("static/css/fon_neyman/self.css").read())

        self.setWindowTitle("Fon Neyman")
        self.setGeometry(550, 300, 600, 240)

        self.font = QFont()
        self.font.setPointSize(10)

        # Input labels (Line Edit)
        self.input_operands = QLineEdit(self)
        self.input_operands.setGeometry(10, 10, 150, 30)
        self.input_operands.move(100, 50)
        self.input_operands.setPlaceholderText("Введіть операндуми")

        self.input_operations = QLineEdit(self)
        self.input_operations.setGeometry(10, 250, 150, 30)
        self.input_operations.move(300, 50)
        self.input_operations.setPlaceholderText("Введіть дії")

        # Send data button
        self.button = QPushButton(self)
        self.button.move(230, 100)
        self.button.setText("Send data")
        self.button.clicked.connect(self.get_data)
        self.button.setStyleSheet(open("static/css/fon_neyman/send_data.css").read())

        # Clear data button
        self.clear_data_button = QPushButton(self)
        self.clear_data_button.move(230, 200)
        self.clear_data_button.setText("Clear data")
        self.clear_data_button.clicked.connect(self.clear)
        self.clear_data_button.setStyleSheet(open("static/css/fon_neyman/clear_data.css").read())

        # Labels
        self.label_operands = QLabel(self)
        self.label_operands.setFont(self.font)
        self.label_operands.setGeometry(0,0, 800, 16)
        self.label_operands.setStyleSheet("QLabel {color: white;}")

        

        self.label_operations = QLabel(self)
        self.label_operations.setFont(self.font)
        self.label_operations.setGeometry(0, 20, 800, 16)
        self.label_operations.setStyleSheet("QLabel {color: white;}")

        # Calculation button
        self.calculation_button = QPushButton(self)
        self.calculation_button.move(230, 150)
        self.calculation_button.setText("Calculate")
        self.calculation_button.clicked.connect(self.calculate)
        self.calculation_button.setStyleSheet(open("static/css/fon_neyman/calculate.css").read())
        
        self.hud()

    # Мені самому соромно, вибачте за це: 
    def calculate(self):
        while len(self.operations) > 0:
            if len(self.operands) - 1 == len(self.operations):
                expression = str(self.operands[0]) + str(self.operations[0]) + str(self.operands[1])
                result = int(eval(expression))
                self.operands[0] = result
                del self.operands[1]
                del self.operations[0]
                self.hud()
            else:
                break


    def get_data(self):
        if not self.input_operands.text() and not self.input_operands.text():
            self.input_operations.setStyleSheet("QLineEdit {color: red; background-color: #2d2d2d;}")
            self.input_operands.setStyleSheet("QLineEdit {color: red; background-color: #2d2d2d;}")
        elif not self.input_operations.text() :
            self.input_operations.setStyleSheet("QLineEdit {color: red; background-color: #2d2d2d;}")

        elif not self.input_operands.text():
            self.input_operands.setStyleSheet("QLineEdit {color: red; background-color: #2d2d2d;}")
        
        else:
            self.operands.extend(int(i) for i in self.input_operands.text().split(" ")) 
            self.operations.extend(i for i in self.input_operations.text().split(" "))
            self.hud()
 
    def hud(self):
        self.label_operands.setText(f"Operands: {self.operands}")
        self.label_operations.setText(f"Operations: {self.operations}")
        self.input_operations.setStyleSheet("QLineEdit {background-color: #2d2d2d; color: white;}")
        self.input_operands.setStyleSheet("QLineEdit {background-color: #2d2d2d; color: white;}")
        self.update()
    
    def clear(self):
        self.operands = []
        self.operations = []
        self.hud()

if __name__ == '__main__':
    app = QApplication([])
    window = Fon_Neyman()
    window.show()
    sys.exit(app.exec_())
