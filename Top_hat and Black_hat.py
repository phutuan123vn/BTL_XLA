import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread("top_hat.png")
kernel = np.ones((5,5),np.uint8)
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel, 
iterations=3)
img1=cv2.imread('black_hat.jpg',0)
filterSize =(3, 3)
kernel1 = cv2.getStructuringElement(cv2.MORPH_RECT,filterSize)
blackhat = cv2.morphologyEx(img1,cv2.MORPH_BLACKHAT,kernel1,iterations=1)
fig,anh=plt.subplots(2,2,figsize=(16,9))
anh[0,0].imshow(img,cmap='gray')
anh[0,1].imshow(tophat,cmap='gray')
anh[1,0].imshow(img1,cmap='gray')
anh[1,1].imshow(blackhat,cmap='gray')
anh[0,0].set_title('Ảnh gốc')
anh[0,1].set_title('Ảnh Top hat')
anh[1,0].set_title('Ảnh gốc')
anh[1,1].set_title('Ảnh Blac hat')
plt.show()
