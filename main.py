import pyrealsense2 as rs
import sys
import numpy as np
import cv2
import importlib
import objectDetect as obj
import objectDict as oDict
import sys


if len(sys.argv) == 3:
	exposure = sys.argv[1]
	threshold = sys.argv[2]	
print("exposure:" + str(exposure))
print("threshold" + str(threshold))

colorNames=["red","blue"]
shapeNames=["Triangle","Rectangle","Pentagon","Hexagon","Circle"]

obj.initializeFrames(exposure)
obj.imageManip(threshold)
shapeList = obj.shapefind(obj.gray_img)
oDict.makeObjects(shapeList)
