import cv2
import numpy as np

#events = [i for i in dir(cv2) if 'EVENT' in i]
#print(events)


points = []

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[x, y, 0]
        green = img[x, y, 1]
        red = img[x, y, 2]

        cv2.circle(img,(x, y), 3, (0, 200, 0), -1)
        my_color_image = np.zeros ((400, 400, 3), np.uint8)
        my_color_image[:] = [blue, green ,red]

        cv2.imshow('image', img)
        cv2.imshow('color', my_color_image)


#img = np.zeros((500, 500, 3), np.uint8)
img = cv2.imread('lena.jpg', -1)

cv2.imshow('image',img)
cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
