# latihan 1 filter sobel
# import library yang diperlukan
import cv2
import numpy as np
from matplotlib import pyplot as plt
from skimage import data
# import foto dari file penyimpanan
cute=cv2.imread("D:\SEMESTER 6\Pengolahan Citra Digital\image\hoammm.jpg")
streching = cv2.cvtColor(cute,cv2.COLOR_BGR2GRAY)
# buat sobel
img_sobelx = cv2.Sobel(streching,cv2.CV_8U,1,0,ksize=5)
img_sobely = cv2.Sobel(streching,cv2.CV_8U,0,1,ksize=5)
img_sobel = img_sobelx + img_sobely
#plot hasil output sobel 
fig, axes =plt.subplots(4,2, figsize=(20,20))
ax = axes.ravel()

ax[0].imshow(streching,cmap = 'gray')
ax[0].set_title("citra input")
ax[1].hist(streching.ravel(), bins =256)
ax[1].set_title("Histogram citra input")

ax[2].imshow(img_sobelx, cmap = 'gray')
ax[2].set_title("citra outpur")
ax[3].hist(img_sobelx.ravel(), bins =256)
ax[3].set_title("Histogram citra output")

ax[4].imshow(img_sobely, cmap = 'gray')
ax[4].set_title("citra outpur")
ax[5].hist(img_sobely.ravel(), bins =256)
ax[5].set_title("Histogram citra output")

ax[6].imshow(img_sobel, cmap = 'gray')
ax[6].set_title("citra outpur")
ax[7].hist(img_sobel.ravel(), bins =256)
ax[7].set_title("Histogram citra output")

fig.tight_layout()
plt.show()