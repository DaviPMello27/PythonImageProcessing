#(x - h)**2 + (y - k)**2 = r**2

import matplotlib.pyplot as plt
import cv2

def showImage(image):
    graph = plt.subplot()
    graph.set_yticks([]), graph.set_xticks([])
    graph.imshow(image)

def fillCircle(h, k, r):
    for y in range(k - r, k + r):
        for x in range(h - r, h + r):
            if(circleEq(x, y, h, k, r)):
                img[y, x] = [255 - img[y, x][0], 255 - img[y, x][1], 255 - img[y, x][2]]
        
def circleEq(x, y, h, k, r):
    return (x - h)**2 + (y - k)**2 <= r**2
    
filename = input("Filename: ")
img = cv2.imread(filename)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(f"Filename has {img.shape[0]}px in height and {img.shape[1]}px in width.")
h, k, r = int(input("Type the x and y or the origin and the radius, respectively: ")), int(input()), int(input())
fillCircle(h, k, r)
showImage(img)
fig = plt.gcf()
fig.canvas.set_window_title('Circle')
plt.show()