import cv2
import numpy as np 

#img = np.zeros((200, 200), dtype=np.uint8)
#img[50:150, 50:150] = 155
#img[100:200, 100:200] = 200

img = cv2.imread('images/4.jpg', 0)


ret, thresh = cv2.threshold(img, 127, 215, 0)
contours, hierarchy = cv2.findContours(
	thresh, cv2.RETR_EXTERNAL, # cv2.RETR_TREE | cv2.RETR_EXTERNAL 
	cv2.CHAIN_APPROX_SIMPLE
)

color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
img = cv2.drawContours(color, contours, -1, (0, 255, 0), 1)


cv2.namedWindow('Contour', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Contour', 680, 680)


cv2.imshow("Contour", color)

cv2.waitKey()