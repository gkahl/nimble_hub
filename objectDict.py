import pyrealsense2 as rs
import sys
import numpy as np
import cv2

#Attributes
#Area. Height. Volume. Color. Shape. Name. Barcode. Description.
colorNames=["red","blue"]
shapeNames=["Triangle","Rectangle","Pentagon","Hexagon","Circle"]
class myClass:
    def __init__(self,name,height,volume,area,color,colorName,shape,barcode,description):
        self.name = ""
        self.height = height
        self.volume = volume
        self.area = area
        self.color = color
        self.colorName = ""
        self.shape = shape
        self.barcode = barcode
        self.description= ""
        
    def ifNew(self):
        self.name = input("Write the name of the Object:\n")
        self.description= input("Write a short description of the object:\n")
        
    def ifOld(self,name,description):
        self.name = name
        self.description = description
        
    



    
    
    


