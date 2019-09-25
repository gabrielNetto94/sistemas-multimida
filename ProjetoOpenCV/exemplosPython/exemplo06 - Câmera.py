import numpy as np
from cv2 import cv2 as cv

#cria um objeto VideoCapture, passando por parâmetro qual câmera (geralmente 0, pois só há uma) ou arquivo de vídeo deseja-se abrir
cap = cv.VideoCapture(0)

#testa se não foi possível abrir a câmera
if not cap.isOpened():
    print("Não foi possível abrir a câmera")
    exit()

#a leitura da câmera é feita frame a frame, por isso o laço infinito
while True:
    # Captura o frame
    ret, frame = cap.read()

    # se o frame for lido corretamente, ret é True
    if not ret:
        print("Não foi possível ler o frame...")
        break

    # convertemos o frame para escala de cinza
    cinza = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Mostra o frame resultante da conversão
    cv.imshow('frame', cinza)

    if cv.waitKey(1) == ord('q'): #se o usuário pressionar 'q'
        break

# Quando o usuário finalizar, libera o dispositivo
cap.release()
cv.destroyAllWindows()