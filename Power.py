import matplotlib.pyplot as plt
import cv2

def showImage(title, pos, effect = None):
    image = plt.subplot(pos)
    image.set_title(title)
    image.set_yticks([]), image.set_xticks([])
    image.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), cmap = effect)

def calculateIntensity(image, plot):
    intervals = ()
    intensities = []
    for i in range(256):
        intervals = intervals + (i,)
        intensities.append(0)
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            g = image[y, x]
            intensities[g] += 100/(image.shape[0] * image.shape[1])
            
    graph.set_title("Intensity")
    graph.set_xlabel("Intensity")
    #print(intensities)
    plot.bar(intervals, intensities, align = "edge", width = 0.3)

def transformPow(image, fact):
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            image[y,x] = (255/255**fact) * (image[y,x] ** fact)

imgName = input("Filename: ")
intens = float(input("Type the value of the intensity factor: "))
img = cv2.imread(imgName)
graph, graph2 = plt.subplot(224), plt.subplot(223)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
showImage("Grayscale Image", 221, "gray")
calculateIntensity(img, graph2)
transformPow(img, intens)
showImage("Pow Image", 222)
calculateIntensity(img, graph)
plt.show()
