# Read images and webcam
import cv2 #computer vision
import numpy as np
print("Packages imported")

# viewing webcam
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)
cap.set(cv2.CAP_PROP_BRIGHTNESS, 100)

while True:
    success, img = cap.read()
    if not success:
        break
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# video importing
cap = cv2.VideoCapture("Resources/test-video.mp4")
while True:
    success, img = cap.read()
    if not success:
        break
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# importing and showing image
img = cv2.imread("Resources/impostor.jpg")
cv2.imshow("Output", img)
cv2.waitKey(0)