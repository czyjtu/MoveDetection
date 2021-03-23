import cv2
import numpy as np




# TODO: type checking
class MoveDetector:
    def __init__(self, source, max_output: () = (800, 800)):
        self.src = source
        self.capture = None
        self.ROI = None
        self.area_threshold = None
        self.movement_threshold = None
        self.kernel_blurr_size = None
        self.show_bounding_box = None
        self.__FRAME_MAX_SIZE: () = max_output
  

    def fit_into_gui(self, frame_size: ()):
        frame_proportions: float = frame_size[0] / frame_size[1]
        gui_proportions: float = self.__FRAME_MAX_SIZE[0]/self.__FRAME_MAX_SIZE[1]
        if frame_proportions > gui_proportions:
            frame_size[0] = self.__FRAME_MAX_SIZE[0]
            frame_size[1] = self.__FRAME_MAX_SIZE[0] // frame_proportions
        else:
            frame_size[1] = self.__FRAME_MAX_SIZE[1]
            frame_size[0] = int(self.__FRAME_MAX_SIZE[1] * frame_proportions)
        return frame_size


    def load_source(self, source = None):
        if not(source is None):
            self.src = source

        capture = cv2.VideoCapture(self.src)

        if capture is None or not capture.isOpened():
            raise ValueError("given source is invalid.")

        self.capture = capture

    def generate(self, ROI = None, area_threshold = 100, movement_threshold = 500, kernel_blurr_size = (5, 5), show_bounding_box = False, frame_size = None):
        if self.capture is None:
            raise ValueError("you have to load source first.")

        self.frame_size = None # TODO: resize frame to the given size
        self.ROI = ROI
        self.area_threshold = area_threshold
        self.movement_threshold = movement_threshold
        self.kernel_blurr_size = kernel_blurr_size
        self.show_bounding_box = show_bounding_box

        # TODO: create constant framerate; preferably the video framerate
        for resized_frame, grey_roi, mask, blurred_mask, final_mask in self.__detect():
            # TODO: make output postprocessing to the gui wanted format; notice that DEBUG mode will be resolved here
            cv2.imshow('Frame', resized_frame)
            cv2.imshow("grey_frame", grey_roi)
            cv2.imshow('Mask', mask)
            cv2.imshow("blurred_mask", blurred_mask)
            cv2.imshow("final", final_mask)
            print("running")

            k = cv2.waitKey(1) & 0xff
            if k == 27:
                break
        
        capture.release()
        cv2.destroyAllWindows()
    
        
    def __detect(self):
        if self.capture is None:
            raise ValueError("you have to load source first.")

        detector = cv2.createBackgroundSubtractorKNN(detectShadows=True)
        frameCount = 0

        while True:
            ret, frame = self.capture.read()
            if not ret:
                break

            frameCount += 1

            # TODO: make function/method for frame preprocessing (need to return 3 frames-resized, roi, roi in grayscale)
            # preprocessing
            resized_frame = cv2.resize(frame, (800, 500)) #change size
            # cut area of interest
            if self.ROI is None:
                roi = resized_frame[:, :] 
            else:
                roi = resized_frame[self.ROI[0][0]: self.ROI[0][1], self.ROI[1][0]: self.ROI[1][1]]

            grey_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY) # change to grayscale

            # TODO: same thing for mask processing
            mask = detector.apply(grey_roi) 
            # denoising 
            blurred_mask = cv2.GaussianBlur(mask, self.kernel_blurr_size, 0) #simple denoising using Gaussian Blurring
            # blurred_mask = cv2.fastNlMeansDenoising(mask, h=30) # lepsze ale mega wolne
            _, final_mask = cv2.threshold(blurred_mask,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU) # setting the best treshold automatically
            # _, final_mask = cv2.threshold(blurred_mask, 200, 255, cv2.THRESH_BINARY) # manual tresholding

            # bounding boxes
            contours, _ = cv2.findContours(final_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            for cnt in contours:
                area = cv2.contourArea(cnt)
                if area > self.area_threshold:
                    if self.show_bounding_box:
                        x, y, w, h, = cv2.boundingRect(cnt)
                        cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 0), 3)
                    else :
                        cv2.drawContours(resized_frame, cnt, -1, (0,255,0), 3)

            count = np.count_nonzero(final_mask,)

            if (frameCount > 1 and count > self.movement_threshold):
                print('Movement')
                cv2.putText(resized_frame, 'Movement', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

            yield resized_frame, grey_roi, mask, blurred_mask, final_mask

    @staticmethod
    def __cut_and_resize(frame, roi: ((float, float), (float, float)), size: (int, int)):
        resized_frame = cv2.resize(frame, size)
        cut_frame = resized_frame[roi[0][0] * size[0]:roi[1][0] * size[0], roi[0][1] * size[1]:roi[1][1] * size[1]]
        grey_frame = cv2.cvtColor(cut_frame, cv2.COLOR_BGR2GRAY)
        return resized_frame, cut_frame, grey_frame



if __name__ == '__main__':
    det = MoveDetector("sample.mp4")
    det.load_source()
    det.generate(show_bounding_box=True, ROI=((250, 500), (400, 800)))
