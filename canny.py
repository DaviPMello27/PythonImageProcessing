import matplotlib.pyplot as plt
import numpy as np
import cv2
import math
from os import system
from time import sleep

maskX = [[-1, 0, 1], 
         [-2, 0, 2],
         [-1, 0, 1]]

maskY = [[ 1,  2,  1], 
         [ 0,  0,  0],
         [-1, -2, -1]]

gaussMask = [[2,  4,  5,  4, 2],
             [4,  9, 12,  9, 4],
             [5, 12, 15, 12, 5],                 #159
             [4,  9, 12,  9, 4],
             [2,  4,  5,  4, 2]]



def showImage(title, image, pos, effect = None):
    plot = plt.subplot(pos)
    plot.set_yticks([])
    plot.set_xticks([])
    plot.set_title(title)
    plot.imshow(image, cmap = effect)

def getSobel(title, image, maskX, maskY):
    kernelHalf = len(maskX)//2
    tempImg = np.array(image)
    for y in range(kernelHalf, image.shape[0] - kernelHalf):
        for x in range(kernelHalf, image.shape[1] - kernelHalf):
            sum = 0.0
            sum2 = 0.0
            for i in range(-kernelHalf, kernelHalf + 1):
                for j in range(-kernelHalf, kernelHalf + 1):
                    sum += float(image[y + i, x + j] * maskX[i + kernelHalf][j + kernelHalf])
                    sum2 += float(image[y + i, x + j] * maskY[i + kernelHalf][j + kernelHalf])
            tempImg[y, x] = min((sum**2 + sum2**2)**0.5, 255)
            atanMat[y , x] = math.degrees(math.atan2(sum2, sum))
    return tempImg

def getImagePixelStrength(image, min, max):
    imageStrength = np.zeros((image.shape[0], image.shape[1]))
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            if(image[y, x] > min and image[y, x] < max):
                imageStrength[y, x] = 1
                image[y, x] = 128
            elif(image[y, x] >= max):
                imageStrength[y, x] = 2
                image[y, x] = 255
            else:
                image[y, x] = 0
    return imageStrength

def nonMax(title, image, atan):
    progress, oldProg, fullProg = 0, -1, atan.shape[0] * atan.shape[1]
    for y in range(1, image.shape[0] - 1):
        for x in range(1, image.shape[1] - 1):
            if(atan[y, x] < 0):
                atan[y, x] += 180
            if((0 <= atan[y, x] < 25.5) or (157.5 <= atan[y, x] <= 180)):
                if((image[y, x] < image[y, x + 1]) or (image[y, x] < image[y, x - 1])):
                    image[y, x] = 0
            elif(25.5 <= atan[y, x] < 67.5):
                if((image[y, x] < image[y - 1, x + 1]) or image[y, x] < image[y + 1, x - 1]):
                    image[y, x] = 0
            elif(67.5 <= atan[y, x] < 112.5):
                if(image[y, x] < image[y + 1, x] or image[y, x] < image[y - 1, x]):
                    image[y, x] = 0
            elif(112.5 <= atan[y, x] < 157.5):
                if(image[y, x] < image[y + 1, x + 1] or image[y, x] < image[y - 1, x - 1]):
                    image[y, x] = 0

            progress += float(1/fullProg)
            if(int(progress*100) > oldProg):
                system("clear")
                print(f"{title}: {int(progress*100)}%")
                oldProg = progress*100
    print(f"{title} is done!")
    sleep(1)

def hysteresisBody(image, imageStrength, y, x):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if(y + i < image.shape[0] and x + j < image.shape[1]):
                if(imageStrength[y, x] == 2 and (not (i == 0 and j == 0)) and imageStrength[y + i, x + j] == 1):
                    image[y + i, x + j] = 255
                    imageStrength[y + i, x + j] = 2
                    print(f"{y}, {x}")
                    hysteresisBody(image, imageStrength, y + i, x + j)
    return
                                

def hysteresis(image, imageStrength):
    for y in range(1, image.shape[0] - 1):
        for x in range(1, image.shape[1] - 1):
            image[y, x] = 0
            if(imageStrength[y, x] == 2):
                hysteresisBody(image, imageStrength, y, x)
                image[y, x] = 255
    return image

imgOriginal = cv2.imread("img/anime.jpg")
imgGauss = cv2.cvtColor(imgOriginal, cv2.COLOR_BGR2GRAY)

#===========================ATAN=MAT===========================#
atanMat = np.zeros((imgOriginal.shape[0], imgOriginal.shape[1]))

#===========================GAUSS+SOBEL===========================#
imgGauss = cv2.GaussianBlur(imgGauss, (5, 5), 3)
imgGauss = getSobel("Masks", imgGauss, maskX, maskY)

#-----Show-Sobel-----#
showImage("Sobel", cv2.cvtColor(imgGauss, cv2.COLOR_GRAY2BGR), 322)

#===========================NON=MAXIMUM=SUPPRESSION===========================#
nonMax("Paint", imgGauss, atanMat)
showImage("Non-Maximum", cv2.cvtColor(imgGauss, cv2.COLOR_GRAY2BGR), 323)

#===========================DOUBLE=THRESHOLD===========================#
imageStrength = getImagePixelStrength(imgGauss, 50, 160)
showImage("Double Threshold", cv2.cvtColor(imgGauss, cv2.COLOR_GRAY2BGR), 324)

#===========================HYSTERESIS===========================#
imgGauss = hysteresis(imgGauss, imageStrength)

#-----Show-Original-----#
showImage("Original", cv2.cvtColor(imgOriginal, cv2.COLOR_RGB2BGR), 321)

#-----Show-Final-----#
showImage("Final", cv2.cvtColor(imgGauss, cv2.COLOR_GRAY2BGR), 325)
plt.show()