from cv2 import cv2
import numpy as np

def adjust_gamma(image, gamma=1.0):

   invGamma = 1.0 / gamma
   table = np.array([((i / 255.0) ** invGamma) * 255
      for i in np.arange(0, 256)]).astype("uint8")

   return cv2.LUT(image, table)

img = cv2.imread('windows.jpg', 1)

imgCpy = adjust_gamma(img, 2.9)
img = adjust_gamma(img, 0.2)

cv2.imshow("imgCpy", imgCpy)
cv2.imshow('img1',img)

cv2.waitKey(0)
cv2.destroyAllWindows()