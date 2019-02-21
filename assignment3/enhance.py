"""
Io = (Ii-Mini)*(((Maxo-Mino)/(Maxi-Mini))+Mino)

 

Io                                - Output pixel value

Ii                                 - Input pixel value

Mini                         - Minimum pixel value in the input image

Maxi                        - Maximum pixel value in the input image

Mino                        - Minimum pixel value in the output image

Maxo                       - Maximum pixel value in the output image
"""

from PIL import Image
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

def gethistogram(img):
    color = ('r','g','b')
    for i,col in enumerate(color):
        histr = cv.calcHist([img],[i],None,[256],[0,256])
        plt.plot(histr,color = col)
        plt.xlim([0,256])
    plt.show()

def normalizeRed(intensity):
    iI = intensity
    minI = 86
    maxI = 230
    minO = 0
    maxO = 255
    iO = (iI - minI)*(((maxO - minO)/(maxI - minI)) + minO)
    return iO

def normalizGreen(intensity):
    iI = intensity
    minI = 90
    maxI = 225
    minO = 0
    maxO = 255
    iO = (iI - minI)*(((maxO - minO)/(maxI - minI)) + minO)
    return iO

def normalizeBlue(intensity):
    iI = intensity
    minI = 100
    maxI = 210
    minO = 0
    maxO = 255
    iO = (iI - minI)*(((maxO - minO)/(maxI - minI)) + minO)
    return iO

imageobject = Image.open("low.png")
#this is for getting histogram
img = cv.imread("low.png")
gethistogram(img)

#splitting the image in r g b
multibands = imageobject.split()

#normalizing r g b
normalizeRedband = multibands[0].point(normalizeRed)
normalizGreenband = multibands[1].point(normalizGreen)
normalizeBlueband = multibands[2].point(normalizeBlue)


#merging the image
normalizedimage = Image.merge("RGB", (normalizeRedband, normalizGreenband, normalizeBlueband))

#imageobject.show()


normalizedimage.save("high.bmp")


    