import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('sample_closing.png')
kernel = np.ones((9,9),np.uint8)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
# cv2.imshow("image", img)
# closing=cv2.resize(closing,(0,0),fx=2,fy=2)
# cv2.imshow("closing image", closing)
fig,anh=plt.subplots(2,1,figsize=(16,9))
anh[0].imshow(img,cmap='gray')
anh[1].imshow(closing,cmap='gray')
plt.show()
# cv2.waitKey(0)
# cv2.destroyAllWindows()