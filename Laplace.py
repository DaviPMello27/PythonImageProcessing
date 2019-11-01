import matplotlib.pyplot as plt
import numpy as np
import cv2

mask = [[0, -1, 0], 
        [-1, 4, -1],
        [0, -1, 0]]

mask = np.array(mask)

def showImage(title, image, pos = 111):
    plot = plt.subplot(pos)
    plot.set_title(title)
    plot.set_yticks([]), plot.set_xticks([])
    plot.imshow(cv2.cvtColor(image, cv2.COLOR_GRAY2BGR))

img = cv2.imread("img/moon.tif")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
showImage("Original Image", img, 121)
laplace = cv2.filter2D(img, -1, mask)
laplace = cv2.add(img, laplace)
showImage("Laplacian Image", laplace, 122)
plt.show()