from cv2 import cv2
import numpy
src = cv2.imread("WindowsLogo.jpg")
if src is None:
    print("Erro ao abrir imagem 1")

else:
    rows = numpy.size(src, 0)
    cols = numpy.size(src, 1)
    for i in range(rows):
        for j in range(cols):
            bgrPixel = src[i,j]
            bgrPixel[0] = 255
            bgrPixel[1] = 0
            bgrPixel[2] = 0

    cv2.imshow("Imagem com cor trocada", src)
    cv2.imwrite("azul.jpg", src)
    cv2.waitKey(0)