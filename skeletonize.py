import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('SAMPLE/test skel.png',0)
fig,anh=plt.subplots(1,2,figsize=(16,9))
anh[0].imshow(img,cmap='gray')
size = np.size(img)
skel = np.zeros(img.shape, np.uint8)
ret, img = cv2.threshold(img, 127, 255, 0)
element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
done = False

while (not done):
    eroded = cv2.erode(img, element)
    temp = cv2.dilate(eroded, element)
    temp = cv2.subtract(img, temp)
    skel = cv2.bitwise_or(skel, temp)
    img = eroded.copy()

    zeros = size - cv2.countNonZero(img)
    if zeros == size:
        done = True

# anh[0].imshow(img,cmap='gray')
anh[1].imshow(skel,cmap='gray')
anh[0].set_title('Ảnh gốc')
anh[1].set_title('Ảnh Xương hóa')
plt.show()
