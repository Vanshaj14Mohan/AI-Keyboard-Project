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
    cv2.imshow("Image", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    cv2.waitKey(1)