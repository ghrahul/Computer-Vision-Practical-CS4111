import cv2
import numpy as np
from matplotlib import pyplot as plt


def gaussian(img):
    blur = cv2.GaussianBlur(img,(5,5),0)
    plt.subplot(121),plt.imshow(img),plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(blur),plt.title('Gaussian filter ')
    plt.xticks([]), plt.yticks([])
    plt.show()

def median(img):
    median = cv2.medianBlur(img,5)
    plt.subplot(121),plt.imshow(img),plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(median),plt.title('Median filter applied')
    plt.xticks([]), plt.yticks([])
    plt.show()

img = cv2.imread('salt.jpg')
gaussian(img)
median(img)



