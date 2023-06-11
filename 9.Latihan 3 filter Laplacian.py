#Latihan 3 filter Laplacian
# import library yang diperlukan
import cv2
import numpy as np
from matplotlib import pyplot as plt
from skimage import data
# import foto dari file penyimpanan
cute=cv2.imread("D:\SEMESTER 6\Pengolahan Citra Digital\image\hoammm.jpg")
# dikonversi gambar menjadi bentuk grayscale
streching = cv2.cvtColor(cute,cv2.COLOR_BGR2GRAY)
# dihiangkan noise dengan gaussian blur
fill_gaussian = cv2.GaussianBlur(streching,(3,3),0)
# konvolusi dengan kernel
fill_Laplacian = cv2.Laplacian(fill_gaussian,cv2.CV_64F)
# tampilkan gambar
fig, axes = plt.subplots(2, 2, figsize=(20,20))
ax = axes.ravel()
# menampilka gambar asli dengan gausian fillter agar memperhalus citra berikut histogramnya
ax[0].imshow(fill_gaussian,cmap = 'gray')
ax[0].set_title("citra gaussian")
ax[1].hist(fill_Laplacian.ravel(), bins =256)
ax[1].set_title("Histogram citra gaussian")
# menampilkan hasil dan histogram dari gambar setelah di ubah dalam bentuk laplacian
ax[2].imshow(fill_Laplacian, cmap = 'gray')
ax[2].set_title("citra output laplacian")
ax[3].hist(fill_Laplacian.ravel(), bins =256)
ax[3].set_title("Histogram citra laplacian")