import cv2
import numpy as np 

#img = np.zeros((200, 200), dtype=np.uint8)
#img[50:150, 50:150] = 255

img = cv2.imread('images/2.jpeg', 0)


ret, thresh = cv2.threshold(img, 127, 255, 0)
contours, hierarchy = cv2.findContours(
	thresh, cv2.RETR_TREE, 
	cv2.CHAIN_APPROX_SIMPLE
)

color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
img = cv2.drawContours(color, contours, -1, (0, 255, 0), 2)


cv2.namedWindow('Contour', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Contour', 680, 680)


cv2.imshow("Contour", color)

cv2.waitKey()