import pyrealsense2 as rs
import sys
import numpy as np
import cv2

img = cv2.imread('/home/pi/nimble_hub/pictures/shapes.png', cv2.IMREAD_GRAYSCALE)
_, threshold = cv2.threshold(img, 245, 255, cv2.THRESH_BINARY)
_, contours ,_ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.imshow("shapes",img)
cv2.imshow("Threshold", threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()

font = cv2.FONT_HERSHEY_COMPLEX


for cnt in contours:
    approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
    x = approx.ravel()[0]
    y = approx.ravel()[1]
    cv2.drawContours(img,[approx],0,(0),3)
    print(len(approx))

    if len(approx) == 3:
        cv2.putText(img,"Triangle",(x,y),font,1,(0))
    
    if len(approx) == 4:
        cv2.putText(img,"Square",(x,y),font,1,(0))
        
    if len(approx) == 5:
        cv2.putText(img,"Pentagon",(x,y),font,1,(0))
        
    if len(approx) == 6:
        cv2.putText(img,"Hexagon",(x,y),font,1,(0))
        
    if len(approx) > 6:
        cv2.putText(img,"Circular-ish",(x,y),font,1,(0))

cv2.imshow("shapes",img)
cv2.imshow("Threshold", threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()