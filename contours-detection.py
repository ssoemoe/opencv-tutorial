# CONTROURS / SHAPE DETECTION
import cv2
import numpy as np
from util import stackImages

def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cont in contours:
        area = cv2.contourArea(cont)
        if area > 5500:
            cv2.drawContours(resultImg, cont, -1, (255, 0, 0), 3)
            perimeter = cv2.arcLength(cont, True)
            # we can play around epsilon for better results
            epsilon = 0.02 * perimeter
            approxCorners = cv2.approxPolyDP(cont, epsilon, True)
            approxNumCorners = len(approxCorners)
            x, y, w, h = cv2.boundingRect(approxCorners)
            shapeType = "N/A"
            if approxNumCorners == 3:
                shapeType = "Tri"
            elif approxNumCorners == 4:
                aspectRatio = w / float(h)
                if aspectRatio > 0.95 and aspectRatio < 1.05:
                    shapeType = "Square"
                else:
                    shapeType = "Rectangle"
            elif approxNumCorners > 4:
                shapeType = "Circle"
            print(shapeType)
            cv2.rectangle(resultImg, (x, y), (x + w, y + h), (255, 255, 255), 3)
            cv2.putText(resultImg, shapeType, (x + (w//2)-10, y+(h//2)-10), cv2.FONT_HERSHEY_COMPLEX,
                        0.7, (125,255,255),2)

path = "Resources/shapes.png"
img = cv2.imread(path)
resultImg = np.zeros_like(img)

# First step - convert it to grayscale image
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Second step - blur the gray image
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 1)

# Third step - image canny
imgCanny = cv2.Canny(imgBlur, 50, 50)
getContours(imgCanny)

# Optional - stack images, so we do not need to open multiple windows
imgStack = stackImages(0.8, ([imgGray, imgBlur], [imgCanny, resultImg]))

cv2.imshow("Result", imgStack)
cv2.waitKey(0)
