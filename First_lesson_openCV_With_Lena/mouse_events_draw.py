import cv2
import numpy as np

#events = [i for i in dir(cv2) if 'EVENT' in i]
#print(events)


points = []

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
        points.append( (x, y))
        if len(points) >= 2:
            cv2.line(img, points[-1], points[-2],(200, 0, 0), 4)

        cv2.imshow('image', img)


#img = np.zeros((500, 500, 3), np.uint8)
img = cv2.imread('lena.jpg', -1)

cv2.imshow('image',img)
cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
