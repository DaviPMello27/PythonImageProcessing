import matplotlib.pyplot as plt
import numpy as np
import cv2

def showImage(title, image, pos = 111, effect = None):
    plot = plt.subplot(pos)
    plot.set_yticks([])
    plot.set_xticks([])
    plot.set_title(title)
    plot.imshow(image, cmap = effect)

def fisrtPass(image):
    result = np.array(image)
    currentLabel = 30
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            if(result[y, x] < 128):
                result[y, x] = 0
            else:
                result[y, x] = 255
    showImage("Original image", cv2.cvtColor(result, cv2.COLOR_GRAY2BGR), 131)
    for y in range(1, image.shape[0]):
        for x in range(1, image.shape[1]):
            north = result[y - 1, x]
            west = result[y, x - 1]
            if(result[y, x] > 250):
                if(north == 0 and west == 0):
                    currentLabel += 15
                    result[y, x] = currentLabel
                elif(north == 0 and west != 0):
                    result[y, x] = result[y, x - 1]
                elif(north != 0 and west == 0 or north == west):
                    result[y, x] = result[y - 1, x]
                else:
                    result[y, x] = min(north, west)
            else:
                result[y, x] = 0
    print(currentLabel)
    return result

#def secondPass(image):


                
                  


    




img = cv2.cvtColor(cv2.imread("img/doublepass.jpeg"), cv2.COLOR_BGR2GRAY)
showImage("Labelled image", cv2.cvtColor(fisrtPass(img), cv2.COLOR_GRAY2BGR), 132)
plt.show()






















































