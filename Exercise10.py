#take team pic and do different parameters, like 4 different one
from matplotlib.cbook import flatten
from skimage import io
import matplotlib.pyplot as plt
import cv2
img = io.imread('bay.png')
e_img = cv2.equalizeHist(img)

plt.imshow(e_img, cmap='gray')
plt.show()