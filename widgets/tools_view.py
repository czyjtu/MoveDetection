from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QDockWidget

from widgets.address_widget import AddressWidget

from controller.tools_controller import ToolsController
from widgets.buttons_widget import ButtonsWidget
from widgets.coords_widget import CoordinatesWidget
from widgets.debug_widget import DebugWidget
from widgets.slider_widget import SliderWidget


class ToolsWidget:
    def __init__(self, parent, config):
        self.parent = parent
        self.config = config
        self.widget = QWidget(self.parent)
        self.widget.setGeometry(1200, 0, 400, 900)
        self.widget.setStyleSheet("background-color:#717171")

        self.dock = QDockWidget("Tools", self.parent)
        self.dock.setWidget(self.widget)
        self.dock.setFeatures(QDockWidget.DockWidgetFloatable | QDockWidget.DockWidgetMovable)

        self.tools_layout = QVBoxLayout(self.widget)
        self.tools_layout.setAlignment(Qt.AlignTop)
        self.tools_layout.setSpacing(15)

        self.controller = ToolsController(self.parent, self)

        self.address = AddressWidget(self.widget, self.controller)
        self.tools_layout.addWidget(self.address.get_address_widget())

        self.buttons = ButtonsWidget(self.widget, self.controller)
        self.tools_layout.addWidget(self.buttons.get_buttons_widget())

        self.slider = SliderWidget(self.widget, self.controller)
        self.tools_layout.addWidget(self.slider.get_slider_widget())

        self.coordinates = CoordinatesWidget(self.widget, self.controller)
        self.tools_layout.addWidget(self.coordinates.get_coordinates_widget())
        self.tools_layout.addWidget(self.coordinates.get_coordinates_button())

        self.debug = DebugWidget(self.widget, self.controller)
        self.parent.enabled = False
        self.tools_layout.addWidget(self.debug.get_debug_widget())

    def get_tools_area(self):
        return self.dock
