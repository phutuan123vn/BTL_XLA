import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('sample_opening.png',0)
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel,iterations=1)
opening3 = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel,iterations=3)
fig,anh=plt.subplots(1,3,figsize=(16,9))
anh[0].imshow(img,cmap='gray')
anh[1].imshow(opening,cmap='gray')
anh[2].imshow(opening3,cmap='gray')
anh[0].set_title('Ảnh gốc')
anh[1].set_title('Ảnh Opening')
anh[2].set_title('Ảnh Opening lặp 3')
plt.show()