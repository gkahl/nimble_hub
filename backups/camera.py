import cv2
from time import sleep
from picamera import PiCamera

camera = PiCamera()
camera.resolution = (1024, 768)
##camera.start_preview()
##input(0)
camera.capture('/home/pi/nimble_hub/pictures/foo.jpg')

