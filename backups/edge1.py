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
    

    #print(depth_array)
    # Stop streaming
    cv2.imwrite('/home/pi/nimble_hub/pictures/foo.jpg',color_image)
    cv2.imwrite('/home/pi/nimble_hub/pictures/depth_array_no_edge.jpg',depth_array*255)
    cv2.imwrite('/home/pi/nimble_hub/pictures/depth.jpg',depth_image)
    edge_list= [None] * 500
    edge_list2= [None] * 480
    
    pipeline.stop()
    
    #Edge detection
    err = 0.03
    #row_edges[row]

    for x in range(row):
        valid = 0
        edge1 = -1
        edge2 = -1
        valid_e1 = 1
        valid_ez1 = 0
        valid_ez2 = 0
        valid_e2 = 1
        skip = 10
        for y in range(col-40):
            if(skip>0):
                skip = skip - 1
                continue
            pixel = [None] * 40
            for i in range(40):
                pixel[i] = depth_array[x,y+i]
            if(abs(pixel[0] - pixel[1]) >= err):
                if(valid == 0):
                    for i in range(39):
                        if(abs(pixel[0] - pixel[1+i])< err):
                            valid_e1 = 0
                        if(pixel[1+i] > 0.005):
                            valid_ez1 = 1
                    if(valid_e1 == 1 and valid_ez1 == 1):
                        edge1 = y
                        valid = 1
                    if(valid_e1 == 0):
                        valid_e1=1
                        skip = 40
                    if(valid_ez1 == 0):
                        skip = 40
                if(valid):
                    for i in range(39):
                        if(abs(pixel[0] - pixel[1+i])< err):
                            valid_e2 = 0
                       # if(pixel[1+i] > 0.005):
                           # valid_ez2 = 0
                    if(valid_e2 == 1 and y-edge1 > 50):
                        edge2 = y
                        valid = 1
                    if(valid_e2 == 0):
                        valid_e2=1
                        skip = 40
                    #if(valid_ez2 == 0):
                    #    skip = 40
        #print("Row:" + str(x) + " edge1:"+str(edge1)+" edge2:"+str(edge2))
        depth_array[x,edge1]=255
        depth_array[x,edge2]=255
        edge_list[x] = (edge1,edge2)
        #row_edges[x] = (edge1, edge2)
        
    #vertical scan
    for y in range(col):
        valid = 0
        edge1 = -1
        edge2 = -1
        valid_e1 = 1
        valid_ez1 = 0
        valid_ez2 = 0
        valid_e2 = 1
        skip = 10
        for x in range(row-100):
            if(skip>0):
                skip = skip - 1
                continue
            pixel = [None] * 100
            for i in range(100):
                pixel[i] = depth_array[x+i,y]
            if(abs(pixel[0] - pixel[1]) >= err):
                if(valid == 0):
                    for i in range(99):
                        if(abs(pixel[0] - pixel[1+i])< err):
                            valid_e1 = 0
                        if(pixel[1+i] > 0.01):
                            valid_ez1 = 1
                    if(valid_e1 == 1 and valid_ez1 == 1):
                        edge1 = x
                        valid = 1
                        skip=200
                    if(valid_e1 == 0):
                        valid_e1=1
                        skip = 100
                    if(valid_ez1 == 0):
                        skip = 100
                if(valid):
                    for i in range(99):
                        if(abs(pixel[0] - pixel[1+i])< err):
                            valid_e2 = 0
                        if(pixel[1+i] > 0.01):
                            valid_ez2 = 1
                    if(valid_e2 == 1 and valid_ez2 == 1 and abs(edge2-y) > 50):
                        edge2 = x
                        valid = 1
                    if(valid_e2 == 0):
                        valid_e2=1
                        skip = 100
                    if(valid_ez2 == 0):
                        skip = 100
        #print("Row:" + str(x) + " edge1:"+str(edge1)+" edge2:"+str(edge2))
        depth_array[edge1,y]=255
        depth_array[edge2,y]=255
        edge_list2[y] = (edge1,edge2)
        
        
#Corner Detection
        #for edge in range(len(edge_list)):
        #    if(edge_list[edge][0]!=-1):
        #        print(edge_list[edge][0])
corner_list = [None] * 8
corners_detected = 0
corner_valid = 0
pot_check = 0
error_skip = 0
potential_corner = None
for x in range(len(edge_list)-1):
    if(edge_list[x][0]!=-1 or corner_valid >=10):
        if(corner_valid < 10):
            if((abs(edge_list[x][0] - edge_list[x+1][0]) <= 5)):
                corner_valid = corner_valid+1
                if(corner_valid == 10):
                    print(x)
                    corner_list[corners_detected]=(x-9,edge_list[x-9][0])
                    corners_detected = corners_detected +1
            else:
                corner_valid = 0
        if(corner_valid>=10 and corner_valid<20):
            if((abs(edge_list[x][0] - edge_list[x+1][0]) >= 5)and pot_check == 0):
                potential_corner = (x,edge_list[x][0])
                pot_check = 1
            #if(pot_check >= 1 and abs(potential_corner[1]-edge_list[x+1][0])>=5 and abs(potential_corner[1]-edge_list[potential_corner[0]-corner_valid-9][0])<=5):
            if(pot_check == 1 and abs(potential_corner[1]-edge_list[x+1][0])>=5):
                corner_valid = corner_valid+1
                if(corner_valid == 20):
                    print(x)
                    corner_list[corners_detected]=potential_corner
                    corners_detected = corners_detected +1
            else:
                if(error_skip == 0):
                    error_skip = 1
                if(error_skip == 1):
                    corner_valid = 10
                    potential_corner = None
                    pot_check = 0
                    error_skip = 0
corner_valid = 0
pot_check = 0
potential_corner = None
for x in range(len(edge_list)-1):
    if(edge_list[x][1]!=-1 or corner_valid >=10):
        if(corner_valid < 10):
            if((abs(edge_list[x][1] - edge_list[x+1][1]) <= 5)):
                corner_valid = corner_valid+1
                if(corner_valid == 10):
                    print(x)
                    corner_list[corners_detected]=(x-9,edge_list[x-9][1])
                    corners_detected = corners_detected +1
            else:
                corner_valid = 0
        if(corner_valid>=10 and corner_valid<20):
            if((abs(edge_list[x][1] - edge_list[x+1][1]) >= 5)and pot_check == 0):
                potential_corner = (x,edge_list[x][1])
                pot_check = 1
            #if(pot_check >= 1 and abs(potential_corner[1]-edge_list[x+1][0])>=5 and abs(potential_corner[1]-edge_list[potential_corner[0]-corner_valid-9][0])<=5):
            if(pot_check == 1 and abs(potential_corner[1]-edge_list[x+1][1])>=5):
                corner_valid = corner_valid+1
                if(corner_valid == 20):
                    print(x)
                    corner_list[corners_detected]=potential_corner
                    corners_detected = corners_detected +1
            else:
                corner_valid = 10
                potential_corner = None
                pot_check = 0
print("This is the corner list:")
print(corner_list)

#Check if two of the corners are near each other
for corner in range(corners_detected):
    for corner2 in range(corners_detected):
        if(corner!=corner2):
            if(abs(corner_list[corner][0]-corner_list[corner2][0])<10 and abs(corner_list[corner][1]-corner_list[corner2][1])<10):
                print(corner_list[corner])
                print(corner_list[corner2])
for i in range(corners_detected):
        for pixelx in range(10):
            for pixely in range(10):
                depth_array[corner_list[i][0]-5+pixelx,corner_list[i][1]] = 255
                depth_array[corner_list[i][0],corner_list[i][1]-5+pixely] = 255
if(corners_detected == 4):
    print("Cube Detected")
if(corners_detected == 3):
    print("Triangle Detected")
if(corners_detected == 0):
    print("Circle Detected")
    
    #height detection
h_avg = 0
h_avgr = 0
for x in range(len(edge_list)-1):
    ledge = edge_list[x][0]
    h_avg = h_avg + abs(depth_array[x,ledge] - depth_array[x,ledge-1])
    h_avgr = h_avgr+1
h_avg = h_avg/h_avgr
print("height in meters: ")
print(h_avg)
    
cv2.imwrite('/home/pi/nimble_hub/pictures/depth_array.jpg',depth_array*255)
#print(edge_list)
#depth_array = np.zeros((row,480))
color_average1 = 0
color_to_add1 = 0
color_average2 = 0
color_to_add2 = 0
color_average3 = 0
color_to_add3 = 0
color_averager=1
for x in range(row-20):
    if(edge_list[x][0] == -1 or edge_list[x][1] == -1):
       continue
    else:
        ranger = edge_list[x][0]
        while (ranger < edge_list[x][1]):
            #print(color_image[x,ranger][0])
            color_to_add1 = color_image[ranger,x+140][0]
            color_average1 = (color_average1 + color_to_add1)
            #
            color_to_add2 = color_image[ranger,x+140][1]
            color_average2 = (color_average2 + color_to_add2)
            #
            color_to_add3 = color_image[ranger,x+140][2]
            color_average3 = (color_average3 + color_to_add3)
            #
            depth_array[x,ranger]=255
            color_image[ranger,x+140][0]=255
            color_image[ranger,x+140][1]=255
            color_image[ranger,x+140][2]=255
            
            color_averager = color_averager+1
            ranger = ranger+1
color_average1 = color_average1/color_averager
color_average2 = color_average2/color_averager
color_average3 = color_average3/color_averager
color_average1 = round(color_average1,2)
color_average2 = round(color_average2,2)
color_average3 = round(color_average3,2)
color_total = (color_average1,color_average2,color_average3)
print("R,G,B Color:")
print(color_total)
cv2.imwrite('/home/pi/nimble_hub/pictures/color_scanned.jpg',color_image)
cv2.imwrite('/home/pi/nimble_hub/pictures/depth_array_scanned_color.jpg',depth_array*255)
