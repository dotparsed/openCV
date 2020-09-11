import numpy as np
import cv2

img = cv2.imread('messi5.jpg')
img2 = cv2.imread('opencv-logo.png')




print(img.shape)
print(img.size)
print(img.dtype)

b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))

ball = img[280:340, 330:390]
img[273:333, 100:160] = ball

img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))


all = cv2.add(img, img2)
all2 = cv2.addWeighted(img2, 60, img, 34, 1)

cv2.imshow('myimg', all)
cv2.imshow('myimg2', all2)

cv2.waitKey(0)
cv2.destroyAllWindows()