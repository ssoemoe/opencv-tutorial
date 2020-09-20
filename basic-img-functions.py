import cv2 #computer vision
import numpy as np
print("Packages imported")

# Basic functions
img = cv2.imread("Resources/impostor.jpg")
kernel = np.ones((5,5), np.uint8,)
# Grayscale 0 - 255 level, 8 bit
# convention is BGR to GRAY
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Blurring
# ksize must be odd numbers ex: 7 x 7
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0)
# Canny
imgCanny = cv2.Canny(img, 100, 100)
#Dilation
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
#Erosion
imgEroded = cv2.erode(imgDilation, kernel, iterations=1)
cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blurry Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dilation Image", imgDilation)
cv2.imshow("Erosion Image", imgEroded)
cv2.waitKey(0)
