import cv2
from time import sleep
from picamera import PiCamera

camera = PiCamera()
camera.resolution = (1024, 786)
camera.start_preview(fullscreen=False,window=(100,200,300,400))
input(0)
##camera.capture('/home/pi/nimble_hub/pictures/foo.jpg')

