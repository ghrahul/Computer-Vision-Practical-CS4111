import cv2
img1 = cv2.imread('11.jpg')
img = cv2.pyrDown(img1)

gaussian_expanded = cv2.pyrUp(img, dstsize=size)
laplacian = cv2.subtract(img, gaussian_expanded)

ret , o1 = cv2.threshold(img, 125, 255, cv2.THRESH_BINARY)
ret , o2 = cv2.threshold(img, 125, 255, cv2.THRESH_BINARY_INV)
ret , o3 = cv2.threshold(img, 125, 255, cv2.THRESH_TOZERO)
ret , o4 = cv2.threshold(img, 125, 255, cv2.THRESH_TOZERO_INV)
ret , o5 = cv2.threshold(img, 125, 255, cv2.THRESH_TRUNC)
thresh6 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,11,2)
thresh7 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)


titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV','Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, o1, o2, o3, o4, o5, thresh6, thresh7]

for i in range(8):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
