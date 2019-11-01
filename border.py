import matplotlib.pyplot as plt
import numpy as np
import cv2

def showImage(title, image, pos = 111, effect = None):
    plot = plt.subplot(pos)
    plot.set_yticks([])
    plot.set_xticks([])
    plot.set_title(title)
    plot.imshow(image, cmap = effect)

img = cv2.imread("img/anime.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
showImage("nice", cv2.cvtColor(img, cv2.COLOR_GRAY2BGR), 211)
imgBorder = cv2.copyMakeBorder(img[455:639, 340:450], 5, 5, 5, 5, cv2.BORDER_REPLICATE)
showImage("nice", cv2.cvtColor(imgBorder, cv2.COLOR_GRAY2BGR), 212)
plt.show()