import cv2
img = cv2.imread('input.jpg')
lower_reso = cv2.pyrDown(img)
higher = cv2.pyrUp(img)
cv2.imwrite("original.jpg",img)
cv2.imwrite('smaller.jpg',lower_reso)
cv2.imwrite('higher.jpg',higher)
cv2.waitKey(0)
cv2.destroyAllWindows