import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('index.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gaussian = cv2.GaussianBlur(gray,(3,3),0)
plt.hist(img_gaussian.ravel(),256,[0,256]); plt.show()