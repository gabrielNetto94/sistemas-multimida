#Faça um algoritmo que leia uma imagem e então aplique uma suavização nos píxeis da mesma.
# A suavização pode ser feita calculando a média do valor de cada píxel com seus pixeis vizinhos.
from cv2 import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('opencv-logo.png')

kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)

cv2.imshow("img original",img)
cv2.imshow("suavizacao",dst)
cv2.waitKey(0)