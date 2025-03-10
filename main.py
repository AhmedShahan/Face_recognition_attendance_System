import cv2
import os 
cap = cv2.VideoCapture(0)  # Try index 0 first
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

cap.set(3, 1200)
cap.set(4, 720)


img_background="/home/shahanahmed/Downloads/FaceRocognition/Files/Resources/background.png"

folderModePath="/home/shahanahmed/Downloads/FaceRocognition/Files/Resources/Modes"
modePath=os.listdir(folderModePath)
imgMode=[]
for path in folderModePath:

while True:
    show, image = cap.read()
    img_background[162:162, 480, 55:55 + 640]=image
    if not show:
        print("Error: Could not read frame.")
        break

    # cv2.imshow("Faces", image)


    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
        break

cap.release()
cv2.destroyAllWindows()