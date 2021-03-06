import cv2 as cv
import numpy as np


haystack_img = cv.imread('albion_farm.jpg', -1)
needle_img = cv.imread('albion_cabbage.jpg', -1)

result = cv.matchTemplate(haystack_img, needle_img, cv.TM_CCOEFF_NORMED)

min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

print('Best match top left pos: %s' % str(max_loc))
print('Best match confidence: %s' % str(max_val))

threshold = 0.8
if max_val >= threshold:
    print('fond needle')

    needle_w = needle_img.shape[1]
    needle_h = needle_img.shape[0]

    top_left = max_loc
    bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)

    cv.rectangle(haystack_img, top_left, bottom_right, (0, 255, 0), 2, cv.LINE_4 )

else:
    print('needle not found')




cv.imshow('Result', haystack_img)
cv.imwrite('result.jpg', haystack_img)
cv.waitKey(0)