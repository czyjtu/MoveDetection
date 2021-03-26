from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow

from configuration import Configuration
from controller.video_controller import VideoController
from detector import MoveDetector
from widgets.main_view import MainAreaWidget
from widgets.tools_view import ToolsWidget


# TODO gui/input: górna granica coordinates, resize okna ogarnać


class GUIWindow(QMainWindow):
    def __init__(self):
        super(GUIWindow, self).__init__()

        self.setGeometry(50, 50, 1600, 900)
        self.setWindowTitle("OpenCV application")
        self.setWindowIcon(QIcon('pythonlogo.png'))

        self.config = Configuration()
        self.controller = VideoController(self)

        self.tools = ToolsWidget(self, self.config)
        self.dock = self.tools.get_tools_area()
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock)

        self.main_area = MainAreaWidget(self, self.config, self.controller)
        self.setCentralWidget(self.main_area.get_main_area())

        self.controller.set_label(self.main_area.get_label())
        self.detector = MoveDetector(self.controller)

        self.show()

    def get_size(self):
        return self.frameGeometry().width(), self.frameGeometry().height()

    def start(self):
        self.detector.generate()

    def closeEvent(self, event):
        self.config.is_window_open = False
        event.accept()

