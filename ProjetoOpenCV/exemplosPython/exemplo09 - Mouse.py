import numpy as np
from cv2 import cv2 as cv

# função callback para tratar o mouse
def draw_circle(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDBLCLK: #se o usuário deu doubleclick com o botão esquerdo
        cv.circle(img,(x,y),100,(255,0,0),-1) #desenha um círculo na posição do mouse

#Criação de uma imagem preta, uma janela e definição da função callback do mouse para a janela criada
img = np.zeros((512,512,3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image',draw_circle)
while(1):
    cv.imshow('image',img)
    if cv.waitKey(20) & 0xFF == 27:
        break
cv.destroyAllWindows()