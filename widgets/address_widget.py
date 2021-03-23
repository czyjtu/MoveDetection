from PyQt5.QtWidgets import QWidget, QLineEdit, QVBoxLayout


class AddressWidget:
    def __init__(self, parent, controller):
        self.parent = parent
        self.controller = controller

        self.address_widget = QWidget(self.parent)
        self.address_widget.setGeometry(0, 0, 400, 30)
        self.address_layout = QVBoxLayout(self.address_widget)
        self.file_address = QLineEdit(self.address_widget)
        self.file_address.resize(400, 25)
        self.file_address.setStyleSheet("background-color:#a7a7a7")
        self.address_layout.addWidget(self.file_address)

    def get_address_widget(self):
        return self.address_widget

    def get_address_text(self):
        return self.file_address.text()
