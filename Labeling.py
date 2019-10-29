import matplotlib.pyplot as plt
from random import randint as rand
import numpy as np
import cv2

def showImage(title, image, pos = 111):
    plot = plt.subplot(pos)
    plot.set_title(title)
    plot.set_yticks([])
    plot.set_xticks([])
    plot.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

def finder(image, y, x, color):
    image[y, x] = color
    for i in range(-1, 2):
        for j in range(-1, 2):
            if(image[y + i, x + j] > 250 and not(i == 0 and j == 0)):
                finder(image, y + i, x + j, color)

def findWhite(image):
    result = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    findColor = 200
    count = 0
    for y in range(1, result.shape[0] - 1):
        for x in range(1, result.shape[1] - 1):
            if(result[y, x] > 250):
                findColor -= 5
                count += 1
                finder(result, y, x, findColor)
    print(f"There are {count} white shapes in the picture.")
    showImage("Result", result)
    return count
            
img = cv2.imread("img/twenty.jpeg")
findWhite(img)
plt.show()