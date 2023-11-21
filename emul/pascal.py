import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt, QRect


class Pascal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pascalina")

        self.setGeometry(500, 300, 0, 0)

        self.total = 0

        image_path = 'static/img/pascal.png'
        pixmap = QPixmap(image_path)

        self.image_label = QLabel(self)
        self.image_label.setPixmap(pixmap)

        self.font = QFont()
        self.font.setPointSize(14)

    
        self.image_label.mousePressEvent = self.on_image_click
        self.setCentralWidget(self.image_label)

        self.text_hs = QLabel(self)
        self.text_hs.setFont(self.font)
        self.text_hs.move(74, 20)

        self.text_ts = QLabel(self)
        self.text_ts.setFont(self.font)
        self.text_ts.move(243, 20)

        self.text_s = QLabel(self)
        self.text_s.setFont(self.font)
        self.text_s.move(402, 20)

        self.text_h = QLabel(self)
        self.text_h.setFont(self.font)
        self.text_h.move(567, 20)

        self.text_t = QLabel(self)
        self.text_t.setFont(self.font)
        self.text_t.move(730, 20)

        self.text_u = QLabel(self)
        self.text_u.setFont(self.font)
        self.text_u.move(896, 20)

        self.button_rectangles = [
            QRect(1, 136, 166, 186),
            QRect(167, 136, 166, 186),
            QRect(333, 136, 166, 186),
            QRect(499, 136, 166, 186),
            QRect(665, 136, 166, 186),
            QRect(825, 136, 166, 186),
        ]
        
        self.hud()
    
    def hud(self):
        self.text_hs.setText(str((self.total // 100000) % 10))
        self.text_ts.setText(str((self.total // 10000) % 10))
        self.text_s.setText(str((self.total // 1000) % 10))
        self.text_h.setText(str((self.total // 100) % 10))
        self.text_t.setText(str((self.total // 10) % 10))
        self.text_u.setText(str(self.total % 10))


    def on_image_click(self, event):
        x = event.x()
        y = event.y()

        for i, rect in enumerate(self.button_rectangles[::-1]):
            if rect.contains(x, y):
                self.total += 1 * 10**i
                print(self.total)
        
        self.hud()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Pascal()
    window.show()
    sys.exit(app.exec_())
