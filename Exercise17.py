#Explore Otsu method
from skimage import io
import matplotlib.pyplot as plt
import cv2
img = io.imread('lena.jpg')
g_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, otsu_img = cv2.threshold(g_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
plt.imshow(otsu_img)
plt.show()