#Latihan 3 filter canny
# import library yang diperlukan
import cv2
import numpy as np
from matplotlib import pyplot as plt
from skimage import data
# import foto dari file penyimpanan
cute=cv2.imread("D:\SEMESTER 6\Pengolahan Citra Digital\image\hoammm.jpg")
streching = cv2.cvtColor(cute,cv2.COLOR_BGR2GRAY)
#buat filter gambar canny
cat_canny = cv2.Canny(streching,100,200)
# buat subplots untuk masing masing gambar dan histogram
fig, axes = plt.subplots(2, 2, figsize=(20,20))
ax = axes.ravel()
# menampilkan gambar input dan histogramnya
ax[0].imshow(streching,cmap = 'gray')
ax[0].set_title("citra input")
ax[1].hist(streching.ravel(), bins =256)
ax[1].set_title("Histogram citra input")
# menampilkan gambar output bentuk canny dan histogramnya
ax[2].imshow(cat_canny, cmap = 'gray')
ax[2].set_title("citra output canny")
ax[3].hist(cat_canny.ravel(), bins =256)
ax[3].set_title("Histogram citra canny")
