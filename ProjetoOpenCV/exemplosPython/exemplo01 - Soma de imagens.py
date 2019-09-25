from cv2 import cv2
import numpy
alpha = 0.5
src1 = cv2.imread("WindowsLogo.jpg")
src2 = cv2.imread("LinuxLogo.jpg")
if src1 is None:
    print("Erro ao abrir imagem 1")

elif src2 is None:
    print("Erro ao abrir a imagem 2")

else:
    beta = 1.0 - alpha
    dst = cv2.addWeighted(src1, alpha, src2, beta, 0.0)
    cv2.imshow("img", dst)
    cv2.waitKey(0)
