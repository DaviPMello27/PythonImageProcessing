import matplotlib.pyplot as plt
import numpy as np
import cv2
import math

def showImage(title, image, pos, effect = None):
    imagem = plt.subplot(pos)
    imagem.set_title(title)
    imagem.set_yticks([]), imagem.set_xticks([])
    imagem.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), cmap = effect)

def transform(image, size):
    counter = 0
    hSize = (size//2)
    #x = -int(size / 2)
    sum = 0
    gauss = np.zeros((size, size), dtype = np.float)
    sigma = int(input("Define the standard deviation: "))
    for y in range(-hSize, hSize + 1):
        for x in range(-hSize, hSize + 1):
            #print(y+hSize)
            gauss[0][0] = (1.0 / (2.0 * math.pi * sigma**2)) \
                     * math.e ** -((y**2 + x**2) / (2.0*(sigma**2)))
            print(f"{y}, {x}: {gauss[y][x]}", end = " ")
        print()

    for y in range(-Ymin, image.shape[0] + Ymin, 1):
        for x in range(-Xmin, image.shape[1] + Xmin, 1):
            sum = 0
            for y2 in range(Ymin, int(size / 2) + 1, 1):
                for x2 in range(Xmin, int(size / 2) + 1, 1):
                    sum += img[y+y2, x+x2] * gauss[-Ymin+y2][-Xmin+x2]
            sum /= 16
            img2[y, x] = sum

#gauss = [[1,2,1],[2,4,2],[1,2,1]]
filename = "einstein.png"
img = cv2.imread(f"img/{filename}")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img2 = img
#--show original--
showImage("Original Image", img, 121)

size = int(input("Type the size of the matrix: "))
transform(img, size)
showImage("another one", img2, 122)


plt.show()