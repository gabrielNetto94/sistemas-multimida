from cv2 import cv2
    import numpy as np

alpha = 0.5
beta = (1.0 - alpha)

#images
linux = cv2.imread("linux.jpg")
windows = cv2.imread("windows.jpg")

#img = linux + windows
#img = cv2.add(linux,windows)
img = cv2.addWeighted(linux, 0.4,windows,0.4,0)

width = img.shape[1]
height = img.shape[0]

#for i in range(width):
#    for j in range(height):
        

        
print("width = ",width ,"height = ",height)


#cv2.imshow('img',img)
cv2.waitKey(0)


#VIDEO CAPTURE
'''
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    
    cv2.imshow('frame',frame)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
'''