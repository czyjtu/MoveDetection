from typing import Tuple # pip install typing

class Configuration:
    """
    param capture: cv2 VideoCapture object
    param area_threshold: minimum area of the moving object to be marked with countours
    param movement_threshold: minimum number of non-zero pixels in the mask to consider it as movement
    param kernel_blurr_size: kernel size for  Gaussian blurr algorithm
    param show_bounding_boxes: if True, boundig boxes will be shown instead of the contours
    param max_window_size: maximum dimensions in pixels for the VideoCapture
    param roi: area of interest, described in realtive unit
    """
    def __init__(
        self,
        capture = None,
        area_threshold: int = 100,
        movement_threshold: int = 500,
        kernel_blurr_size: Tuple[int, int] = (5, 5),
        show_bounding_box: bool = True,
        max_window_size: Tuple[int, int] = (800, 800), 
        roi: Tuple[Tuple[float, float], Tuple[float, float]] = ((0., 1.), (0., 1.)),
        debug: bool = False

    ):
        self.capture = capture
        self.area_threshold = area_threshold
        self.movement_threshold = movement_threshold
        self.kernel_blurr_size = kernel_blurr_size
        self.show_bounding_box = show_bounding_box
        self.max_window_size = max_window_size
        self.roi = roi
        self.debug = debug

        self.is_up_to_date = False
        