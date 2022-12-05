import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread("SAMPLE/test duong bao.png")
kernel = np.ones((3,3),np.uint8)

eroded = cv2.morphologyEx(img, cv2.MORPH_ERODE, kernel)
bound = cv2.subtract(img, eroded)
fig,anh=plt.subplots(1,2,figsize=(16,9))
anh[0].imshow(img,cmap='gray')
anh[1].imshow(bound,cmap='gray')
anh[0].set_title('Ảnh gốc')
anh[1].set_title('Ảnh Boundary')
plt.show()