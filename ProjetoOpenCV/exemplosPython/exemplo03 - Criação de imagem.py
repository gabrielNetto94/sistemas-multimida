from cv2 import cv2
import numpy as np
#cria uma imagem de 20x20 com 3 canais, em que todos os valores de rgb são 127
M = np.ones([20, 20, 3], np.uint8)*127
print(M)

#cria uma imagem de 900x800 com 3 canais, em que todos os valores de rgb são aleatórios entre 0 e 255
M2 = np.random.randint(0, 255, size=(900,800,3),dtype=np.uint8)
print(M2)
cv2.imshow("Imagem com cor trocada", M2)
cv2.waitKey(0)