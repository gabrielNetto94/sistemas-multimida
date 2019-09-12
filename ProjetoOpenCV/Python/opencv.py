from cv2 import cv2
import numpy
img = cv2.imread("img.jpg")
cv2.imshow("img",img)
cv2.waitKey(0)