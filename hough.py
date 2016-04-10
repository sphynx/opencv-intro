import cv2
import numpy as np

from matplotlib import pyplot as plt

def subplot(ix, img, title):
    plt.subplot(ix)
    plt.imshow(img, cmap = "gray")
    plt.title(title)
    plt.xticks([])
    plt.yticks([])

img = cv2.imread("images/board1.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150, apertureSize = 3)

lines = cv2.HoughLines(edges, 1, np.pi/180, 200)

with_lines = np.copy(img)

for rho, theta in lines[0]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))

    print (x1, y1)

    cv2.line(with_lines, (x1,y1), (x2,y2), (255,0,0), 3)

# hough_lines = edges

subplot(131, img, "Original image")
subplot(132, edges, "Edges")
subplot(133, with_lines, "Hough lines")

plt.show()
