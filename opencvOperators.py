import matplotlib.pyplot as plt
import numpy as np
import cv2
import math

def showImage(title, image, pos, grayToBgr = True, rgbToBgr = False):
    print(grayToBgr)

    if grayToBgr:
       image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    elif rgbToBgr:
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    
    plot = plt.subplot(pos)
    plot.set_yticks([])
    plot.set_xticks([])
    plot.set_title(title)
    plot.imshow(image)

def blur(image, kSize):
    return cv2.blur(image, kSize)

def gaussianBlur(image, kSize, sigma):
    return cv2.GaussianBlur(image, kSize, sigma)

def medianBlur(image, kSize):
    return cv2.medianBlur(image, kSize)

def sobel(image, kSize):
    sobelX = cv2.convertScaleAbs(cv2.Sobel(image, cv2.CV_16S, 1, 0, ksize=kSize, scale=1, delta=0, borderType=cv2.BORDER_DEFAULT))
    sobelY= cv2.convertScaleAbs(cv2.Sobel(image, cv2.CV_16S, 0, 1, ksize=kSize, scale=1, delta=0, borderType=cv2.BORDER_DEFAULT))
    return cv2.add(sobelX, sobelY)

imgOriginal = cv2.imread("imagens/menina.png")
imgGray = cv2.cvtColor(imgOriginal, cv2.COLOR_RGB2GRAY)

imgSobel = sobel(imgGray, 3)


showImage("original",  imgGray, 121)
showImage("Opencv sobel 3X3",imgSobel, 122)

plt.show()