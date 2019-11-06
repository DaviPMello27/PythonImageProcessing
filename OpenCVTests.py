import numpy as np
import matplotlib.pyplot as plt
import cv2

def showImage(title, image, pos = 111):
    plot = plt.subplot(pos)
    plot.set_title(title)
    plot.set_yticks([]), plot.set_xticks([])
    plot.imshow(cv2.cvtColor(image, cv2.COLOR_RGB2BGR))

img = cv2.imread("img/mountains.jpg")
img2 = cv2.imread("img/aurora.png")
result = cv2.bitwise_xor(img, img2)
showImage("Original", img, 121)
showImage("Bilateral Filter", cv2.bitwise_not(img), 122)
plt.show()