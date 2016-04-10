import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/board2.jpg',0)
b_small = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
b_blured = cv2.bilateralFilter(b_small,9,75,75)
edges = cv2.Canny(b_small,100,200)
edges_blured = cv2.Canny(b_blured,100,200)


plt.subplot(131),plt.imshow(b_small,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])

plt.subplot(132),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.subplot(133),plt.imshow(edges_blured,cmap = 'gray')
plt.title('Edge Blured Image'), plt.xticks([]), plt.yticks([])

plt.show()