import pyrealsense2 as rs
import sys
import numpy as np
import cv2

font = cv2.FONT_HERSHEY_COMPLEX


np.set_printoptions(threshold=sys.maxsize)

# Configure depth and color streams
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

# Start streaming
pipeline.start(config)

x=0

# Align the depth and color frames
align_to = rs.stream.color
align = rs.align(align_to)

try:
    while x<16:

        # Wait for a coherent pair of frames: depth and color
        frames = pipeline.wait_for_frames()
        
        aligned_frames = align.process(frames)
        
        depth_frame = aligned_frames.get_depth_frame()
        
        color_frame = aligned_frames.get_color_frame()
        if not depth_frame or not color_frame:
            continue

        #Post-Processing
        colorizer = rs.colorizer()
        spatial = rs.spatial_filter()

        
        filtered_depth = spatial.process(depth_frame)
                        
        # Convert images to numpy arrays
        bw_filtered = np.asanyarray(filtered_depth.get_data())
        filtered_image = np.asanyarray(colorizer.colorize(filtered_depth).get_data())
        gray = cv2.cvtColor(filtered_image,cv2.COLOR_BGR2GRAY)
        depth_image = np.asanyarray(depth_frame.get_data())
        color_image = np.asanyarray(color_frame.get_data())

        # Apply colormap on depth image (image must be converted to 8-bit per pixel first)
        depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)

        # Stack both images horizontally
        images = np.hstack((color_image, depth_colormap))
       
        x=x+1
finally:
    
    x = 640
    y = 480
    depth_array = np.zeros((x,y))
    for j in range(x):
        for k in range(y):
            depth_array[j,k] = round(depth_frame.get_distance(j,k),3)

    #filtered_image = filtered_image[5:475, 160:630]
    # Stop screaming
    # Writing the output images
    cv2.imwrite('/home/pi/nimble_hub/pictures/outputs/gray.jpg',gray)
    cv2.imwrite('/home/pi/nimble_hub/pictures/outputs/filtered.jpg',filtered_image)
    cv2.imwrite('/home/pi/nimble_hub/pictures/outputs/color_image.jpg',color_image)
    cv2.imwrite('/home/pi/nimble_hub/pictures/outputs/depth_array_no_edge.jpg',depth_image*255)
    cv2.imwrite('/home/pi/nimble_hub/pictures/outputs/depth.jpg',depth_image)

    
    pipeline.stop()
    
    # Running Canny Edge Detection and Ouputting the Results to Output Directory
    bw_filtered = bw_filtered*255
    bw_filtered = np.uint8(bw_filtered)
    cv2.imwrite('/home/pi/nimble_hub/pictures/oputputs/bw_filtered.jpg',gray)

    # Tried doing it on the color image
    gray_img = cv2.cvtColor(color_image,cv2.COLOR_BGR2GRAY)
    cv2.imwrite('/home/pi/nimble_hub/pictures/outputs/color_bw.jpg',gray_img)
    thresh = 100
    bw_img = cv2.threshold(gray_img, thresh, 255, cv2.THRESH_BINARY)[1]
    cv2.imwrite('/home/pi/nimble_hub/pictures/outputs/bw.jpg',bw_img)
    
    edges = cv2.Canny(gray_img,100,250)
    cv2.imwrite('/home/pi/nimble_hub/pictures/outputs/uncanny.jpg',edges)
    
        
    
    
    # Find the contours using the Canny Edges image
    _, contours, _= cv2.findContours(bw_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    

    # Calculate the Average Distance of the background from the camera
    corner1= 0
    corner2= 0
    corner3= 0
    corner4= 0
    i= 0
    j= 0
    k= 0
    l = 0

    while corner1 == 0:
        corner1 = depth_frame.get_distance(10+i,10+i)
        i=i+1
    while corner2 == 0:
        corner2 = depth_frame.get_distance(630-j,10+j)
        j=j+1
    while corner3 == 0:
        corner3 = depth_frame.get_distance(10+k,470-k)
        k=k+1
    while corner4 == 0:
        corner4 = depth_frame.get_distance(630-l,470-l)
        l=l+1
    bHeight = (corner1+corner2+corner3+corner4) / 4
    
#shape func start
    # Determine the Shape Maybe
    for cnt in contours:
        approx = cv2.approxPolyDP(cnt, 0.02*cv2.arcLength(cnt,True),True)
        cv2.drawContours(gray_img, [approx], 0,(0),2)
        x = approx.ravel()[0]
        y = approx.ravel()[1]
        if len(cnt)>30:
            #Finding the Area of each shape
            area = cv2.contourArea(cnt)
            
            #Finding the Center point of each shape to get the height value
            M=cv2.moments(cnt)
            if M["m00"] > 0:
                cX = int(M["m10"]/M["m00"])
                cY = int(M["m01"]/M["m00"])
            
            cHeight = 0
            i=0
            while cHeight == 0:
                cHeight = depth_frame.get_distance(cX+i,cY)
                i=i+1
            height = bHeight - cHeight
            vol = area*height
            if (len(approx) == 3 ):
                cv2.putText(color_image,"Triangle",(x,y),font,1,(0))
                print('Triangle of area '+ str(area) + " detected")
                print('Triangle is ' + str(height) + ' meters tall')
                print('Volume of: ' + str(vol) + " pixels^2 * meters")

                
            if (len(approx) == 4 ):
                cv2.putText(color_image,"Square",(x,y),font,1,(0))
                print('Square of area '+ str(area) + " detected")
                print('Square is ' + str(height) + ' meters tall')
                print('Volume of: ' + str(vol) + " pixels^2 * meters")
                
            if (len(approx) == 5 ):
                cv2.putText(color_image,"Pentagon",(x,y),font,1,(0))
                print('Pentagon of area '+ str(area) + " detected")
                print('Pentagon is ' + str(height) + ' meters tall')
                print('Volume of: ' + str(vol) + " pixels^2 * meters")

                
            if (len(approx) == 6 ):
                cv2.putText(color_image,"Hexagon",(x,y),font,1,(0))
                print('Hexagon of area '+ str(area) + " detected")
                print('Hexagon is ' + str(height) + ' meters tall')
                print('Volume of: ' + str(vol) + " pixels^2 * meters")
               
            if (len(approx) > 6 ):
                cv2.putText(color_image,"Circle",(x,y),font,1,(0))
                print('Circle of area '+ str(area) + " detected")
                print('Circle is ' + str(height) + ' meters tall')
                print('Volume of: ' + str(vol) + " pixels^2 * meters")
            print()

    
        


    cv2.imwrite('/home/pi/nimble_hub/pictures/outputs/approx.jpg',bw_img)   
    
    cv2.drawContours(color_image, contours, -1, (0,255,0), 3)
    cv2.imwrite('/home/pi/nimble_hub/pictures/outputs/countours2.jpg',color_image)
    
