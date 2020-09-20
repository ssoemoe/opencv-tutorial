import cv2
import numpy as np

def getBiggestContour(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    maxArea = 0
    biggest = np.array([])
    largestContour = None
    for cont in contours:
        # cv2.drawContours(imgContour, cont, -1, (255, 0, 0), 3)
        area = cv2.contourArea(cont)
        if area > 100: #adjust according to the paper size
            perimeter = cv2.arcLength(cont, True)
            # we can play around epsilon for better results
            epsilon = 0.02 * perimeter
            approxCorners = cv2.approxPolyDP(cont, epsilon, True)
            approxNumCorners = len(approxCorners)
            if area > maxArea and approxNumCorners == 4:
                maxArea = area
                biggest = approxCorners
                largestContour = cont
    cv2.drawContours(imgContour, largestContour, -1, (255, 0, 0), 5)
    return biggest

def preprocess(img):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1)
    imgCanny = cv2.Canny(imgGray, 200, 200)
    kernel = np.ones_like((5, 5))
    imgDilation = cv2.dilate(imgCanny, kernel = kernel, iterations = 2)
    imgThreshold = cv2.erode(imgDilation, kernel, iterations=1)
    cv2.imshow("Threshold", imgThreshold)
    return imgThreshold

def getWarp(img, biggest):
    print(biggest)

widthImg = 800
heightImg = 900
# viewing webcam
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, widthImg)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, heightImg)
cap.set(cv2.CAP_PROP_BRIGHTNESS, 150)

while True:
    success, img = cap.read()
    cv2.resize(img, (widthImg, heightImg))
    imgContour = img.copy()
    imgThreshold = preprocess(img)
    biggest = getBiggestContour(imgThreshold)
    getWarp(img, biggest)
    cv2.imshow("Video", imgContour)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break