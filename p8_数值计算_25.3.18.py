# -*- coding: utf-8 -*-
# @Author :Xiaoju
# Time : 2025/3/18 下午6:45

import cv2

img_cat = cv2.imread('01_Picture/01_cat.jpg')
img_dog = cv2.imread('01_Picture/03_dog.jpg')

# 图片直接加10 相当于全部像素都加10
img_cat2 = img_cat + 10
print(img_cat[:5, :, 0])
print("............我是分割线............")
print(img_cat2[:5, :, 0])
print("............我是分割线............")

# 所以两张图片直接相加就相当于直接相加 再余256
print((img_cat + img_cat2)[:5, :, 0])
print("............我是分割线............")

# cv2.add就只取到最大的255
print(cv2.add(img_cat, img_cat2)[:5, :, 0])
print("............我是分割线............")

# 图像融合
# 因为狗图和猫片的shape(H, W, C)不同，所以需要调整大小才能融合
print(img_cat.shape)

# 注意这里的cv2.resize的维度是 W, H
img_dog = cv2.resize(img_dog, (500, 414))
print(img_dog.shape)

cv2.imshow('origin_catdog', img_cat + img_dog)

res = cv2.addWeighted(img_cat, 0.4, img_dog, 0.6, 0)
cv2.imshow('catdog', res)

cv2.waitKey(0)
