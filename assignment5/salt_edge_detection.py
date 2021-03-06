import cv2
import numpy as np

img = cv2.imread('C:/Users/rahul/Desktop/Computer-Vision-Practical-CS4111/assignment5/salt.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)




img_canny = cv2.Canny(img,100,200)


img_sobelx = cv2.Sobel(gray,cv2.CV_8U,1,0,ksize=5)
img_sobely = cv2.Sobel(gray,cv2.CV_8U,0,1,ksize=5)
img_sobel = img_sobelx + img_sobely



kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
img_prewittx = cv2.filter2D(gray, -1, kernelx)
img_prewitty = cv2.filter2D(gray, -1, kernely)


cv2.imshow("Original Image", img)
cv2.imshow("Canny", img_canny)
cv2.imshow("Sobel X", img_sobelx)
cv2.imshow("Sobel Y", img_sobely)
cv2.imshow("Sobel", img_sobel)
cv2.imshow("Prewitt X", img_prewittx)
cv2.imshow("Prewitt Y", img_prewitty)
cv2.imshow("Prewitt", img_prewittx + img_prewitty)


cv2.waitKey(0)
cv2.destroyAllWindows()
