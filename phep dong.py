import cv2
import numpy as np
img = cv2.imread("test phep dong.png")
kernel = np.ones((9,9),np.uint8)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
cv2.imshow("image", img)
cv2.imshow("closing image", closing)
cv2.waitKey(0)
cv2.destroyAllWindows()