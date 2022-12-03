import cv2
import numpy as np
img = cv2.imread("phep dan.png")
kernel = np.ones((3,3),np.uint8)
imgDialation = cv2.dilate(img, kernel, iterations=1)
imgDialation3 = cv2.dilate(img, kernel, iterations=3)

cv2.imshow("image", img)
cv2.imshow("Dialation image", imgDialation)
cv2.imshow("Dialation3 image", imgDialation3)

cv2.waitKey(0)
cv2.destroyAllWindows()
