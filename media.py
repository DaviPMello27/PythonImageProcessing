import matplotlib.pyplot as plt
import cv2

def showImage(title, pos, effect = None):
    image = plt.subplot(pos)
    image.set_title(title)
    image.set_yticks([]), image.set_xticks([])
    image.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), cmap = effect)

def transformMedian(image, min, max, pos):
    for y in range(1, image.shape[0] - 1, 1):
        for x in range(1, image.shape[1] - 1, 1):
            if image[y, x] > max or image[y, x] < min:
                temp = [int(image[y - 1, x - 1]), int(image[y - 1, x]), int(image[y - 1, x + 1]), int(image[y, x - 1]), int(image[y, x]), int(image[y, x + 1]), int(image[y + 1, x - 1]), int(image[y + 1, x]), int(image[y + 1, x + 1])]
                temp.sort()
                image[y, x] = temp[4]
    showImage(f"Transform Median: Min: {min}, Max: {max}", pos)

def transform9(image, min, max, pos):
    for y in range(1, image.shape[0] - 1, 1):
        for x in range(1, image.shape[1] - 1, 1):
            if image[y, x] > max or image[y, x] < min:
                temp = int((int(image[y - 1, x - 1]) + int(image[y - 1, x]) + int(image[y - 1, x + 1]) + int(image[y, x - 1]) + int(image[y, x]) + int(image[y, x + 1]) + int(image[y + 1, x - 1]) + int(image[y + 1, x]) + int(image[y + 1, x + 1])) / 9)
                image[y, x] = temp
    showImage(f"Transform 9: Min: {min}, Max: {max}", pos)

def transform8(image, min, max, pos):
    for y in range(1, image.shape[0] - 1, 1):
        for x in range(1, image.shape[1] - 1, 1):
            if image[y, x] > max or image[y, x] < min:
                temp = int((int(image[y - 1, x - 1]) + int(image[y - 1, x]) + int(image[y - 1, x + 1]) + int(image[y, x - 1]) + int(image[y, x + 1]) + int(image[y + 1, x - 1]) + int(image[y + 1, x]) + int(image[y + 1, x + 1])) / 8)
                image[y, x] = temp
    showImage(f"Transform 8: Min: {min}, Max: {max}", pos)

def transformInterval(image, min, max, pos, threshold):
    for y in range(1, image.shape[0] - 1, 1):
        for x in range(1, image.shape[1] - 1, 1):
            if image[y, x] < max and image[y, x] > max - threshold or image[y, x] < min and image[y, x] > min - threshold:
                temp = int((int(image[y - 1, x - 1]) + int(image[y - 1, x]) + int(image[y - 1, x + 1]) + int(image[y, x - 1]) + int(image[y, x]) + int(image[y, x + 1]) + int(image[y + 1, x - 1]) + int(image[y + 1, x]) + int(image[y + 1, x + 1])) / 9)
                image[y, x] = temp
    showImage(f"Min: {min} - {min - threshold}, Max: {max} - {max - threshold}", pos)

def transformBetween(image, min, max, pos):
    for y in range(1, image.shape[0] - 1, 1):
        for x in range(1, image.shape[1] - 1, 1):
            if image[y, x] < max and image[y, x] > min:
                temp = int((int(image[y - 1, x - 1]) + int(image[y - 1, x]) + int(image[y - 1, x + 1]) + int(image[y, x - 1]) + int(image[y, x]) + int(image[y, x + 1]) + int(image[y + 1, x - 1]) + int(image[y + 1, x]) + int(image[y + 1, x + 1])) / 9)
                image[y, x] = temp
    showImage(f"Between {min} and {max}", pos)

minMax = [255, 0]
filename = input("Filename: ")
img = cv2.imread(f"img/{filename}")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#--show original--
showImage("Original Image", 221)
transformMedian(img, 50, 205, 222)
transform8(img, 50, 205, 223)
transform8(img, 0, 200, 224)

plt.show()