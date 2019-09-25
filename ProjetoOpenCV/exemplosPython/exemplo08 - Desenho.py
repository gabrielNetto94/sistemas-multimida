import numpy as np
from cv2 import cv2 as cv

# Cria uma imagem colorida com todos os píxeis pretos de 512x512
img = np.zeros((512,512,3), np.uint8)

# Desenha uma diagonal azul com Draw a diagonal blue line with espessura de 5px
cv.line(img,(0,0),(511,511),(255,0,0),5)

#desenha um retângulo verde com 3px de espessura
cv.rectangle(img,(384,0),(510,128),(0,255,0),3)

#desenha um círculo vermelho, com espessura de -1 (circulo preenchido)
cv.circle(img,(447,63), 63, (0,0,255), -1)

#desenha uma elipse preenchida
cv.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

#desenha um polígono
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32) #coordenadas dos vértices do polígono
pts = pts.reshape((-1,1,2))
cv.polylines(img,[pts],True,(0,255,255))

#desenha um texto na imagem
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv.LINE_AA)

cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()