import cv2
import numpy as np

#events = [i for i in dir(cv2) if 'EVENT' in i]
#print(events)


def click_event(event, x, y, flags, param):
    font = cv2.FONT_HERSHEY_SIMPLEX
    if event == cv2.EVENT_LBUTTONDOWN:
        str_x_y = str(x) + ", " + str(y)
        print(str_x_y)
        cv2.putText(img, str_x_y, (x, y), font, 0.7, (200, 0, 0), 2)
        cv2.imshow('image', img)

    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]

        str_bgr = str(blue) + " " + str(green) + " " + str(red)
        cv2.putText(img, str_bgr, (x, y), font, 0.7, (200, 0, 0), 2)
        cv2.imshow('image', img)


#img = np.zeros((500, 500, 3), np.uint8)
img = cv2.imread('lena.jpg', -1)

cv2.imshow('image',img)
cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
