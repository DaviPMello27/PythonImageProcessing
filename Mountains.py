import matplotlib.pyplot as plt
from time import sleep
import numpy as np
import cv2

def showImage(title, image, pos = 111):
    plot = plt.subplot(pos)
    plot.set_title(title)
    plot.set_yticks([])
    plot.set_xticks([])
    plot.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

def finder(image, y, x, color, count):
    image[y, x] = color
    for i in range(-1, 2):
        for j in range(-1, 2):
            if(image[y + i, x + j] > 250 and not(i == 0 and j == 0) and count < 800):
                count += 1
                print(count)
                cv2.imshow("nice", image)
                cv2.waitKey(1)
                finder(image, y + i, x + j, color, count)


def findWhite(image):
    result = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)
    findColor = 10
    count = 0
    for y in range(1, result.shape[0] - 1):
        for x in range(1, result.shape[1] - 1):
            if(result[y, x] > 250):
                findColor -= 10
                finder(result, y, x, findColor, count)
                count = 0
                print("-------------")
    cv2.imshow("nice", image)
    cv2.waitKey(50)
    showImage("Result", result)
    return count

img = cv2.imread("img/mount.jpeg")
cv2.namedWindow("nice", cv2.WINDOW_NORMAL)
cv2.resizeWindow("nice", 600, 600)
print(findWhite(img))
plt.show()