#perform canny edge detection
from skimage import io
import numpy as np
import matplotlib.pyplot as plt
import cv2
messi = io.imread('messi5.jpg')
edges = cv2.Canny(messi,50,130)

plt.subplot(121),plt.imshow(messi,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()