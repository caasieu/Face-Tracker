import cv2
import numpy as np

img = cv2.imread('images/1.jpg', 0)

cv2.namedWindow('Neon', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Neon',860, 680)

cv2.imwrite('canny.jpg', cv2.Canny(img, 200, 300))
cv2.imshow('Neon', cv2.imread('canny.jpg'))
cv2.waitKey(0)