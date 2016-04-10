import numpy as np
import cv2

img = cv2.imread("images/lena.jpg")

# Create a black image
# width = 512
# img = np.zeros((512, 512, 3), np.uint8)
# img[:, 0 : 0.5*width] = (255,0,0)

# Draw a diagonal blue line with thickness of 5 px
# cv2.line(img, (0,0), (511,511), (255,0,0), 5)

# show picture
cv2.imshow("Result", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

