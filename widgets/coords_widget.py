from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSlider, QGridLayout, QLineEdit, QPushButton


class CoordinatesWidget:
    def __init__(self, parent, controller):
        self.parent = parent
        self.controller = controller

        self.toolbox_widget = QWidget(self.parent)
        self.toolbox_widget.setGeometry(0, 0, 400, 400)
        self.toolbox_widget.setStyleSheet("background:#5e5e5e; border: 1px solid #494949;")
        self.toolbox_layout = QGridLayout(self.toolbox_widget)

        self.x_field = QLineEdit(self.toolbox_widget)
        self.y_field = QLineEdit(self.toolbox_widget)
        self.width_field = QLineEdit(self.toolbox_widget)
        self.height_field = QLineEdit(self.toolbox_widget)

        self.x_field.resize(170, 20)
        self.y_field.resize(170, 20)
        self.width_field.resize(170, 20)
        self.width_field.resize(170, 20)

        self.x_field.setStyleSheet("background:#494949; border: 1px solid #3a3a3a;color:#c5c5c5")
        self.y_field.setStyleSheet("background:#494949; border: 1px solid #3a3a3a;color:#c5c5c5")
        self.width_field.setStyleSheet("background:#494949; border: 1px solid #3a3a3a;color:#c5c5c5")
        self.height_field.setStyleSheet("background:#494949; border: 1px solid #3a3a3a;color:#c5c5c5")

        self.x_label = QLabel()
        self.x_label.setText("x value")
        self.y_label = QLabel()
        self.y_label.setText("y value")

        self.width_label = QLabel()
        self.width_label.setText("width value")
        self.height_label = QLabel()
        self.height_label.setText("height value")

        self.x_label.setStyleSheet(" border: none; color:#c5c5c5;")
        self.y_label.setStyleSheet(" border: none; color:#c5c5c5;")
        self.width_label.setStyleSheet(" border: none; color:#c5c5c5;")
        self.height_label.setStyleSheet("border: none; color:#c5c5c5;")

        self.toolbox_layout.addWidget(self.x_label, 0, 0)
        self.toolbox_layout.addWidget(self.x_field, 1, 0)
        self.toolbox_layout.addWidget(self.y_label, 0, 1)
        self.toolbox_layout.addWidget(self.y_field, 1, 1)
        self.toolbox_layout.addWidget(self.width_label, 2, 0)
        self.toolbox_layout.addWidget(self.width_field, 3, 0)
        self.toolbox_layout.addWidget(self.height_label, 2, 1)
        self.toolbox_layout.addWidget(self.height_field, 3, 1)
        self.toolbox_widget.setLayout(self.toolbox_layout)

        self.toolbox_button = QPushButton("Choose Parameters")
        self.toolbox_button.setStyleSheet("background:#3f3f3f; color:#d1d1d1; text-transform:uppercase;")
        self.toolbox_button.clicked.connect(lambda: self.controller.get_coordinates())

    def get_coordinates_widget(self):
        return self.toolbox_widget

    def get_coordinates_button(self):
        return self.toolbox_button

    def get_coordinates(self):
        return [self.x_field.text(), self.y_field.text(), self.width_field.text(), self.height_field.text()]