from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel


class MainAreaWidget:
    def __init__(self, parent):
        self.parent = parent
        self.widget = QWidget(parent)
        self.widget.setGeometry(0, 0, 1200, 900)
        self.widget.setStyleSheet("background-color:#494949")

        self.video_area = QWidget(self.widget)
        self.video_area.setStyleSheet("background:#232323; border: 1px solid #5e5e5e;")
        self.video_area.setGeometry(20, 20, 1160, 700)
        self.video_layout = QGridLayout(self.video_area)
        self.video_label = QLabel(self.video_area)
        self.video_layout.addWidget(self.video_label, 0, 0)
        self.video_area.setLayout(self.video_layout)

    def get_main_area(self):
        return self.widget
