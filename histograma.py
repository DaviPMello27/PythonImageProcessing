import matplotlib.pyplot as plt
import cv2

def showImage(title, pos, effect = None):
    image = plt.subplot(pos)
    image.set_title(title)
    image.set_yticks([]), image.set_xticks([])
    image.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), cmap = effect)

def calculateIntensity(plot, plot2):
    intervals = ()
    intensities = []
    for i in range(256):
        intervals = intervals + (i,)
        intensities.append(0)
    
    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            g = img[y, x]
            intensities[g] += 100/(img.shape[0] * img.shape[1])
            
    graph.set_title("Light intensity in picture")
    graph.set_xlabel("Intensity")
    #print(intensities)
    plot.bar(intervals, intensities, align = "edge", width = 0.3)

    maxGray = 0
    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            if(img[y, x] > maxGray):
                maxGray = img[y, x]
    const = 255 / maxGray

    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            img[y, x] = int(img[y, x] * const)
            g = img[y, x]
            intensities[g] += 100/(img.shape[0] * img.shape[1])
            
    graph2.set_title("Light intensity in windowed picture")
    graph2.set_xlabel("Intensity")
    #print(intensities)
    plot2.bar(intervals, intensities, align = "edge", width = 0.3)
    

imgName = input("Filename: ")
img = cv2.imread(imgName)
graph, graph2 = plt.subplot(223), plt.subplot(224)
showImage("Grayscale Image", 221, "gray")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
calculateIntensity(graph, graph2)
showImage("Windowed Grayscale Image", 222)
plt.show()
