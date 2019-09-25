from cv2 import cv2
import numpy
src = cv2.imread("LinuxLogo.jpg")
if src is None:
    print("Erro ao abrir imagem")

else:
    copia = src.copy()
    cv2.imshow("img", copia)
    cv2.waitKey(0)
