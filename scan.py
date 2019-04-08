#zbar-py and opencv_python
import numpy as np
import cv2
import zbar


img = cv2.imread('/home/pi/nimble_hub/pictures/foo.jpg', 0)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

scanner = zbar.Scanner()
results = scanner.scan(img)
for result in results:
	print(result.type, result.data, result.quality, result.position)

