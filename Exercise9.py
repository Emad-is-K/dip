#take team pic, and apply qualize histogram
from skimage import io
import matplotlib.pyplot as plt
import cv2
img = io.imread('bay.png')
e_img = cv2.equalizeHist(img)
plt.imshow(e_img, cmap='gray')
plt.show()