from PyQt5.QtWidgets import QFileDialog, QMessageBox
import cv2
import pafy


class Controller:
    def __init__(self, parent, tools):
        self.parent = parent
        self.tools = tools
        self.capture = None

    def open_file_name_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name = QFileDialog.getOpenFileName(self.parent, 'Open File', "", "Video files (*.mp4)")
        if file_name:
            self.capture = cv2.VideoCapture(file_name[0])

    def get_address(self):
        url = self.tools.address.get_address_text()
        self.capture = cv2.VideoCapture(url)
        if self.capture is None or not self.capture.isOpened():
            QMessageBox.information(self.parent, "Error", "Cannot open url {}.".format(url))
        print(url)

    def get_yt_address(self):
        url = self.tools.address.get_address_text()
        try:
            video = pafy.new(url)
            best = video.getbest(preftype="mp4")
            self.capture = cv2.VideoCapture()
            self.capture.open(best.url)
        except:
            QMessageBox.information(self.parent, "Error", "Cannot open url {}.".format(url))
        print(url)

    def get_camera(self):
        self.capture = cv2.VideoCapture(0)
        if self.capture is None or not self.capture.isOpened():
            QMessageBox.information(self.parent, "Error", "Cannot open a camera.")
        print("camera")

    def slider_changed_value(self):
        value = self.tools.slider.get_value()
        print(value)

    def get_parameters(self):
        coords = self.tools.coordinates.get_coordinates()
        if all([x.isnumeric() for x in coords]):
            coords = [int(x) for x in coords]
            if all([x >= 0 for x in coords]): # TODO gorna granica
                print(coords)
                return
        QMessageBox.information(self.parent, "Error", "Invalid coordinates.")

    def enable_debug(self):
        is_debug = self.tools.debug.is_enabled()
        print(is_debug)
