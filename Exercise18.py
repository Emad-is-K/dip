#perform dialation and erosion  and shown example of each
from skimage import io
import numpy as np
import matplotlib.pyplot as plt
import cv2
img = io.imread('morph.png')

plt.imshow(img)
plt.show()

kernel = np.ones((10,10),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)

plt.imshow(cv2.cvtColor(erosion, cv2.COLOR_BGR2RGB))
plt.show()

dilation = cv2.dilate(img,kernel,iterations = 1)

plt.imshow(cv2.cvtColor(dilation, cv2.COLOR_BGR2RGB))
plt.show()