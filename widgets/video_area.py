from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QPoint, QRect
from PyQt5.QtWidgets import QLabel, QRubberBand


class VideoArea(QLabel):
    def __init__(self, parent=None, main=None):
        QLabel.__init__(self, parent)
        self.selection = QRubberBand(QRubberBand.Rectangle, self)
        self.main = main
        self.setAlignment(Qt.AlignCenter)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:

            position = QPoint(event.pos())
            if self.selection.isVisible():
                if (self.upper_left - position).manhattanLength() < 20:
                    self.mode = "UL"
                elif (self.lower_right - position).manhattanLength() < 20:
                    self.mode = "LR"
                else:
                    self.selection.hide()
            else:
                self.upper_left = position
                self.lower_right = position
                self.mode = "LR"
                self.selection.show()

    def mouseMoveEvent(self, event):
        if self.selection.isVisible():
            if self.mode == "LR":
                self.lower_right = QPoint(event.pos())
            elif self.mode == "UL":
                self.upper_left = QPoint(event.pos())
            self.selection.setGeometry(QRect(self.upper_left, self.lower_right).normalized())

    def mouseReleaseEvent(self, event):
        self.main.controller.set_coordinates(*self.selection.geometry().getCoords())
        self.selection.hide()
