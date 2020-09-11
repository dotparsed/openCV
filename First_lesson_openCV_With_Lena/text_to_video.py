import cv2
import datetime
cap = cv2.VideoCapture(0)

# c
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(3), cap.get(4))

# cap.set(3, 100)  = cap.set(cv2.CAP_PROP_FRAME_WIDTH)
cap.set(3, 600)
cap.set(4, 600)

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = "WIDTH: " + str(cap.get(3))+" "+"HEIGHT" + str(cap.get(4))
        datet = str(datetime.datetime.now())

        frame = cv2.putText(frame, datet, (4, 50), font, 1, (0, 200, 0), 2, cv2.LINE_AA)


        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()