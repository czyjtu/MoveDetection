import cv2
import pafy

# TODO: jak będzie już przycisk wyboru źródła to napiszę kontroler do niego, żeby tworzył i zwracał odpowiedni capture

title = "Stream"

''' Webcam '''
# capture = cv2.VideoCapture(0, cv2.CAP_DSHOW) # cap_dshow is windows only, generally can go without it

''' Local file '''
# file_path = "cut.mp4"
# capture = cv2.VideoCapture(file_path)

''' IP camera/RTSP stream '''
# Sample streams
# url = "http://46.151.101.149:8081/?action=stream"
# url = "http://158.58.130.148/mjpg/video.mjpg"
# url = 'rtsp://freja.hiof.no:1935/rtplive/definst/hessdalen03.stream'
# url = "http://81.83.10.9:8001/mjpg/video.mjpg"
# capture = cv2.VideoCapture(url)

''' Youtube video and livestream '''
url = "https://youtu.be/OWA0y-ocjIs"
video = pafy.new(url)
best = video.getbest(preftype="mp4")
capture = cv2.VideoCapture()
capture.open(best.url)


while capture.isOpened():
    ret, frame = capture.read()
    cv2.imshow(title, frame)

    # w waitKey musi być jakaś liczba > 0, bo filmikom z yt odwala inaczej
    if cv2.waitKey(24) & 0xFF == ord('q'):
        break

    if cv2.getWindowProperty(title, cv2.WND_PROP_VISIBLE) < 1:
        break

capture.release()
cv2.destroyAllWindows()