import numpy as np 
import cv2 
import math
  
# You can give path to the 
# image as first argument 
img = cv2.imread('index.jpeg', 0) 

img1 = 255 - img

img_3 = np.uint8(np.log1p(img))

thresh = 1
img_4 = cv2.threshold(img_3, thresh, 255, cv2.THRESH_BINARY)[1]

cv2.imwrite('negative.png',img1) 
cv2.imshow('Original Image', img)
cv2.imshow('negative image', img1)
cv2.imshow("Log transformation", img_4)
cv2.imwrite('log.png',img_4) 
cv2.waitKey(100000)
      


