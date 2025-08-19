import numpy as np
import cv2
import HandTrackingModule as htm
import time
import autopy

#######################
#Basic Camera Setting
wCam, hCam = 900, 600
#######################

cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4, hCam)
pTime = 0
detector = htm.HandDetector(maxHands=1)

while True:
    #Step 1: Find the Hand Landmarks
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)
    # print(lmList)

    #Step 2: get the tip of index and middle fingers
    if len(lmList )!= 0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]
        #print(x1, y1, x2, y2)

     #Step 3: Check which fingers is up
    fingers = detector.fingersUp()
    print(fingers)
    #Step 4: Only Index Finger : Moving mode
    #Step 5: Converting into coordinates
    #Step 6: Smoothen the values
    #Step 7: Moving the mouse using the coordinates
    #Step 8: For Clicking mode check if both index and middle fingers are up
    #Step 9: Find distance between the fingers
    #Step 10: If distance is short, then do the clicking action
    #Step 11: Checking the Frame Rate
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f"FPS:{int(fps)}", (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3) #FPS Count 
    #Step 12: Displaying the result
    cv2.imshow("Image", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    cv2.waitKey(1)

