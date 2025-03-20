# -*- coding: utf-8 -*-
# @Author :Xiaoju
# Time : 2025/3/18 下午7:41

import cv2

img = cv2.imread('01_Picture/04_LenaNoise.png')

cv2.imshow('Lena Noise', img)
print(img.shape)

# 均值滤波
# 简单的平均卷积操作
# 不会改变图像大小，意思就是3*3的卷积核只会一次改变卷积核中间的那一个像素，使其变成均值
blur = cv2.blur(img, (3, 3))
print(blur.shape)
cv2.imshow('Blur', blur)

# 方框滤波
# 基本和均值一样，可以选择归一化
box1 = cv2.boxFilter(img, -1, (3, 3), normalize=True)
cv2.imshow('Box1', box1)
# 归一化就是超过255就自动余255
# 如下box2就是没有进行归一化(已亮瞎)
box2 = cv2.boxFilter(img, -1, (3, 3), normalize=False)
cv2.imshow('Box2', box2)
cv2.waitKey(0)
