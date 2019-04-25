import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("index.jpg")
# Gaussian Pyramid
layer = img.copy()
gaussian_pyramid = [layer]
for i in range(4):
  layer = cv2.pyrDown(layer)
  gaussian_pyramid.append(layer)
# Laplacian Pyramid
layer = gaussian_pyramid[4]
#cv2.imshow("6", layer)
laplacian_pyramid = [layer]
for i in range(4, 0, -1):
  size = (gaussian_pyramid[i - 1].shape[1], gaussian_pyramid[i - 1].shape[0])
  gaussian_expanded = cv2.pyrUp(gaussian_pyramid[i], dstsize=size)
  laplacian = cv2.subtract(gaussian_pyramid[i - 1], gaussian_expanded)
  laplacian_pyramid.append(laplacian)
  #adaptive(laplacian)
  cv2.imwrite(str(i) + ".jpg", laplacian)
  
cv2.imshow("Original image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()