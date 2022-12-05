import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread('SAMPLE/sample_dilation.png',0)
kernel=np.ones((3,3),dtype=np.uint8)
imgDilation=cv2.dilate(img,kernel,iterations=1)
imgDilation3=cv2.dilate(img,kernel,iterations=3)
fig,anh=plt.subplots(1,3,figsize=(16,9))
anh[0].imshow(img,cmap='gray')
anh[1].imshow(imgDilation,cmap='gray')
anh[2].imshow(imgDilation3,cmap='gray')
anh[0].set_title('Ảnh gốc')
anh[1].set_title('Ảnh Erosion')
anh[2].set_title('Ảnh Erosion 3 lần')
cv2.imwrite('SAVED_IMAGE/DilationImage.jpg',imgDilation)
cv2.imwrite('SAVED_IMAGE/DilationImage3.jpg',imgDilation3)
plt.show()