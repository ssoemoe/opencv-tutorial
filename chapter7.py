# COLOR EXTRACTION
import cv2
import numpy as np
from util import stackImages

def empty(arg):
    pass

path = "Resources/impostor.jpg"
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 240)
cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 19, 179, empty)
cv2.createTrackbar("Saturation Min", "TrackBars", 110, 255, empty)
cv2.createTrackbar("Saturation Max", "TrackBars", 240, 255, empty)
cv2.createTrackbar("Value Min", "TrackBars", 153, 255, empty)
cv2.createTrackbar("Value Max", "TrackBars", 255, 255, empty)

while True:
    img = cv2.imread(path)
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    sat_min = cv2.getTrackbarPos("Saturation Min", "TrackBars")
    sat_max = cv2.getTrackbarPos("Saturation Max", "TrackBars")
    val_min = cv2.getTrackbarPos("Value Min", "TrackBars")
    val_max = cv2.getTrackbarPos("Value Max", "TrackBars")

    lower = np.array([h_min, sat_min, val_min])
    higher = np.array([h_max, sat_max, val_max])
    mask = cv2.inRange(imgHSV, lower, higher)
    colorExtractedImage = cv2.bitwise_and(img, img, mask=mask)
    imgStack = stackImages(0.4, ([img, imgHSV], [mask, colorExtractedImage]))
    # cv2.imshow("Original", img)
    # cv2.imshow("HSV", imgHSV)
    # cv2.imshow("Mask", mask)
    # cv2.imshow("Color Detected", colorExtractedImage)
    cv2.imshow("Result", imgStack)
    cv2.waitKey(1)