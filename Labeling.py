import matplotlib.pyplot as plt
from random import randint as rand
import numpy as np
import cv2

def showImage(title, image, pos = 111):
    plot = plt.subplot(pos)
    plot.set_title(title)
    plot.set_yticks([])
    plot.set_xticks([])
    plot.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

def finder(image, y, x, color):
    image[y, x] = color
    print(f"Changing ({y}, {x})")
    for i in range(-1, 2):
        for j in range(-1, 2):
            if(image[y + i, x + j] > 250 and not(i == 0 and j == 0)):
                finder(image, y + i, x + j, color)

def findWhite(image):
    result = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)
    result = np.res
    findColor = 200
    count = 0
    for y in range(1, result.shape[0] - 1):
        for x in range(1, result.shape[1] - 1):
            if(result[y, x] > 250):
                findColor -= 5
                count += 1
                finder(result, y, x, findColor)
                print("-------------")
    showImage("Result", result)
    return count

def check4connectivity(image,y, x):
    north = image[y-1, x]
    west = image[y, x-1]
    

def twoPass(image):
    result = image[:,:,0]
    result[result < 3] = 0 
    result[result > 250] = 1
    findColor = 200
    count = 0
    for y in range(result.shape[0]):
        for x in range(result.shape[1]):
            if result[y,x] == 1:
                count+=1
                check4connectivity(result,y, x)
            

   


                
img = cv2.imread("img/doublepass.jpeg")
twoPass(img)
plt.show()