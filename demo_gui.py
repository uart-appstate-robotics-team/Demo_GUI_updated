import cv2
import numpy as np

key = cv2. waitKey(1)
webcam = cv2.VideoCapture(0)

while True:

    check, frame = webcam.read()
    cv2.imshow("Capturing", frame)
    key = cv2.waitKey(1)
    if key == ord('s'):
        cv2.imwrite(filename='saved_img.jpg', img=frame)
        webcam.release()
        cv2.waitKey(1650)
        cv2.destroyAllWindows()
        img_ = cv2.imread('saved_img.jpg')
        gray=cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
        blurred=cv2.GaussianBlur(gray, (3,3), 0)
        wide = cv2.Canny(blurred, 15, 60)
        cv2.imshow("Edges", wide)
        cv2.waitKey(0)
        break

    elif key == ord('q'):
        webcam.release()
        cv2.destroyAllWindows()
        break




