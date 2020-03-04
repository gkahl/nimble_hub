# Nimble Hub Object Recognition

## About
Nimble Hub Object Recognition System is designed to be run on a Raspberry Pi using an Intel Real Sense Camera. It polls an image from the Intel Real Sense camera. The depth and color images are run through filters and analyzed to detect objects and log object statistics/count the number of times it has seen the object.


## Contributors:
- Holden Crochiere
- Greg Kahl
- Jonathan Ntale
- Sophia Martinez

## Features
### Shape Detection
Using OpenCV NHORS determines the shape of the objects detected by counting the number of sides/corners each of the blobs has. The number of sides is translated into the type of shape that has been found.

### Color Detection
Using the color image and the borders of each object detected, the average HSV color value is determined for the object.

### Area/Volume Detection
Using the depth value for both the top face of the object and the background a height, in centimeters is determined for the object. Next, by using our pixel to square centimeter conversion formula, which was determined through regression, we translate the area of the top face of the object in pixels to square centimeters depeinding on how far away it is from the camera. Using both the height of the object and the area of the top face we are able to determine the volume. 

### Counting
When a new object is detected, we compare its statistics to all the existing objects in our log. If the statistics match, the count for the old object is incremented. If the object is new, the user is asked to input a name and short description and a new entry is added to the log. There is functionality for the user to reset the count of the object in the log. 

## Usage
In order to use N.H.O.R.S. you must install the numpy package,OpenCV 2,and the pyrealsense2 package.

In order to install numpy run the cli command: `pip3 install numpy --user`

To install OpenCV run: `pip3 install opencv-python --user`

To install the pyrealsense2 package locate the `librealsense2.so` and `pyrealsensse2.cpython-35m-arm-linux-gnueabihf.so` files online and copy them to the nimble_hub folder
