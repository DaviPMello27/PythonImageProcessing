import cv2
import matplotlib.pyplot as plt

f ,f2 = plt.subplot(121), plt.subplot(122)
imgOriginal = cv2.imread("img/bike.jpg")
img = cv2.cvtColor(imgOriginal, cv2.COLOR_RGB2GRAY)

f.imshow(cv2.cvtColor(img, cv2.COLOR_GRAY2BGR))
img = cv2.GaussianBlur(img, (3, 3), 1)

## gradient X ##
#gradx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3, scale=1, delta=0)
#gradx = cv2.convertScaleAbs(gradx)

## gradient Y ##
grady = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3, scale=1, delta=0)
grady = cv2.convertScaleAbs(grady)
#img = cv2.add(gradx, grady)

f2.imshow(cv2.cvtColor(grady, cv2.COLOR_GRAY2BGR))
plt.show()