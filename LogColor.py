import matplotlib.pyplot as plt
import cv2
import math

def showImage(title, pos, effect = None):
    image = plt.subplot(pos)
    image.set_title(title)
    image.set_yticks([]), image.set_xticks([])
    image.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), cmap = effect)

def calculateLog(image):
    prog, oldprog, temp = 0, -1, 0
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            image[y,x] = (255/math.log(256)) * math.log(img[y, x] + 1)
            #=================PROGRESS=================
            if(prog > oldprog):
                print(f"{prog}% done...")
                oldprog = prog
            temp += 1
            prog = int(temp * 50 /(image.shape[0]*image.shape[1]))

def insertColor(image, OriginalImage):
    prog, oldprog, temp = 0, -1, 0
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            if((1 + image[y, x][0] / 255) * OriginalImage[y, x][0] > 255):
                image[y,x][0] = 255
            else:
                image[y,x][0] = (1 + image[y, x][0] / 255) * OriginalImage[y, x][0]
            if((1 + image[y, x][1] / 255) * OriginalImage[y, x][1] > 255):
                image[y,x][1] = 255
            else:
                image[y,x][1] = (1 + image[y, x][1] / 255) * OriginalImage[y, x][1]
            if((1 + image[y, x][2] / 255) * OriginalImage[y, x][2] > 255):
                image[y,x][2] = 255
            else:
                image[y,x][2] = (1 + image[y, x][2] / 255) * OriginalImage[y, x][2]
            #=================PROGRESS=================
            if(prog > oldprog):
                print(f"{prog + 50}% done...")
                oldprog = prog
            temp += 1
            prog = int(temp * 50 /(image.shape[0]*image.shape[1]))
    print("100% done!")
    showImage("Colored Log Image", 212)

imgName = input("Filename: ")
print("Working...")
imgOri, img = cv2.imread(imgName), cv2.imread(imgName)
showImage("Original Image", 211)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
calculateLog(img)
img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
insertColor(img, imgOri)
plt.show()
