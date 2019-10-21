import cv2
import numpy
import matplotlib.pyplot as plt

def showImage(title, image, pos):
    plot = plt.subplot(pos)
    plot.set_yticks([])
    plot.set_xticks([])
    plot.set_title(title)
    plot.imshow(image)

def getSobel(img):
    SobelX = cv2.Sobel(img, cv2.CV_16S, 0, 1)
    SobelX = cv2.convertScaleAbs(SobelX)
    SobelY = cv2.Sobel(img, cv2.CV_16S, 1, 0)
    SobelY = cv2.convertScaleAbs(SobelY)
    sketch = cv2.add(SobelX, SobelY)
    return cv2.bitwise_not(sketch)

image = cv2.imread("img/menininha.png")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = getSobel(image)
image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
showImage("nice", image, 111)
plt.show()