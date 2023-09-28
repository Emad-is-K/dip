# Simple Thresholding
from skimage import io
import cv2
import matplotlib.pyplot as plt
img = io.imread('https://github.com/opencv/opencv/blob/master/samples/data/gradient.png?raw=true')
ret,thresh1 = cv2.threshold(img,100,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,150,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,170,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,198,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,200,255,cv2.THRESH_TOZERO_INV)

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
