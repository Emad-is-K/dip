#translation information and translate shift to right by 100 and down 50
#then rotate the image 90 degrees
#[1,0,100],[0,1,50]
from skimage import io
import cv2
import numpy as np
import matplotlib.pyplot as plt
messi = io.imread('messi5.jpg')
rows,cols,ch = messi.shape
M = np.float32([[1,0,100],[0,1,50]])
dst = cv2.warpAffine(messi,M,(cols,rows))
M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
dst1 = cv2.warpAffine(messi,M,(cols,rows))

plt.imshow(dst1)
plt.show()