import cv2
import numpy as np

img = cv2.imread('C:/Users/rahul/Desktop/Computer-Vision-Practical-CS4111/assignment5/zebra.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

denoised_image = cv2.GaussianBlur(gray,(3,3),0)
img_laplacian = cv2.Laplacian(denoised_image,cv2.CV_64F)

only_laplacian = cv2.Laplacian(gray,cv2.CV_64F)

cv2.imshow("Original Image", img)
cv2.imshow("Laplacian", img_laplacian)
cv2.imshow("Without Gaussian", only_laplacian)

cv2.waitKey(0)
cv2.destroyAllWindows()
