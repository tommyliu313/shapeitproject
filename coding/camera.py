import cv2

cap = cv2.VideoCapture(0)

while(True):
# click the button esc and do the following action
    ret, frame = cap.read(1)
    if cv2.waitKey(1) & 0xFF == ord('e'):
        break
# close the application
cv2.window("camera",cap)

cv2.waitKey(0)
cv2.destroyAllWindows()
