import cv2
import numpy as np


def __cut_and_resize(frame, V1: (), V2: ()):
    cut_frame = frame[V1[0]:V2[0], V1[1]:V2[1]]
    grey_frame = cv2.cvtColor(cut_frame, cv2.COLOR_BGR2GRAY)

    return grey_frame


class MoveDetector:
    """

    """
    def __init__(self, source):
        self.src = source
        self.capture = None
  

    def load_source(self, source = None):
        if not(source is None):
            self.src = source

        capture = cv2.VideoCapture(self.src)

        if capture is None or not capture.isOpened():
            raise ValueError("given source is invalid.")

        self.capture = capture


    def detect(self, treshold):
        if self.capture is None:
            raise ValueError("you have to load source first.")

        detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=500)

        frameCount = 0

        while True:
            ret, frame = self.capture.read()
            if not ret:
                break

            frameCount += 1
            # Resize the frame
            resizedFrame = cv2.resize(frame, (1000, 800))
            roi = resizedFrame[300:800, 600:900]

            # Get the foreground mask
            fgmask = detector.apply(roi)

            # removing shadows
            # _, fgmask = cv2.threshold(fgmask, 254, 255, cv2.THRESH_BINARY)

            contours, _ = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            for cnt in contours:
                area = cv2.contourArea(cnt)
                if area > 100:
                    x, y, w, h, = cv2.boundingRect(cnt)
                    cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 0), 3)

            count = np.count_nonzero(fgmask)
            print('Frame: %d, Pixel Count: %d' % (frameCount, count))
            if (frameCount > 1 and count > treshold):
                print('Movement')
                cv2.putText(resizedFrame, 'Movement', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

            cv2.imshow('Frame', resizedFrame)
            cv2.imshow('Mask', fgmask)
    
            k = cv2.waitKey(1) & 0xff
            if k == 27:
                break

        capture.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    det = MoveDetector("sample2.mp4")
    det.load_source()
    det.detect(500)




