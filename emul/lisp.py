import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QTextEdit, QShortcut
from PyQt5.QtGui import QPixmap, QFont, QKeySequence
import cl4py
import ast

class Lisp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Lisp")

        self.setGeometry(550, 200, 690, 650)

        self.total = 0

        image_path = 'static/img/lisp.png'
        pixmap = QPixmap(image_path)

        self.image_label = QLabel(self)
        self.image_label.setPixmap(pixmap)

        self.image_label.setGeometry(10, 10, pixmap.width(), pixmap.height())
        self.font = QFont()
        self.font.setPointSize(22)
        self.font.setFamily("Consolas")


        self.lineedit = QTextEdit(self)
        self.lineedit.setGeometry(78, 70, 530, 210)
        self.lineedit.setStyleSheet(open("static/css/lisp/lineedit.css").read())

        self.label_output = QTextEdit(self)
        self.label_output.setReadOnly(True)
        self.label_output.setGeometry(78, 280, 530, 210)
        self.label_output.setStyleSheet(open("static/css/lisp/label_output.css").read())

        shortcut = QShortcut(QKeySequence("Ctrl+Return"), self)
        shortcut.activated.connect(self.launch)

        self.setFocus()
        self.lisp = cl4py.Lisp()

    def launch(self):
        try:
            result = self.lisp.eval(ast.literal_eval(self.lineedit.toPlainText().replace(" ", ", ")))
            self.label_output.setText(f"Output:\n{result}")
            print(result)
        except Exception as e:
            print(f"Error: {e}")
            self.label_output.setText("ERROR :/")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Lisp()
    window.show()
    sys.exit(app.exec_())
