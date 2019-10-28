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
    result[result < 128] = 0
    result[result >= 128] = 255
    currentLabel = 0
    links = []
    
    showImage("Original image", cv2.cvtColor(result, cv2.COLOR_GRAY2BGR), 121)
    for y in range(1, image.shape[0]):
        for x in range(1, image.shape[1]):
            north = result[y - 1, x]
            west = result[y, x - 1]
            if(result[y, x] > 250):
                if(north == 0 and west == 0):
                    currentLabel += 1
                    links.append([currentLabel])
                    result[y, x] = currentLabel
                elif(north == 0 and west != 0):
                    result[y, x] = result[y, x - 1]
                elif(north != 0 and west == 0 or north == west):
                    result[y, x] = result[y - 1, x]
                else:
                    result[y, x] = min(north, west)
                    for i in range(len(links[max(north, west) - 1])):
                        if(not(links[max(north, west) - 1][i] in links[min(north, west) - 1])):
                            links[min(north, west) - 1].append(links[max(north, west) - 1][i])
                    links[max(north, west) - 1][0] = min(north, west)
            else:
                result[y, x] = 0
    for i in range(len(links) - 1, 0, -1):
        if(links[i][0] != i + 1):
            links.pop(i)
    print(links)
    return result, links

def secondPass(image, links):
    result = np.array(image)
    print(result)
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            for i in range(len(links)):
                if(result[y, x] in links[i]):
                    result[y, x] = (i+2)*36
    return result, links

# def secondPass(image, links):
#     result = np.array(image)
#     for y in range(image.shape[0]):
#         for x in range(image.shape[1]):
#             for i in range(len(links)):
#                 for j in range(len(links[i])):
#                     if(image[y, x] == links[i][j]):
#                         result[y, x] = links[i][0] * 10 + 50
#     return result, links

img = cv2.cvtColor(cv2.imread("img/doublepass.jpeg"), cv2.COLOR_BGR2GRAY)
img, links = fisrtPass(img)
img, links = secondPass(img, links)
print(img)
showImage("Labelled", cv2.cvtColor(img, cv2.COLOR_GRAY2BGR), 122)
plt.show()