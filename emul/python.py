import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QTextEdit, QShortcut
from PyQt5.QtGui import QPixmap, QFont, QKeySequence
import io


class Python(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Python")

        self.setGeometry(350, 100, 1140, 852)
        # self.setGeometry()

        self.total = 0

        image_path = 'static/img/python.png'
        pixmap = QPixmap(image_path)

        self.image_label = QLabel(self)
        self.image_label.setPixmap(pixmap)

        self.image_label.setGeometry(10, 10, pixmap.width(), pixmap.height())
        self.font = QFont()
        self.font.setPointSize(22)
        self.font.setFamily("Consolas")


        self.lineedit = QTextEdit(self)
        self.lineedit.setGeometry(26, 30, 1090, 330)
        self.lineedit.setStyleSheet(open("static/css/python/lineedit.css").read())
        # self.lineedit.setTabStopWidth(4 * self.lineedit.fontMetrics().width(' '))

        self.label_output = QTextEdit(self)
        self.label_output.setReadOnly(True)
        self.label_output.setGeometry(26, 30+309, 1090, 300)
        self.label_output.setStyleSheet(open("static/css/python/label_output.css").read())

        # Shortcut
        shortcut = QShortcut(QKeySequence("Ctrl+Return"), self)
        shortcut.activated.connect(self.launch)

        self.setFocus()

    def launch(self):
        try:
            code = self.lineedit.toPlainText()
            sys.stdout = io.StringIO()
            exec(code, globals())
            result = sys.stdout.getvalue()
            self.label_output.setText(f"Output:\n{result}")
        except Exception as e:
            print(f"Error: {e}")
            self.label_output.setText(f"{e}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Python()
    window.show()
    sys.exit(app.exec_())
