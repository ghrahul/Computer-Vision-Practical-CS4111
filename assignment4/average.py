import cv2
import numpy as np
from matplotlib import pyplot as plt

def result1(img):
    kernel = np.ones((5,5),np.float32)/25
    dst = cv2.filter2D(img,-1,kernel)

    plt.subplot(121),plt.imshow(img),plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(dst),plt.title('Averaging(5,5)')
    plt.xticks([]), plt.yticks([])
    plt.show()

def result2(img):
    kernel = np.ones((7,7),np.float32)/49
    dst = cv2.filter2D(img,-1,kernel)

    plt.subplot(121),plt.imshow(img),plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(dst),plt.title('Averaging(7,7)')
    plt.xticks([]), plt.yticks([])
    plt.show()

def result3(img):
    kernel = np.ones((3,3),np.float32)/9
    dst = cv2.filter2D(img,-1,kernel)

    plt.subplot(121),plt.imshow(img),plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(dst),plt.title('Averaging(3,3)')
    plt.xticks([]), plt.yticks([])
    plt.show()




img = cv2.imread('279.jpg')
result1(img)
result2(img)
result3(img)

