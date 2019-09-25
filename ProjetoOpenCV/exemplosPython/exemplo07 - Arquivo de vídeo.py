import numpy as np
from cv2 import cv2 as cv

#le um arquivo de video
cap = cv.VideoCapture('video.avi')

print (cap)

if not cap.isOpened():
    print("Não foi possível abrir a câmera")
    exit()

#le o primeiro frame para pegar o tamanho do vídeo
ret, frame = cap.read()
h, w, _ = frame.shape
# Define o codec e criamos um objeto VideoWriter para gravar em um arquivo .avi
fourcc = cv.VideoWriter_fourcc(*'DIVX')
out = cv.VideoWriter('output.avi', fourcc, 20.0, (w,  h), True)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Não foi possível ler o frame...")
        break
    cinza = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cinzaInv = cv.flip(cinza, 0) #inverte de cabeça para baixo o frame
    # grava o frame cinza invertido no arquivo
    out.write(cinzaInv)
    cv.imshow('frame', cinzaInv)
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
out.release()
cv.destroyAllWindows()