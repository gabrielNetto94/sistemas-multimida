import numpy as np
from cv2 import cv2 as cv
img = cv.imread('messi5.jpg')

#acessando um pixel BGR individualmente
px = img[100,100]
print("1 - ", px )

#acessando o AZUL de um pixel:
blue = img[100,100,0]
print("2 - ", blue )

#modificando o valor de um pixel:
img[100,100] = [255,255,255]
print("3 - ", img[100,100] )

#ps: a biblioteca Numpy, utilizada para operações nas imagens, 
# é otimizada para cálculos rápidos em arrays. 
# Portanto, acessar os valores dos píxeis individualmente e 
# modificá-los diretamente pode resultar em uma grande perda de performance.

#Jeito mais apropriado de acessar o valor de um píxel:
red = img.item(10,10,2)
print("4 - ",red)
img.itemset((10,10,2),100)
print("5 - ",img.item(10,10,2))

#Acessamento propriedades da imagem:
print("6 - ", img.shape ) #quantas linhas, colunas e canais de cor
print("7 - ", img.size ) #quantos pixeis a imagem possui
print("8 - ", img.dtype ) #o tipo de imagem

#Acessando regiões de interesse na imagem:
bola = img[280:340, 330:390]
img[273:333, 100:160] = bola

#separando os canais RGB da imagem:
b,g,r = cv.split(img)

#pegando só o canal azul:
b = img[:,:,0]

#juntando os canais RGB em uma imagem:
img = cv.merge((b,g,r))

#setando ZERO para o canal vermelho da imagem:
img[:,:,2] = 0


#cv.imshow('image',img)
#cv.waitKey(0)