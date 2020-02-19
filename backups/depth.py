import pyrealsense2 as rs
import cv2
import numpy as np
import time


pipeline = rs.pipeline()

pipeline.start()
time.sleep(0.5)

frames = pipeline.wait_for_frames()
depth = frames.get_depth_frame()
rows, cols = (480,640)
depth_array = [[0]*rows]*cols

#print(depth_array)

for y in range(480):
	for x in range(640):
		depth_array[x][y] = round(depth.get_distance(x,y),2)

print(depth_array)

image = np.asanyarray(depth.get_data())
cv2.imwrite('/home/pi/nimble_hub/pictures/depth_image.jpg',image)
cv2.imshow('depth',image)
