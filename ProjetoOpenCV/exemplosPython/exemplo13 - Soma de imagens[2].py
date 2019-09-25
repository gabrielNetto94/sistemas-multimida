import numpy as np
from cv2 import cv2 as cv

#Adicção de imagens
x = np.uint8([250])
y = np.uint8([10])
print("1 - ", cv.add(x,y) ) # adição do opencv faz 250+10 = 260 => 255

print("2 - ", x+y )          # adição do numpy faz 250+10 = 260 % 256 = 4

#Combinação de imagens
#A combinação de imagens, que também é uma adição, leva em consideração pesos para dar uma sensação de transparência, de acordo com a equação:
#dst=α⋅img1+β⋅img2+γ em que α,β e γ varia de 0 a 1
img1 = cv.imread('ml.png')
img2 = cv.imread('opencv-logo.png')
dst = cv.addWeighted(img1,0.7,img2,0.3,0) #os parâmetros são: img1, α, img2, β, γ
cv.imshow('dst',dst)
cv.waitKey(0)
cv.destroyAllWindows()