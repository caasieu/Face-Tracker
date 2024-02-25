import cv2
import numpy as np
from scipy import ndimage

kernel_3x3 = np.array([
  [-1, -1, -1],
  [-1,  8, -1],
  [-1, -1, -1]
])

kernel_5x5 = np.array([
  [1, -1, -1, -1, -1],
  [-1,  1,  2,  1, -1],
  [-1,  2,  4,  2, -1],
  [-1,  1,  2,  1, -1],
  [-1, -1, -1, -1, -1]
])

img = cv2.imread("images/1.jpg", 0)

k3 = ndimage.convolve(img, kernel_3x3)
k5 = ndimage.convolve(img, kernel_5x5)

blurred = cv2.GaussianBlur(img, (11, 11), 0)
g_hpf = img - blurred


# Naming the window
cv2.namedWindow('MyWindow', cv2.WINDOW_NORMAL)
cv2.resizeWindow("MyWindow", 840, 780)

#esperar uma tecla ser pressionada
while cv2.waitKey(1) != 27:
  #cv2.imshow('MyWindow', k3)
  #cv2.imshow('MyWindow', k5)
  cv2.imshow("MyWindow", g_hpf)
