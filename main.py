import cv2

cap = cv2.VideoCapture(0)  # Try index 0 first

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

cap.set(3, 1200)
cap.set(4, 720)

while True:
    show, image = cap.read()
    if not show:
        print("Error: Could not read frame.")
        break

    cv2.imshow("Faces", image)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
        break

cap.release()
cv2.destroyAllWindows()
import cv2

cap = cv2.VideoCapture(0)  # Try index 0 first

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

cap.set(3, 1200)
cap.set(4, 720)

while True:
    show, image = cap.read()
    if not show:
        print("Error: Could not read frame.")
        break

    cv2.imshow("Faces", image)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
        break

cap.release()
cv2.destroyAllWindows()