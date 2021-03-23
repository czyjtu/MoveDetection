from PyQt5.QtWidgets import QLabel, QWidget, QMainWindow, QHBoxLayout
from PyQt5.QtGui import QIcon

from views.main_view import MainAreaWidget
from views.tools_view import ToolsWidget

# TODO gui/input: górna granica coordinates, resize okna ogarnać

class GUIWindow(QMainWindow):
    def __init__(self):
        super(GUIWindow, self).__init__()

        self.setGeometry(50, 50, 1600, 900)
        self.setWindowTitle("OpenCV application")
        self.setWindowIcon(QIcon('pythonlogo.png'))

        tools = ToolsWidget(self)
        main_area = MainAreaWidget(self)

        self.hbox_layout = QHBoxLayout(self)
        self.hbox_layout.addWidget(main_area.get_main_area())
        self.hbox_layout.addWidget(tools.get_tools_area())

        self.show()


