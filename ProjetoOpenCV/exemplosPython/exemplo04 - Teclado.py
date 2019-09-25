import numpy as np
from cv2 import cv2 as cv

#lê uma imagem em tons de cinza
#o segundo parâmetro pode ter os seguintes valores:
#cv.IMREAD_COLOR ou 1 : Lê uma imagem colorida, sem alpha/transparência. É o default
#cv.IMREAD_GRAYSCALE ou 0 : Lê uma imagem em tons de cinza.
#cv.IMREAD_UNCHANGED ou 1: Lê uma imagem incluindo o alpha/transparência.
img = cv.imread('WindowsLogo.jpg',0)

#mostra a imagem em uma janela
cv.imshow('image',img)

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
