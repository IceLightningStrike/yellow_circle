import sys

from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from random import randint


class DrawCircle(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi("UI.ui", self)

        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paint(self) -> None:
        self.do_paint = True
        self.update()

    def paintEvent(self, event) -> None:
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def draw_circle(self, qp) -> None:
        x, y = randint(10, 590), randint(10, 590)
        d = randint(2, min(x, y, 800 - x, 600 - y) * 2)

        qp.setBrush(QColor('yellow'))
        qp.drawEllipse(x - d // 2, y - d // 2, d, d)


def except_hook(cls, exception, traceback) -> None:
    sys.excepthook(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DrawCircle()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
