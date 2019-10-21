import matplotlib.pyplot as plt
import cv2

class Image:
    def __init__(self, filename):
        self.fileName = filename
        self.img = cv2.imread(f"img/{filename}")
        self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        self.xSize = self.img.shape[1]
        self.ySize = self.img.shape[0]
        self.transform = Transform(self.img, self.xSize, self.ySize)

    def showSelf(self, title = "", pos = 111, effect = None):
        image = plt.subplot(pos)
        image.set_title(title)
        image.set_yticks([]), image.set_xticks([])
        image.imshow(cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB), cmap = effect)

class Transform:
    def __init__(self, img, xSize, ySize):
        print("")
        self.img = img
        self.y = ySize
        self.x = xSize
    def media(self, min, max):
        for y in range(2, self.y - 2, 1):
            for x in range(2, self.x - 2, 1):
                if self.img[y, x] > max or self.img[y, x] < min:
                    temp = int( int(self.img[y - 1, x - 1])    *1    + 
                                int(self.img[y - 1, x])        *2    + 
                                int(self.img[y - 1, x + 1])    *1    + 
                                int(self.img[y, x - 1])        *2    + 
                                int(self.img[y, x])            *4    + 
                                int(self.img[y, x + 1])        *2    + 
                                int(self.img[y + 1, x - 1])    *1    + 
                                int(self.img[y + 1, x])        *2    + 
                                int(self.img[y + 1, x + 1])    *1    / 16)
                    self.img[y, x] = temp
        #Image.showSelf(f"Transform 9: Min: {min}, Max: {max}")

minMax = [255, 0]
img = Image("fingor.jpg")
#--show original--
img.showSelf("Original Image", 121)
img.transform.media(255, 0)
img.showSelf("Media9 Image", 122)

plt.show()