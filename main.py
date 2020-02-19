import pyrealsense2 as rs
import sys
import numpy as np
import cv2
import importlib
import objectDetect as obj
import objectDict as oDict


obj.initializeFrames()
obj.imageManip()
shapeList = obj.shapefind(obj.gray_img)
print(shapeList)


    
