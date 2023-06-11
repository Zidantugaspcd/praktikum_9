# Latihan 2 filter prewitt
# import library yang diperlukan
import cv2
import numpy as np
from matplotlib import pyplot as plt
from skimage import data
# import foto dari file penyimpanan
cute=cv2.imread("D:\SEMESTER 6\Pengolahan Citra Digital\image\hoammm.jpg")
streching = cv2.cvtColor(cute,cv2.COLOR_BGR2GRAY)
#buat prewitt
kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
# menbuat filtering pada masing masing kernel sumbu x dan y dan pada prewitt dijumlahkan nilainya
img_prewittx = cv2.filter2D(streching, -1, kernelx)
img_prewitty = cv2.filter2D(streching, -1, kernely)
img_prewitt = img_prewittx + img_prewitty

fig, axes = plt.subplots(4, 2, figsize=(20,20))
ax = axes.ravel()

ax[0].imshow(streching,cmap = 'gray')
ax[0].set_title("citra input")
ax[1].hist(streching.ravel(), bins =256)
ax[1].set_title("Histogram citra input")

ax[2].imshow(img_prewittx, cmap = 'gray')
ax[2].set_title("citra outpur prewitt x")
ax[3].hist(img_prewittx.ravel(), bins =256)
ax[3].set_title("Histogram citra output prewitt x")

ax[4].imshow(img_prewitty, cmap = 'gray')
ax[4].set_title("citra outpur prewitt y")
ax[5].hist(img_prewitty.ravel(), bins =256)
ax[5].set_title("Histogram citra output prewitt y")

ax[6].imshow(img_prewitt , cmap = 'gray')
ax[6].set_title("citra output prewitt")
ax[7].hist(img_prewitt .ravel(), bins =256)
ax[7].set_title("histogram citra output prewitt")
