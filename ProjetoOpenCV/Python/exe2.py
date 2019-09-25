from cv2 import cv2
import numpy
imgPixelChanged = cv2.imread("windows.jpg")
imgNegative = cv2.imread("windows.jpg")
if imgPixelChanged is None:
    print("Erro ao abrir imagem 1")

else:
    rows = numpy.size(imgPixelChanged, 0)
    cols = numpy.size(imgPixelChanged, 1)
    for i in range(rows):
        for j in range(cols):
            bgrPixel = imgPixelChanged[i,j]
            
            temp = bgrPixel[0]
            bgrPixel[0] = bgrPixel[1]
            bgrPixel[1] = bgrPixel[2]
            bgrPixel[2] = temp

            bgrPixel = imgNegative[i,j]
            bgrPixel[0] = 255 - bgrPixel[0]
            bgrPixel[1] = 255 - bgrPixel[1]
            bgrPixel[2] = 255 - bgrPixel[2]

cv2.imshow("imagem pixel trocado", imgPixelChanged)
cv2.imshow("imagem negativo", imgNegative)
cv2.waitKey(0)