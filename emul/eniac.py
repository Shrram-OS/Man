#Абсолютно ничего не работает, даже не пробуйте.
# Если конкретно, библиотека cl4py не считает значение и eval() возвращает какой-то бред сумасшедшего.
# В коде разбирайтесь сами, комментарии писать у меня абсолютно отсутсвует желание
# Код ОЧЕНЬ простой и нормальные названия переменных не требуют комментарий
#  Код на 20 строчек, cmon

import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QLineEdit, QTextEdit, QShortcut
from PyQt5.QtGui import QPixmap, QFont, QKeySequence
from PyQt5.QtCore import QRect, Qt
import cl4py

lisp = cl4py.Lisp()

class Eniac(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ENIAC")

        self.setGeometry(550, 200, 690, 650)

        self.total = 0

        image_path = 'static/img/eniac.png'
        pixmap = QPixmap(image_path)

        self.image_label = QLabel(self)
        self.image_label.setPixmap(pixmap)

        self.image_label.setGeometry(10, 10, pixmap.width(), pixmap.height())
        self.font = QFont()
        self.font.setPointSize(22)
        self.font.setFamily("Consolas")


        self.lineedit = QTextEdit(self)
        self.lineedit.setGeometry(78, 70, 530, 210)
        self.lineedit.setStyleSheet(open("static/css/eniac/lineedit.css").read())

        self.label_output = QTextEdit(self)
        self.label_output.setReadOnly(True)
        self.label_output.setGeometry(78, 280, 530, 210)
        self.label_output.setStyleSheet(open("static/css/eniac/label_output.css").read())
        # self.label_output.setText("Output")

        shortcut = QShortcut(QKeySequence("Ctrl+Return"), self)
        shortcut.activated.connect(self.launch)

        self.setFocus()

    def launch(self):
        try:
            result = lisp.eval(self.lineedit.toPlainText())
            self.label_output.setText(f"Output:\n{result}")
            print(result)
        except Exception as e:
            print(f"Error: {e}")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Eniac()
    window.show()
    sys.exit(app.exec_())
