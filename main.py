import pyrealsense2 as rs
import sys
import numpy as np
import cv2
import importlib
import objectDetect as obj
import objectDict as oDict

colorNames=["red","blue"]
shapeNames=["Triangle","Rectangle","Pentagon","Hexagon","Circle"]


obj.initializeFrames()
obj.imageManip()
shapeList = obj.shapefind(obj.gray_img)
#print(shapeList)
oDict.makeObjects(shapeList)





