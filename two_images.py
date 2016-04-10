import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("images/board1.jpg", 0)
edges = cv2.Canny(img, 100, 200)

def subplot(ix, img, title):
    plt.subplot(ix)
    plt.imshow(img, cmap = "gray")
    plt.title(title)
    plt.xticks([])
    plt.yticks([])

subplot(221, img, "Original image")
subplot(222, edges, "Edge image")
subplot(223, edges, "Edge image")
subplot(224, edges, "Edge image")

plt.show()
