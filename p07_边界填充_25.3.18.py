# -*- coding: utf-8 -*-
# @Author :Xiaoju
# Time : 2025/3/18 下午6:29

import cv2
import matplotlib.pyplot as plt

top_size, bottom_size, left_size, right_size = (50, 50, 50, 50)
img = cv2.imread("01_Picture/01_cat.jpg")

replicate = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, borderType=cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, cv2.BORDER_WRAP)
constant = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, cv2.BORDER_CONSTANT, value=[0])

plt.subplot(231), plt.imshow(img, cmap='gray'), plt.title('Original')
plt.subplot(232), plt.imshow(replicate, cmap='gray'), plt.title('Replicate')
plt.subplot(233), plt.imshow(reflect, cmap='gray'), plt.title('Reflect')
plt.subplot(234), plt.imshow(reflect101, cmap='gray'), plt.title('Reflect101')
plt.subplot(235), plt.imshow(wrap, cmap='gray'), plt.title('Wrap')
plt.subplot(236), plt.imshow(constant, cmap='gray'), plt.title('Constant')

# BORDER_REPLICATE：复制法，也就是复制最边缘像素。
# BORDER_REFLECT：反射法，对感兴趣的图像中的像素在两边进行复制例如：fedcba|abcdefgh|hgfedcb
# BORDER_REFLECT_101：反射法，也就是以最边缘像素为轴，对称，gfedcb|abcdefgh|gfedcba
# BORDER_WRAP：外包装法cdefgh|abcdefgh|abcdefg
# BORDER_CONSTANT：常量法，常数值填充。

plt.show()
