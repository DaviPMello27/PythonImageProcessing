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

def finder(image, y, x, color, size):
    image[y, x] = color
    for i in range(-1, 2):
        for j in range(-1, 2):
            if(image[y + i, x + j] > 250 and not(i == 0 and j == 0)):
                size[1] = max(y, size[1])
                size[2] = min(x, size[2])
                size[3] = max(x, size[3])
                finder(image, y + i, x + j, color, size)

def findWhite(image):
    result = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    findColor = 200
    count = 0
    for y in range(1, result.shape[0] - 1):
        for x in range(1, result.shape[1] - 1):
            if(result[y, x] > 250):
                findColor -= 5
                count += 1
                size = [y, y, x, x]
                finder(result, y, x, findColor, size)
                cv2.namedWindow(f"Region {count}", cv2.WINDOW_NORMAL)
                cv2.resizeWindow(f"Region {count}", 300, 300)
                cv2.imshow(f"Region {count}", image[size[0]:size[1]+1, size[2]:size[3]+1])
                print(size)
    print(f"There are {count} white shapes in the picture.")
    showImage("Result", result)
    return count
            
img = cv2.imread("img/doublepasstest.jpeg")
findWhite(img)
plt.show()