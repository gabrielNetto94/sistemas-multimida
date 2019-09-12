from cv2 import cv2
import numpy
img = numpy.zeros([320, 320], numpy.uint8)
cv2.imshow("test", img)
cv2.waitKey(0)