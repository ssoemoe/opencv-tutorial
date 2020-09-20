# Joining images
import cv2
import numpy as np
from util import stackImages

img = cv2.imread("Resources/impostor.jpg")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgStack = stackImages(0.5, ([img, imgGray, img], [img, imgGray, img]))
imgHorizontal = np.hstack((img, img))
imgVertical = np.vstack((img, img))
# cv2.imshow("Horizontal", imgHorizontal)
# cv2.imshow("Vertical", imgVertical)
cv2.imshow("Image stack", imgStack)
cv2.waitKey(0)