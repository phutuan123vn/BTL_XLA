import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('SAMPLE/sample_closing.png')
kernel = np.ones((9,9),np.uint8)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel,iterations=1)
closing3 = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel,iterations=3)
fig,anh=plt.subplots(1,3,figsize=(16,9))
anh[0].imshow(img,cmap='gray')
anh[1].imshow(closing,cmap='gray')
anh[2].imshow(closing3,cmap='gray')
anh[0].set_title('Ảnh gốc')
anh[1].set_title('Ảnh Closing')
anh[2].set_title('Ảnh Closing lặp 3')
cv2.imwrite('SAVED_IMAGE/ClosingImage.jpg',closing)
cv2.imwrite('SAVED_IMAGE/ClosingImage3.jpg',closing3)
plt.show()