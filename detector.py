import cv2
import numpy as np
from configuration import Configuration
import time


# TODO: type checking
class MoveDetector:
    def __init__(self, controller=None):
        self.controller = controller
        self.capture = None
        self.roi = None
        self.area_threshold = None
        self.movement_threshold = None
        self.kernel_blurr_size = None
        self.show_bounding_box = None
        self.max_window_size = None
        self.frame_size = None  # output frame size
        self.is_gui_open = None
        self.is_debug = None
        self.dilated_kernel_size = None
        self.pixel_threshold = None
        self.history_size = None

    # resize the frame to fit into gui window but keep original proportions
    def set_frame_size(self, frame_size):
        frame_proportions: float = frame_size[0] / frame_size[1]
        gui_proportions: float = self.max_window_size[0] / self.max_window_size[1]
        if frame_proportions > gui_proportions:
            w = int(self.max_window_size[0])
            h = int(self.max_window_size[0] // frame_proportions)
        else:
            w = int(self.max_window_size[1])
            h = int(self.max_window_size[1] * frame_proportions)

        self.frame_size = (w, h)

    def update_parameters(self):
        config = self.controller.get_config()
        # capture = cv2.VideoCapture("sample2.mp4")
        # if capture is None or not capture.isOpened():
        #     raise ValueError("given source is invalid.")
        # config = Configuration(capture = capture)

        self.capture = config.capture
        self.roi = config.roi
        self.area_threshold = config.area_threshold
        self.movement_threshold = config.movement_threshold
        self.kernel_blurr_size = config.kernel_blurr_size
        self.show_bounding_box = config.show_bounding_box
        self.max_window_size = config.max_window_size
        self.is_gui_open = config.is_window_open
        self.is_debug = config.debug
        self.dilated_kernel_size = config.dilated_kernel_size
        self.pixel_threshold = config.pixel_threshold
        self.eps = config.eps
        if config.history_size != self.history_size:
            self.history_size = config.history_size
            self.detector = cv2.createBackgroundSubtractorKNN(detectShadows=False, history = self.history_size)



    def generate(self):
        self.update_parameters()
        if self.capture is None:
            raise ValueError("you have to load source first.")

        fps = self.capture.get(cv2.CAP_PROP_FPS)

        time_stamp: float = time.time()

        heap_debug: bool = False

        for  resized_frame, grey_roi, mask, blurred_mask, dilated, final_mask in self.__detect():
            if self.controller.need_update():
                self.update_parameters()

            self.controller.update_frame(resized_frame)

            if not self.controller.is_window_open():
                break

            if self.is_debug:
                cv2.imshow("grey roi", grey_roi)
                cv2.imshow("mask", mask)
                cv2.imshow("1.blurred mask", blurred_mask)
                cv2.imshow("2.dilated mask", dilated)
                cv2.imshow("3.thresholded mask", final_mask)
                heap_debug = True
            elif heap_debug:
                cv2.destroyAllWindows()
                heap_debug = False

            cv2.waitKey(10)
            # time.sleep(max((1 / fps) - (time.time() - time_stamp), 0))
            time_stamp = time.time()

        self.capture.release()
        cv2.destroyAllWindows()

    def __next_frame(self):
        ret, frame = self.capture.read()
        if frame is None:
            return None

        if self.frame_size is None:
            width = self.capture.get(3)  # float `width`
            height = self.capture.get(4)  # float `height`
            self.set_frame_size((width, height))

        resized_frame = cv2.resize(frame, self.frame_size)
        cut_frame = resized_frame[
                    int(self.roi[0][1] * self.frame_size[1]): int(self.roi[1][1] * self.frame_size[1]),
                    int(self.roi[0][0] * self.frame_size[0]): int(self.roi[1][0] * self.frame_size[0])
                    ]
        grey_frame = cv2.cvtColor(cut_frame, cv2.COLOR_BGR2GRAY)
        return resized_frame, cut_frame, grey_frame

    def __detect(self):
        if self.capture is None:
            raise ValueError("you have to load source first.")

        self.detector = cv2.createBackgroundSubtractorKNN(detectShadows=False, history = self.history_size)
        frameCount = 0

        while True:
            frame_set = self.__next_frame()
            if frame_set is None:
                break
            else:
                resized_frame, roi, grey_roi = frame_set

            frameCount += 1

            blurred_roi = grey_roi #cv2.medianBlur(grey_roi, self.kernel_blurr_size[0])
            
            mask = self.detector.apply(blurred_roi)

            blurred_mask = cv2.GaussianBlur(mask, self.kernel_blurr_size, 0)

            if self.dilated_kernel_size != 0:
                kernal = np.ones((self.dilated_kernel_size, 3), np.uint8)
                dilated = cv2.dilate(blurred_mask, kernal, iterations= 2)
            else:
                dilated = blurred_mask

            _, final_mask = cv2.threshold(dilated, self.pixel_threshold, 255, cv2.THRESH_BINARY)  
         
            contours, _ = cv2.findContours(final_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            rects = [cv2.boundingRect(cnt) for cnt in 2*contours if cv2.contourArea(cnt) > self.area_threshold]

            if self.show_bounding_box:
                merge_rects, weights = cv2.groupRectangles(rects, 1, eps=self.eps) 
                for x, y, w, h in merge_rects:
                    cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 0), 2)
                count = np.count_nonzero(final_mask, )
            else:
                for x, y, w, h in rects:
                    cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 0), 2)

            count = np.count_nonzero(final_mask, )
            if (frameCount > 1 and count > self.movement_threshold):
                cv2.putText(resized_frame, 'Movement', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2,
                            cv2.LINE_AA)

            yield  resized_frame, grey_roi, mask, blurred_mask, dilated, final_mask

# if __name__ == '__main__':
#     det = MoveDetector()
#     det.generate()
