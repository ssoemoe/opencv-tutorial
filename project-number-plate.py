import cv2
import imutils
import numpy as np
from util import stackImages
####################################
widthImg = 600
heightImg = 600
MIN_AREA = 100
###################################
# viewing webcam
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, widthImg)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, heightImg)
cap.set(cv2.CAP_PROP_BRIGHTNESS, 120)
while True:
    success, img = cap.read()
    resultImg = img.copy();
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0)
    imgCanny = cv2.Canny(imgBlur, 100, 100)
    contours = cv2.findContours(imgCanny, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
    numberPlateContour = None
    for cont in contours:
        perimeter = cv2.arcLength(cont, True)
        approx = cv2.approxPolyDP(cont, 0.018 * perimeter, True)
        if len(approx) == 4:
            cv2.drawContours(resultImg, cont, -1, (255, 0, 0), 3)
            numberPlateContour = cont
            break
    cv2.drawContours(resultImg, numberPlateContour, -1, (255, 0, 0), 3)
    result = stackImages(0.5, ([img, resultImg], [imgBlur, imgCanny]))
    cv2.imshow("Result", result)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break