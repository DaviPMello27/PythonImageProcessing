import matplotlib.pyplot as plt
import cv2

def showImage(title, pos, effect = None):
    image = plt.subplot(pos)
    image.set_title(title)
    image.set_yticks([]), image.set_xticks([])
    image.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), cmap = effect)

def getIntensityPercentage(image):
    intensities = []
    for i in range(256):
        intensities.append(0)
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            g = image[y, x]
            intensities[g] += 100/(image.shape[0] * image.shape[1])
    return intensities

def makeHistogram(image, pos, intensities):
    intervals = ()
    for i in range(256):
        intervals += (i, )    
    plot = plt.subplot(pos)
    plot.set_title("Histogram")
    plot.set_xlabel("Intensity")  
    plot.bar(intervals, intensities, align = "center", width = 1)

def getThreshold(image, intensities):
    min, max = 0, 0
    for i in range(255, 0, -1):
        max = intensities[i]
        if max > 2:
            max = i
            break
        intensities[i - 1] += intensities[i]
        intensities[i] = 0
    for i in range(255):
        min = intensities[i]
        if min > 2:
            min = i
            break
        intensities[i + 1] += intensities[i]
        intensities[i] = 0
    print(f"Min: {min}, Max: {max}")
    return [min, max]

def transform(image, minMax):
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            temp = (image[y, x] - minMax[0]) * (255/(minMax[1] - minMax[0]))
            if temp > 255:
                image[y, x] = 255
            else:
                image[y, x] = temp

minMax = [255, 0]
img = cv2.imread("img/polen.tif")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#--show original--
showImage("Original Image", 221)
intensityVector = getIntensityPercentage(img)
makeHistogram(img, 223, intensityVector)
#--show windowed--
img = cv2.imread("img/polen.tif")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
minMax = getThreshold(img, getIntensityPercentage(img))
transform(img, minMax)
showImage("Good one", 222)
makeHistogram(img, 224, getIntensityPercentage(img))
plt.show()