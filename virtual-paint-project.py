import cv2
import numpy as np
from util import stackImages

# viewing webcam
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)
cap.set(cv2.CAP_PROP_BRIGHTNESS, 120)

myColors = [[5, 107, 0, 19, 255, 255], #reduced orange to HSV white.
            [133,56,0,159,156,255], #reduced purple to HSV white.
            [57, 76, 0, 100, 255, 255]] # reduced green to HSV white.

# in the format of BGR (NOT RGB)
myColorValues = [[51,153,255], [255, 0, 255], [0, 255, 0]]
myPoints = []

# For multiple colors, pass in the list of color hsv list and color values list, then loop for x and y
def drawOnCanvas(myPoints, colorVal):
    for point in myPoints:
        cv2.circle(imgResult, point, 10, colorVal, cv2.FILLED)

# For multiple colors, pass in the list of color hsv list and color values list, then loop for x and y
def getContours(img, colorVal):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cont in contours:
        area = cv2.contourArea(cont)
        if area > 300:
            cv2.drawContours(imgResult, cont, -1, colorVal, 3)
            perimeter = cv2.arcLength(cont, True)
            # we can play around epsilon for better results
            epsilon = 0.02 * perimeter
            approxCorners = cv2.approxPolyDP(cont, epsilon, True)
            x, y, w, h = cv2.boundingRect(approxCorners)
    return x + w//2, y

# detects color, however it removes the color and forms the white mask so the contours can be easily
# detected. Colors = noise and we remove noise
# For multiple colors, pass in the list of color hsv list and color values list, then loop for x and y
def findColor(image, colorHSV, colorValue):
    imgHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower = np.array(colorHSV[0:3])
    higher = np.array(colorHSV[3:6])
    mask = cv2.inRange(imgHSV, lower, higher)
    x, y = getContours(mask, colorValue)
    cv2.circle(imgResult, (x, y), 10, colorValue, cv2.FILLED)
    return x, y

while True:
    success, img = cap.read()
    imgResult = img.copy()
    green = myColors[2]
    greenVal = myColorValues[2]
    newPoint = findColor(img, green, greenVal)
    myPoints.append(newPoint)
    drawOnCanvas(myPoints, greenVal)
    cv2.imshow("Video", imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break