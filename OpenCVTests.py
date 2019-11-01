import numpy as np
import matplotlib.pyplot as plt
import cv2

def showImage(title, image, pos = 111):
    plot = plt.subplot(pos)
    plot.set_title(title)
    plot.set_yticks([]), plot.set_xticks([])
    plot.imshow(cv2.cvtColor(image, cv2.COLOR_RGB2BGR))

img1 = cv2.imread("img/mountains.jpg")
img2 = cv2.imread("img/aurora.png")
result = cv2.bitwise_xor(img1, img2)
showImage("Mountains.jpg", img1, 221)
showImage("Aurora.png", img2, 222)
showImage("And", cv2.bitwise_and(img2, cv2.bitwise_not(img1)), 223)
showImage("Not", cv2.bitwise_not(img1, img2), 224)
plt.show()