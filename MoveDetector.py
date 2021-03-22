import cv2
import numpy as np


def __read_and_cut(frame, V1: (), V2: ()):
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

        # History, Threshold, DetectShadows 
        fgbg = cv2.createBackgroundSubtractorMOG2(300, treshold, False)

        frameCount = 0

        while True:
            # Return Value and the current frame
            ret, frame = self.capture.read()

            #  Check if a current frame actually exist
            if not ret:
                break

            frameCount += 1
            # Resize the frame
            resizedFrame = cv2.resize(frame, (1500, 1000))

            # Get the foreground mask
            fgmask = fgbg.apply(resizedFrame)

            # Count all the non zero pixels within the mask
            count = np.count_nonzero(fgmask)

            print('Frame: %d, Pixel Count: %d' % (frameCount, count))

            # Determine how many pixels do you want to detect to be considered "movement"
            # if (frameCount > 1 and cou`nt > 5000):
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
    det = MoveDetector("sample.mp4")
    det.load_source()
    det.detect(500)




