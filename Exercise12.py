# Resize the provided image using nearest neighbor or bilinear interpolation
from skimage import io
import matplotlib.pyplot as plt
import cv2
image = io.imread('messi5.jpg')
res1 = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
res2 = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_NEAREST)
plt.imshow(res2)
plt.show()

