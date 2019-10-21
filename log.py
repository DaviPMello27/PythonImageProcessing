import matplotlib.pyplot as plt
import cv2
import math

def showImage(title, pos, effect = None):
    image = plt.subplot(pos)
    image.set_title(title)
    image.set_yticks([]), image.set_xticks([])
    image.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), cmap = effect)

def calculateIntensity(plot):
    intervals = ()
    intensities = []
    for i in range(256):
        intervals = intervals + (i,)
        intensities.append(0)
    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            img[y,x] = (255/math.log(256)) * math.log(img[y, x] + 1)
            g = img[y, x]
            intensities[g] += 100/(img.shape[0] * img.shape[1])
            
    graph.set_title("Intensity")
    graph.set_xlabel("Intensity")
    print(intensities)
    plot.bar(intervals, intensities, align = "edge", width = 0.3)

imgName = input("Filename: ")
img = cv2.imread(imgName)
graph = plt.subplot(212)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
showImage("Grayscale Image", 221, "gray")
calculateIntensity(graph)
showImage("Log Image", 222)
plt.show()
