#zbar-py and opencv_python
import numpy as np
import cv2
import zbar
import sys


<<<<<<< HEAD
if len(sys.argv) > 1:
    path = ('/home/greg/nimble_hub/pictures/' + sys.argv[1])
else:
    path = '/home/greg/nimble_hub/pictures/foo.jpg'

img = cv2.imread(path, 0)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

scanner = zbar.Scanner()
results = scanner.scan(img)
for result in results:
    xval, yval = list(zip(*result.position))
    
    count = 1
    
    for i in range(len(yval)):
        if ((len(yval) - i) > 6):

            if ((yval[i] != yval[i+1]) and (yval[i+1] == yval[i+2])):
                if (yval[i+3] != yval[i+2] and yval[i+3] == yval[i+4] and yval[i+3] == yval[i+5] and yval[i+3] == yval[i+6]):
                    count = count+1
            if yval[i+1] > yval[i] + 2:
                count = count + 1
    print(result.type, result.data, result.quality,'Count:', count)
        
        
