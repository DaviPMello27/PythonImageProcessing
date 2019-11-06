import matplotlib.pyplot as plt
import numpy as np
import cv2

class Img:
    def __init__(self, img):
        self.image = img

    def invert(self):
        self.image = cv2.bitwise_not(self.image)

    def insertBorder(self, top, bottom, left, right, borderType):
        self.image = cv2.copyMakeBorder(self.image, top, bottom, left, right, borderType)
        self.borders = [top, bottom, left, right]

    def removeBorder(self):
        img = self.image
        border = self.borders
        self.image = img[border[0]:img.shape[0] - border[1], border[2]:img.shape[1] - border[3]]
        self.borders = [0, 0, 0, 0]

    def getInverted(self):
        inverted = cv2.bitwise_not(self.image)
        self.inverted = Img(inverted)
        return inverted

    def getBlurred(self, ksize = (3, 3)):
        blurred = cv2.blur(self.image, ksize)
        self.blurred = Img(blurred)
        return blurred

    def getGuaussianBlurred(self, ksize = (5, 5), sigma = 3):
        gaussBlurred = cv2.GaussianBlur(self.image, ksize, sigma)
        self.gaussBlurred = Img(gaussBlurred)
        return gaussBlurred

    def getLaplacian(self):
        laplacian = cv2.Laplacian(self.image, -1)
        self.laplacian = Img(laplacian)
        return laplacian

    def show(self, pos = 111, title = "", effect = None):
        plot = plt.subplot(pos)
        plot.set_title(title)
        plot.set_yticks([])
        plot.set_xticks([])
        plot.imshow(self.image, cmap = effect)

    def grayToBGR(self):
        image = cv2.cvtColor(self.image, cv2.COLOR_GRAY2BGR)
        self.image = image
        return image

    def BGRToGray(self):
        image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.image = image
        return image
    
    def showHistogram(self, pos = 111):
        intervals = range(256)
        intensities = np.zeros(256)
        for y in range(self.image.shape[0]):
            for x in range(self.image.shape[1]):
                g = self.image[y, x]
                intensities[g] += 100/(self.image.shape[0] * self.image.shape[1])

        plot = plt.subplot(pos)
        plot.set_title("Light intensity in picture")
        plot.set_xlabel("Intensity")
        plot.bar(intervals, intensities, align = "edge", width = 0.3)

    def getSepia(self):
        sepia = np.zeros(self.image.shape)
        img = self.image
        sepia[:, :, 2] = img[:, :, 0] * 0.272 + img[:, :, 1] * 0.534 + img[:, :, 2] * 0.131
        sepia[:, :, 1] = img[:, :, 0] * 0.349 + img[:, :, 1] * 0.686 + img[:, :, 2] * 0.168
        sepia[:, :, 0] = img[:, :, 0] * 0.393 + img[:, :, 1] * 0.769 + img[:, :, 2] * 0.189
        sepia[sepia > 255] = 255
        self.sepia = Img(sepia.astype('uint8'))
        return sepia.astype('uint8')

    def getSobel(self):
        sobel = cv2.add(cv2.Sobel(self.image, -1, 0, 1), cv2.Sobel(self.image, -1, 1, 0))
        self.sobel = Img(sobel)
        return sobel

    def getCanny(self, min, max):
        canny = cv2.Canny(self.image, min, max)
        self.canny = Img(canny)
        return canny

    def getBinary(self, limit = 0):
        binary = self.image
        binary[binary >= limit] = 255
        binary[binary < limit] = 0
        self.binary = Img(binary)
        return binary

    def dilate(self, ksize = (3, 3)):
        kernel = np.ones((ksize))
        self.image = cv2.dilate(self.image, kernel)

    def erode(self, ksize = (3, 3)):
        kernel = np.ones((ksize))
        self.image = cv2.erode(self.image, kernel)


class Image:
    def __init__(self, filename):
        self.original = Img(cv2.cvtColor(cv2.imread(filename), cv2.COLOR_RGB2BGR))
        self.gray = Img(cv2.cvtColor(self.original.image, cv2.COLOR_BGR2GRAY))
    
lego = Image("img/lego.jpg")

lego.gray.getLaplacian()
lego.gray.laplacian.getBinary(20)
lego.gray.laplacian.grayToBGR()
lego.gray.laplacian.dilate((3, 3))
lego.gray.laplacian.show(121)
lego.gray.laplacian.erode((3, 3))
lego.gray.laplacian.show(122)

plt.show()