import cv2 as cv
import numpy as np
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def findClickPositions(needle_img_path, haystack_img_path, threshold=0.5, debug_mode=None):

    haystack_img = cv.imread('albion_farm.jpg', cv.IMREAD_UNCHANGED)
    needle_img = cv.imread('albion_cabbage.jpg', cv.IMREAD_UNCHANGED)

    needle_w = needle_img.shape[1]
    needle_h = needle_img.shape[0]

    # There are 6 methods to choose from:
    # TM_CCOEFF, TM_CCOEFF_NORMED, TM_CCORR, TM_CCORR_NORMED, TM_SQDIFF, TM_SQDIFF_NORMED
    method = cv.TM_CCOEFF_NORMED
    result = cv.matchTemplate(haystack_img, needle_img, method)

    locations = np.where(result >= threshold)
    locations = list(zip(*locations[::-1]))


    rectangles = []
    for loc in locations:
        rect = [int(loc[0]), int(loc[1]), needle_w, needle_h]

        # its must repeat because group rectangle need two copy for comfirm
        rectangles.append(rect)
        rectangles.append(rect)

    rectangles, weights = cv.groupRectangles(rectangles, 1, 0.5)
    print(rectangles)

    points = []
    if len(rectangles):
        print("Found needle")

        for (x, y, w, h) in rectangles:

            center_x = x + int(w / 2)
            center_y = y + int(h / 2)
            points.append((center_x, center_y))

            if debug_mode == 'rectangles':
                top_left = (x, y)
                bottom_right = (x + w, y + h)
                cv.rectangle(haystack_img, top_left, bottom_right, (0, 255, 0), 2, cv.LINE_4)
        
            elif debug_mode == 'points':
                cv.drawMarker(haystack_img, (center_x, center_y), (0, 0, 255), cv.MARKER_CROSS)
        if debug_mode:
            cv.imshow('result',haystack_img)
            cv.waitKey(0)
            cv.destroyAllWindows()
    return points


points = findClickPositions('albion_cabbage.jpg', 'albion_farm.jpg', debug_mode='points')
print(points)
points = findClickPositions('albion_turnip.jpg', 'albion_farm.jpg',
                            threshold=0.70, debug_mode='rectangles')
print(points)
print('Done.')