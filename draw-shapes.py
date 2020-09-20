import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
# print(img)
# img[0:100,0:100] = 255,0,0
# img[:] = 255,125,125 # middle colon means the whole x and y full height and width

# img.shape[1] = width, img.shape[0] = height
cv2.line(img, (0,0), (img.shape[1], img.shape[0]), (255,125,125), 3)
cv2.rectangle(img, (0, 0), (250, 350), (125,125,255), cv2.FILLED)
cv2.circle(img, (400,50), 30, (125,125,125), 5)
cv2.putText(img, " OPENCV ", (300,200), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 2)

cv2.imshow("Image", img)
cv2.waitKey(0)