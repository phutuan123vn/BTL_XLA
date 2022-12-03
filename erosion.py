import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread('Sample_erosion.png',0)
kernel=np.ones((3,3),dtype=np.uint8)
imgErosion=cv2.erode(img,kernel,iterations=1)
imgErosion3=cv2.erode(img,kernel,iterations=3)
fig,anh=plt.subplots(1,3,figsize=(16,9))
anh[0].imshow(img,cmap='gray')
anh[1].imshow(imgErosion,cmap='gray')
anh[2].imshow(imgErosion3,cmap='gray')
anh[0].set_title('Ảnh gốc')
anh[1].set_title('Ảnh Erosion')
anh[2].set_title('Ảnh Erosion 3 lần')
plt.show()