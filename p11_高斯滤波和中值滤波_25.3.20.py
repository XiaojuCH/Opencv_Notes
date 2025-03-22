# -*- coding: utf-8 -*-
# @Author :Xiaoju
# Time : 2025/3/20 下午8:01

import cv2
import numpy as np


img = cv2.imread('01_Picture/04_LenaNoise.png')

cv2.imshow('Lena Noise', img)
print(img.shape)

# 高斯滤波
# 高斯模糊的卷积核里的数值是满足高斯分布，相当于更重视中间的
# 就是正态分布，离卷积核中间距离越近，权重越大

gauss = cv2.GaussianBlur(img, (5, 5), 1)
# cv2.imshow('Gaussian Blur', gauss)

# 中值滤波
# 相当于用中值代替
median = cv2.medianBlur(img, 5)

# cv2.imshow('Median Blur', median)

res = np.hstack((gauss, median))
print(res)
cv2.imshow('gauss VS median', res)
cv2.waitKey(0)
