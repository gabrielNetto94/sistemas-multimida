import numpy as np
from cv2 import cv2 as cv

def nada(x):
    pass

#criação de uma imagem preta e de uma janela
img = np.zeros((300,512,3), np.uint8)
cv.namedWindow('image')

#criação das trackbar para troca de cor. O último parâmetro é uma função que executa toda vez que algo muda
cv.createTrackbar('R','image',0,255,nada)
cv.createTrackbar('G','image',0,255,nada)
cv.createTrackbar('B','image',0,255,nada)

# criação de um "interruptor" que liga e desliga a funcionalidade
switch = '0 : OFF \n1 : ON'
cv.createTrackbar(switch, 'image',0,1,nada)
while(1):
    cv.imshow('image',img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
    # pega a posição atual das quatro trackbar
    r = cv.getTrackbarPos('R','image')
    g = cv.getTrackbarPos('G','image')
    b = cv.getTrackbarPos('B','image')
    s = cv.getTrackbarPos(switch,'image')
    if s == 0:
        img[:] = 0 #seta a imagem toda preta
    else:
        img[:] = [b,g,r] #seta a cor como sendo o rgb das trackbar
cv.destroyAllWindows()