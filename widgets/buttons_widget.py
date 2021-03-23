from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QGridLayout


class QGridBoxLayout(object):
    pass


class ButtonsWidget:
    def __init__(self, parent, controller):
        self.parent = parent
        self.controller = controller
        self.button_widget = QWidget(parent)
        self.button_widget.setGeometry(0, 0, 400, 50)

        self.button_layout = QGridLayout(self.button_widget)
        self.button_layout.setContentsMargins(0, 0, 0, 0)
        self.button_layout.setSpacing(5)

        self.file_button = QPushButton("Choose File")
        self.path_button = QPushButton("Choose Address")
        self.camera_button = QPushButton("Choose Camera")
        self.yt_button = QPushButton("Choose Youtube")

        self.file_button.clicked.connect(lambda: self.controller.open_file_name_dialog())
        self.path_button.clicked.connect(lambda: self.controller.get_address())
        self.camera_button.clicked.connect(lambda: self.controller.get_camera())
        self.yt_button.clicked.connect(lambda: self.controller.get_yt_address())

        self.file_button.setStyleSheet("background:#3f3f3f; color:#d1d1d1; text-transform:uppercase;")
        self.path_button.setStyleSheet("background:#3f3f3f; color:#d1d1d1; text-transform:uppercase;")
        self.camera_button.setStyleSheet("background:#3f3f3f; color:#d1d1d1; text-transform:uppercase;")
        self.yt_button.setStyleSheet("background:#3f3f3f; color:#d1d1d1; text-transform:uppercase;")

        self.button_layout.addWidget(self.file_button)
        self.button_layout.addWidget(self.path_button)
        self.button_layout.addWidget(self.camera_button)
        self.button_layout.addWidget(self.yt_button)

    def get_buttons_widget(self):
        return self.button_widget
