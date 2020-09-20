import cv2 #computer vision
import numpy as np
print("Packages imported")

# Resizing images
img = cv2.imread("Resources/impostor.jpg")
print(img.shape)
imgResize = cv2.resize(img, (300, 200))
print(imgResize.shape)
#Cropped image
imgCropped = img[0:200, 200:500]

cv2.imshow("Original image", img)
cv2.imshow("Resized image", imgResize)
cv2.imshow("Cropped image", imgCropped)
cv2.waitKey(0)