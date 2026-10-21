# import cv2

# cam = cv2.VideoCapture(2)

# while True:
#     _, frame = cam.read()
#     cv2.imshow('my cam', frame)
#     cv2.waitKey(1)


import cv2

cam = cv2.VideoCapture(2)

while True:
    ret, frame = cam.read()

    if not ret:
        print("Camera open/read korte pareni!")
        break

    cv2.imshow('my cam', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()