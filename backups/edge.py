import pyrealsense2 as rs
import sys
import numpy as np
import cv2

np.set_printoptions(threshold=sys.maxsize)

# Configure depth and color streams
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

# Start streaming
pipeline.start(config)
x=0
try:
    while x<16:

        # Wait for a coherent pair of frames: depth and color
        frames = pipeline.wait_for_frames()
        depth_frame = frames.get_depth_frame()
        color_frame = frames.get_color_frame()
        if not depth_frame or not color_frame:
            continue

        # Convert images to numpy arrays
        depth_image = np.asanyarray(depth_frame.get_data())
        color_image = np.asanyarray(color_frame.get_data())

        # Apply colormap on depth image (image must be converted to 8-bit per pixel first)
        depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)

        # Stack both images horizontally
        images = np.hstack((color_image, depth_colormap))
       
        x=x+1
finally:
    row = 500
    col = 480
    depth_array = np.zeros((row,480))
    


    for y in range(480):
        for x in range(row):
            depth_array[x,y] = round(depth_frame.get_distance(x+140,y),3)

    print(depth_array)
    # Stop streaming
    cv2.imwrite('/home/pi/nimble_hub/pictures/foo.jpg',color_image)
    cv2.imwrite('/home/pi/nimble_hub/pictures/depth_array_no_edge.jpg',depth_array*255)
    cv2.imwrite('/home/pi/nimble_hub/pictures/depth.jpg',depth_image)
    
    
    pipeline.stop()
    
    
    err = 0.05
    #row_edges[row]

    for x in range(row):
        valid = 0
        edge1 = -1
        edge2 = -1
        valid_e1 = 1
        valid_e2 = 1
        skip = 10
        for y in range(col-20):
            if(skip>0):
                skip = skip - 1
                continue
            pixel = [None] * 20
            for i in range(20):
                pixel[i] = depth_array[x,y+i]

            if(abs(pixel[0] - pixel[1]) >= err):
                if(valid == 0):
                    for i in range(19):
                        if(abs(pixel[0] - pixel[1+i])< err):
                            valid_e1 = 0
                    if(valid_e1 == 1):
                        edge1 = y
                        valid = 1
                    if(valid_e1 == 0):
                        valid_e1=1
                        skip = 20
                if(valid):
                    for i in range(19):
                        if(abs(pixel[0] - pixel[1+i])< err):
                            valid_e2 = 0
                    if(valid_e2 == 1):
                        edge2 = y
                        valid = 1
                    if(valid_e2 == 0):
                        valid_e2=1
                        skip = 20
        print("Row:" + str(x) + " edge1:"+str(edge1)+" edge2:"+str(edge2))
        depth_array[x,edge1]=255
        depth_array[x,edge2]=255
        #row_edges[x] = (edge1, edge2)

cv2.imwrite('/home/pi/nimble_hub/pictures/depth_array.jpg',depth_array*255)
