import cv2
import numpy as np
img = cv2.imread("test duong bao.png")
kernel = np.ones((3,3),np.uint8)

eroded = cv2.morphologyEx(img, cv2.MORPH_ERODE, kernel)
bound = cv2.subtract(img, eroded)
cv2.imshow("image", img)
cv2.imshow("bound image", bound)
cv2.waitKey(0)
cv2.destroyAllWindows()
