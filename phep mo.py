import cv2
import numpy as np
img = cv2.imread("text1.png")
kernel = np.ones((7,7),np.uint8)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
cv2.imshow("image", img)
cv2.imshow("opening image", opening)
cv2.waitKey(0)
cv2.destroyAllWindows()