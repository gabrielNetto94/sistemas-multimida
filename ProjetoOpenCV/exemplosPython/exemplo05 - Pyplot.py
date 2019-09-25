import numpy as np
from cv2 import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('WindowsLogo.jpg',0)

#mostra a imagem em uma janela usando matplotlib
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')

#esconde os eixos X e Y
plt.xticks([]), plt.yticks([])

#mostra a imagem
plt.show()

#Espera o usuário pressionar uma tecla por um tempo em milissegundos. Se for passado 0, espera infinitamente.
k = cv.waitKey(0) & 0xFF

if k == 27: #usuário pressionou ESC
    #destrói todas as janelas criadas
    cv.destroyAllWindows()
elif k == ord('s'): #usuário pressionou 's'
    #salva a imagem em um arquivo
    cv.imwrite('WindowsLogoCinza.png',img)
    #destrói todas as janelas criadas
    cv.destroyAllWindows()
