from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSlider


class SliderBlurrWidget:
    def __init__(self, parent, controller):
        self.parent = parent
        self.controller = controller

        self.slider_widget = QWidget(self.parent)
        self.slider_widget.setGeometry(0, 100, 400, 50)

        self.slider_layout = QVBoxLayout(self.slider_widget)
        self.slider_layout.setContentsMargins(0, 0, 0, 20)
        self.slider_layout.setSpacing(20)
        self.slider_layout.setAlignment(Qt.AlignTop)

        self.slider_name = QLabel()
        self.slider_name.setText("1.blurr value")
        self.slider_name.setStyleSheet("font-size:15px; color:#c5c5c5; text-transform:uppercase;")
        self.slider_name.setGeometry(0, 0, 375, 20)

        self.slider = QSlider(Qt.Horizontal, self.slider_widget)
        self.slider.setGeometry(0, 0, 375, 30)
        self.slider.setMinimum(0)
        self.slider.setMaximum(10)
        self.slider.setValue(1)	
        self.slider.setTickInterval(1)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.valueChanged[int].connect(lambda: self.controller.slider_changed_value())
        self.slider_layout.addWidget(self.slider_name)
        self.slider_layout.addWidget(self.slider)

    def get_slider_widget(self):
        return self.slider_widget

    def get_value(self):
        return self.slider.value()