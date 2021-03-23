from PyQt5.QtWidgets import QPushButton


class DebugWidget:
    def __init__(self, parent, controller):
        self.parent = parent
        self.controller = controller

        self.button_enable = QPushButton("Enable debug")
        self.button_enable.clicked.connect(lambda: self.controller.enable_debug())
        self.button_enable.setStyleSheet("background:#3f3f3f; color:#d1d1d1; text-transform:uppercase;")

    def get_debug_widget(self):
        return self.button_enable

    def is_enabled(self):
        if self.button_enable.text() == "Enable debug":
            self.button_enable.setText("Disable debug")
            return True
        self.button_enable.setText("Enable debug")
        return False
