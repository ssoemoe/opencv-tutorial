# First real-time detection method was done by Viola and Jones
import cv2
import numpy as np

faceCascade = cv2.CascadeClassifier("Resources/haarcascades/haarcascade_frontalface_default.xml")
img = cv2.imread('Resources/lena.png')

cv2.imshow("Result", img)
cv2.waitKey(0)