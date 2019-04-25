import cv2
import numpy as np
from matplotlib import pyplot as plt
for i in range(1,5):
	img = cv2.imread(str(i) + ".jpg",0)
	plt.hist(img.ravel(),256,[0,256]); plt.show()

