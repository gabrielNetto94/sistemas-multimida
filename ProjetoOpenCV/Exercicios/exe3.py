#3. Escreva um algoritmo que leia a imagem abaixo, e então clareie somente as regiões mais escuras dela:
from cv2 import cv2
import numpy as np
img = cv2.imread("img1.jpg")

gamma = 0.6

lookUpTable = np.empty((1,256), np.uint8)

for i in range(256):
    lookUpTable[0,i] = np.clip(pow(i / 255.0, gamma) * 255.0, 0, 255)
res = cv2.LUT(img, lookUpTable)

cv2.imshow("img original", img)
cv2.imshow("res", res)
cv2.waitKey(0)