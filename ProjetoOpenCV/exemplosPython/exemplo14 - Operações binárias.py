import numpy as np
from cv2 import cv2 as cv

#ler https://www.geeksforgeeks.org/arithmetic-operations-on-images-using-opencv-set-2-bitwise-operations-on-binary-images/

#Operações binárias
img1 = cv.imread('messi5.jpg')
img2 = cv.imread('opencv-logo-white.png')
# Criação de uma reigão de interesse que começa no canto superior esquerdo da img1 e tem o tamanho da img2
rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols ]
# Converte a imagem 2 em escala de cinza
img2gray = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
cv.imshow('1 - Imagem 2 em escalas de cinza',img2gray)

# Cria-se uma máscara do logo com a operação de threshold binária, 
# ou seja, todo píxel com valor acima de 10 vira 255 (branco), se não vira 0
ret, mask = cv.threshold(img2gray, 10, 255, cv.THRESH_BINARY)
cv.imshow('2 - Máscara da logo',mask)

#e então invertemos as cores da máscara com a operação binária NOT
mask_inv = cv.bitwise_not(mask)
cv.imshow('3 - Máscara da logo invertida',mask_inv)

# Realiza-se uma operação AND para "colar" o logo em cima da imagem do messi
img1_bg = cv.bitwise_and(roi,roi,mask = mask_inv)
cv.imshow('4 - AND',img1_bg)

# Take only region of logo from logo image.
img2_fg = cv.bitwise_and(img2,img2,mask = mask)
cv.imshow('5 - AND',img2_fg)


# Coloca o logo na reigão de interesse 
dst = cv.add(img1_bg,img2_fg)
cv.imshow('6 - ADD',img2_fg)

#e modifica a imagem principal
img1[0:rows, 0:cols ] = dst
cv.imshow('7 - Resultado',img1)
cv.waitKey(0)
cv.destroyAllWindows()