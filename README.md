# Nimble Hub Image Recognition

### Members:
- Holden Crochiere
- Greg Kahl
- Jonathan Ntale
- Sophia Martinez


Currently, `scan.py` opens an image into a numpy array using OpenCV. This image is fed to zbar which identifies the 1D and 2D barcodes in the image and returns their type, the data within them, and their clarity.
This is achieved using the opencv_python and zbar-py python modules
