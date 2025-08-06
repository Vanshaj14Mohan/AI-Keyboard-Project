import numpy as np
import cv2
import HandTrackingModule as htm
import time
import autopy

#######################
#Basic Camera Setting
wCam, hCam = 640, 480
#######################

cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4, hCam)

while True:
    #Step 1: Find the Hand Landmarks
    success, img = cap.read()
    #Step 2: get the tip of index and middle fingers
    #Step 3: Check which fingers is up
    #Step 4: Only Index Finger : Moving mode
    #Step 5: Converting into coordinates
    #Step 6: Smoothen the values
    #Step 7: Moving the mouse using the coordinates
    #Step 8: For Clicking mode check if both index and middle fingers are up
    #Step 9: Find distance between the fingers
    #Step 10: If distance is short, then do the clicking action
    cv2.imshow("Image", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    cv2.waitKey(1)