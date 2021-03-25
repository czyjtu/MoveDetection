from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel

from controller.video_controller import VideoController
from widgets.video_area import VideoArea


class MainAreaWidget:
    def __init__(self, parent, config, controller):
        self.parent = parent
        self.config = config
        self.widget = QWidget(parent)
        self.widget.setStyleSheet("background-color:#494949")

        self.video_area = VideoArea(self.widget, self.parent)
        self.video_area.setStyleSheet("background:#232323; border: 1px solid #5e5e5e;")
        self.video_area.setGeometry(10, 10, 1310, 880)

        self.controller = controller

    def get_label(self):
        return self.video_area

    def get_main_area(self):
        return self.widget
