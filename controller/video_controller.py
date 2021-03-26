from PyQt5.QtCore import Qt, QRect, QSize
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QRubberBand


# TODO: lol pół okna, brak resizu, roi,


class VideoController:
    def __init__(self, parent):
        self.parent = parent
        self.config = self.parent.config

    def need_update(self):
        return not self.config.is_up_to_date

    def set_label(self, label):
        self.label = label

    def update_frame(self, frame):
        h, w, ch = frame.shape
        bytesPerLine = ch * w
        converted = QImage(frame.data, w, h, bytesPerLine, QImage.Format_BGR888)

        self.label.resize(*self.parent.get_size())
        image = converted.scaled(*self.parent.get_size(), Qt.KeepAspectRatio)

        self.label.setPixmap(QPixmap(image))
        self.config.is_up_to_date = True

    def get_config(self):
        return self.config

    def set_coordinates(self, x1, y1, x2, y2):
        max_w, max_h = self.parent.get_size()
        self.config.roi = ((x1/max_w, y1/max_h), (x2/max_w, y2/max_h))
        self.config.is_up_to_date = False

    def is_window_open(self):
        return self.config.is_window_open
