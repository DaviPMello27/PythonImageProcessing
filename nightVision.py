import matplotlib.pyplot as plt
import cv2
import math

def showImage(title, pos, effect = None):
    image = plt.subplot(pos)
    image.set_title(title)
    image.set_yticks([]), image.set_xticks([])
    image.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), cmap = effect)

def calculateLog(image):
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            image[y,x] = (255/math.log(256)) * math.log(img[y, x] + 1)

def nightVision(image):
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            image[y,x] = [0, image[y, x][1], 0]

imgName = input("Filename: ")
img = cv2.imread(imgName)
graph = plt.subplot(212)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
showImage("Original Image", 121)
calculateLog(img)
img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
nightVision(img)
showImage("Log Image", 122)
plt.show()
