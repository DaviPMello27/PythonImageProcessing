import matplotlib.pyplot as plt
import numpy as np
import cv2

mask = [[-1, -1, -1], 
        [-1, 8, -1],
        [-1, -1, -1]]

def showImage(title, image, pos = 111):
    plot = plt.subplot(pos)
    plot.set_title(title)
    plot.set_yticks([]), plot.set_xticks([])
    plot.imshow(cv2.cvtColor(image, cv2.COLOR_GRAY2BGR))

def sumLaplace(image, laplace):
    result = np.array(image)
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            sum = int(image[y, x]) + int(laplace[y, x])
            result[y, x] = max(min(255, sum - 128), 0)
    return result

def laplaceTransform(image, mask):
    result = np.array(image)
    for y in range(1, image.shape[0] - 1):
        for x in range(1, image.shape[1] - 1):
            sum = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    sum += image[y + i, x + j] * mask[1 + i][1 + j]
            result[y, x] = max(min(255, sum + 128), 0)
    return result

img = cv2.imread("img/dog.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
showImage("Original Image", img, 121)
laplace = laplaceTransform(img, mask)
laplace = sumLaplace(img, laplace)
showImage("Laplacian Image", laplace, 122)
plt.show()