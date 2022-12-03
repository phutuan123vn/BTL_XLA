import cv2
import matplotlib.pyplot as plt
img1 = cv2.imread('test skel.png')
img = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
# Threshold the image
ret, thresh = cv2.threshold(img,50,255,0)
# Find the contours
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, 
cv2.CHAIN_APPROX_SIMPLE)
# For each contour, find the convex hull and draw it
# on the original image.
for i in range(len(contours)):
 hull = cv2.convexHull(contours[i])
 cv2.drawContours(img1, [hull], -1, (255, 0, 0), 2)
fig,anh=plt.subplots(1,2,figsize=(16,9))
anh[0].imshow(img,cmap='gray')
anh[1].imshow(img1,cmap='gray')
anh[0].set_title('Ảnh gốc')
anh[1].set_title('Ảnh Convex')
plt.show()