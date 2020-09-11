import cv2

#cap = cv2.VideoCapture('myfile.avi')
#use webcam
cap = cv2.VideoCapture(0)

# fourcc - codec
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# 20 - frames/sec
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

        out.write(frame)

        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        cv2.imshow('frame', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
