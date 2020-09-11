import cv2
import os
import sys

try:
    label_name = sys.argv[1]
    num_samples = int(sys.argv[2])
except:
    print("Argument missing")
    print(desc)
    exit(-1)

img_save_path = 'image_data'
img_class_path = os.path.join(img_save_path, label_name)

try:
    os.mkdir(img_save_path)
except FileExistsError:
    pass

try:
    os.mkdir(img_class_path)
except FileExistsError:
    print("directory_already exist")
    print("all images saved in this folder")

cap = cv2.VideoCapture(0)

start = False
count = 0

while True:
    ret, frame = cap.read()

    if not ret:
        continue

    if count == num_samples:
        break

    cv2.rectangle(frame, (100, 100), (500, 500), (255, 255, 255), 2)

    if start:
        roi = frame[100:500, 100:500]
        save_path = os.path.join(img_class_path, '{}.jpg'.format(count))
        cv2.imwrite(save_path, roi)
        count += 1


    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, 'collecting{}'.format(count), (5, 50), font, 0.7, (255, 0, 0), 2, cv2.LINE_AA)

    cv2.imshow('collecting images', frame)

    k = cv2.waitKey(10)
    if k == ord('a'):
        start = not start
    if k == ord('q'):
        break
print("\n {} image(s) saved to {}".format(count, img_class_path))
cap.release()
cv2.destroyAllWindows()