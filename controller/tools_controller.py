from PyQt5.QtWidgets import QFileDialog, QMessageBox
import cv2
import pafy


class ToolsController:
    def __init__(self, parent, tools):
        self.parent = parent
        self.tools = tools
        self.config = self.tools.config

    def open_file_name_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name = QFileDialog.getOpenFileName(self.parent, 'Open File', "", "Video files (*.mp4)")

        if file_name:
            self.config.capture = cv2.VideoCapture(file_name[0])
            self.config.is_up_to_date = False
            self.parent.start()

    def get_address(self):
        url = self.tools.address.get_address_text()
        self.config.capture = cv2.VideoCapture(url)

        if self.config.capture is None or not self.config.capture.isOpened():
            QMessageBox.information(self.parent, "Error", "Cannot open url {}.".format(url))
            return

        self.config.is_up_to_date = False
        self.parent.start()

    def get_yt_address(self):
        url = self.tools.address.get_address_text()

        try:
            video = pafy.new(url)
            best = video.getbest(preftype="mp4")
            self.config.capture = cv2.VideoCapture()
            self.config.capture.open(best.url)
            self.config.is_up_to_date = False
            self.parent.start()
        except:
            QMessageBox.information(self.parent, "Error", "Cannot open url {}.".format(url))

    def get_camera(self):
        self.config.capture = cv2.VideoCapture(0)

        if self.config.capture is None or not self.config.capture.isOpened():
            QMessageBox.information(self.parent, "Error", "Cannot open a camera.")
            return

        self.config.is_up_to_date = False
        self.parent.start()

    def slider_changed_value(self):
        self.config.movement_threshold = self.tools.slider_movement.get_value() * 100

        self.config.area_threshold = self.tools.slider_cached_area.get_value() * 100

        blurr = 2 * (self.tools.slider_blurr.get_value() // 5) + 1
        self.config.kernel_blurr_size = (blurr, blurr)

        self.config.is_up_to_date = False

    def get_coordinates(self):
        coords = self.tools.coordinates.get_coordinates()
        if all([x.isnumeric() for x in coords]):
            coords = [int(x) for x in coords]
            max_coords = (self.parent.frameGeometry().width(), self.parent.frameGeometry().height())

            if all([x >= 0 for x in coords]) \
                    and coords[0] + coords[2] < max_coords[0] and coords[1] + coords[3] < max_coords[1]:
                self.config.roi = ((float(coords[0]) / max_coords[0], float(coords[1]) / max_coords[1]),
                                   (float(coords[2]) / max_coords[0], float(coords[3]) / max_coords[1]))
                self.config.is_up_to_date = False
                return
        QMessageBox.information(self.parent, "Error", "Invalid coordinates.")

    def enable_debug(self):
        self.config.debug = self.tools.debug.is_enabled()
        self.config.is_up_to_date = False
