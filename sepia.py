import matplotlib.pyplot as plt
import numpy as np
import cv2

def showImage(title, image, pos, effect = None):
    plot = plt.subplot(pos)
    plot.set_title(title)
    plot.set_yticks([]), plot.set_xticks([])
    plot.imshow(image, cmap = effect)

def to_sepia(image):
    sepia = np.zeros((image.shape[0], image.shape[1], 3), dtype = np.float32)
    sepia[:, :, 2] = image[:, :, 0] * 0.272 + image[:, :, 1] * 0.534 + image[:, :, 2] * 0.131
    sepia[:, :, 1] = image[:, :, 0] * 0.349 + image[:, :, 1] * 0.686 + image[:, :, 2] * 0.168
    sepia[:, :, 0] = image[:, :, 0] * 0.393 + image[:, :, 1] * 0.769 + image[:, :, 2] * 0.189
    sepia[sepia > 255] = 255
    sepia /= 255
    return sepia

img = cv2.imread("img/anime.jpg")
showImage("Original", cv2.cvtColor(img, cv2.COLOR_RGB2BGR), 211)
final1 = to_sepia(img)
showImage("Sepia Quick", final1, 212)
plt.show()
