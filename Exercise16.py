#Take an image, add Gaussian noise and salt and pepper noise,
# compare the effect of blurring via box, Gaussian, median and bilateral filters
# for both noisy images, as you change the level of noise.
from skimage import io
import numpy as np
import matplotlib.pyplot as plt
import cv2
img = io.imread('lena.jpg')

#salt n pepper and guassian noise
sp_img = img
salt_prob = .15
pepper_prob = .15
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if np.random.rand() < salt_prob:
            sp_img[i, j] = [255, 255, 255]  # White pixel (salt noise)
        elif np.random.rand() < pepper_prob:
            sp_img[i, j] = [0, 0, 0]  # Black pixel (pepper noise)

g_img = cv2.GaussianBlur(img, (9,9), sigmaX=0)

#Averaging filter
avg_blur = cv2.blur(sp_img,(7,7))
avg_blur1 = cv2.blur(g_img,(7,7))

#Median Filter
median = cv2.medianBlur(sp_img,3)
median1 = cv2.medianBlur(g_img,3)

#Guassian filter
guas_blur = cv2.GaussianBlur(sp_img,(9,9),0)
guas_blur1 = cv2.GaussianBlur(g_img,(9,9),0)

#Bilateral filter
bil_blur = cv2.bilateralFilter(sp_img,9,75,75)
bil_blur1 = cv2.bilateralFilter(g_img,9,75,75)

#cv2.fastNlMeansDenoisingColored filter
cv_blur = cv2.fastNlMeansDenoisingColored(sp_img,None, 10, 10, 7, 21)
cv_blur1 = cv2.fastNlMeansDenoisingColored(g_img,None, 10, 10, 7, 21)

plt.subplot(161),plt.imshow(sp_img),plt.title('Input')
plt.subplot(162),plt.imshow(g_img),plt.title('Output')
plt.subplot(163),plt.imshow(avg_blur)
plt.subplot(164),plt.imshow(avg_blur1)
plt.subplot(165),plt.imshow(median)
plt.subplot(166),plt.imshow(median1)
plt.subplot(261),plt.imshow(guas_blur)
plt.subplot(262),plt.imshow(guas_blur1)
plt.subplot(263),plt.imshow(bil_blur)
plt.subplot(264),plt.imshow(bil_blur1)
plt.subplot(265),plt.imshow(cv_blur)
plt.subplot(266),plt.imshow(cv_blur1)

plt.show()