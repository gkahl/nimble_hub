import pyrealsense2 as rs
import sys
import numpy as np
import cv2


colorNames=["red","blue"]
shapeNames=["Triangle","Rectangle","Pentagon","Hexagon","Circle"]


#Attributes
#Area. Height. Volume. Color. Shape. Name. Barcode. Description.

class foundObj:
    def __init__(self,height,volume,area,color,shape,name="",description="",count=0):
        self.name = name
        self.height = height
        self.volume = volume
        self.area = area
        self.color = color
        self.colorName = ""
        self.shape = shape
        self.count = count+1
        self.barcode = ""
        self.description= description
        
        # Check whether the object is new or old
    def writeToLog(self):
        log = open("/home/pi/nimble_hub/outputs/log.txt", "a")
        log.write(str(self.name) + "|" + str(self.height)+ "|" + str(self.volume)+ "|" + str(self.area)+ "|" + str(self.color[0]) + "|" + str(self.shape)+ "|" + str(self.description)+ "|" + str(self.count)+"\n")
        log.close()
                   
        
    def ifNew(self):
        self.name = input("Write the name of the Object:\n")
        self.description= input("Write a short description of the object:\n")
        self.writeToLog()
        
        
    def resetCount(self):
        self.count = 0
        log = open("/home/pi/nimble_hub/outputs/log.txt","r")
        lines = log.readlines()
        for i in range(0,len(lines)):
            if lines[i].contains(self.name):
                split=lines[i].split("|")
                lines[i] = str(split[0]+"|"+ split[1]+"|"+split[2]+"|"+split[3]+"|"+split[4]+"|"+split[5]+"|"+split[6]+"|"+str(0))
        
        log = open("/home/pi/nimble_hub/outputs/log.txt","w")
        log.writelines(lines)
        log.close() 
    
    def updateCount(self,count):
        log = open("/home/pi/nimble_hub/outputs/log.txt","r")
        lines = log.readlines()
        for i in range(0,len(lines)):
            split=lines[i].split("|")
            if split[0] == self.name:
                lines[i] = str(split[0]+"|"+ split[1]+"|"+split[2]+"|"+split[3]+"|"+split[4]+"|"+split[5]+"|"+split[6]+"|"+str(int(count))+"\n")
        log = open("/home/pi/nimble_hub/outputs/log.txt","w")
        log.writelines(lines)
        log.close()

def makeObjects(shapeList):
    count = 0
    log = open("outputs/log.txt","r")
    lines = log.readlines()


    for obj in shapeList:
        same = -1
        lineCount = 0
        for line in lines:
            splits = line.split("|")

            # Comparing Height
            if(abs(float(splits[1])-obj[0])>1):
                lineCount = lineCount+1
                continue
            # Comparing Volume
            elif(abs(float(splits[2])-obj[1])>3):
                lineCount = lineCount+1
                continue
            # Comparing Area
            elif(abs(float(splits[3]) -obj[2])> 3):
                lineCount = lineCount+1
                continue
            # Comparing Color
            elif(abs(float(splits[4]) -obj[3][0])>15):
                lineCount = lineCount+1
                continue
            # Comparing Shape
            elif(float(splits[5])!=obj[4]):
                if(not((float(splits[5]) > 6) and (obj[4] > 6))):
                        lineCount = lineCount+1
                        continue
            else:
                same = lineCount
                break  

        if (same >=0):
            logObject = lines[lineCount].split("|")

            objectToEnter = foundObj(obj[0],obj[1],obj[2],obj[3],obj[4],logObject[0],logObject[6],int(logObject[7]))
            objectToEnter.updateCount(objectToEnter.count)

    
        if (same == -1):
            objectToEnter = foundObj(obj[0],obj[1],obj[2],obj[3],obj[4])
            objectToEnter.ifNew()
        print(objectToEnter.name)
        print(objectToEnter.height)
        print(objectToEnter.volume)
        print(objectToEnter.area)
        print(objectToEnter.color)
        print(shapeNames[objectToEnter.shape])
        print(objectToEnter.count)
        count=count+1


def zero(name):

    count = 0
    log = open("/home/pi/nimble_hub/outputs/log.txt","r")
    lines = log.readlines()
    for i in range(0,len(lines)):
        if name+"|" in lines[i]:
            split=lines[i].split("|")
            lines[i] = str(split[0]+"|"+ split[1]+"|"+split[2]+"|"+split[3]+"|"+split[4]+"|"+split[5]+"|"+split[6]+"|"+"0\n")
        
    log = open("/home/pi/nimble_hub/outputs/log.txt","w")
    log.writelines(lines)
    log.close() 
