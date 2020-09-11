import numpy as np
import cv2
#img = cv2.imread('lena.jpg', 1)


img = np.zeros([100, 512, 3], np.uint8)


img = cv2.line(img, (0, 0), (255, 255), (255, 0, 0), 5)
img = cv2.arrowedLine(img, (255, 0), (0, 255), (0, 0, 255), 5)
img = cv2.rectangle(img, (100,0),(200,100),(200,0,0), -1)

img = cv2.circle(img, (400, 300), 100,(20,20,20), -1)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img,'Text1',(10,500), font, 4, (0, 200, 0), cv2.LINE_AA)

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
