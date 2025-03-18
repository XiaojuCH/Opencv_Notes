# -*- coding: utf-8 -*-
# @Author :Xiaoju
# Time : 2025/3/18 下午7:11

import cv2
from matplotlib import pyplot as plt

img = cv2.imread('01_Picture/01_cat.jpg')

# ret, dst = cv2.threshold(src, thresh, maxvalue, type)

# src： 输入图，只能输入单通道图像，通常来说为灰度图
# thresh： 阈值
# dst： 输出图
# ret： 阈值
# maxvalue： 当像素值超过了阈值 ( 或者小于阈值，根据 type 来决定 )，所赋予的值

# type：二值化操作的类型，包含以下5种类型：
# cv2.THRESH_BINARY           超过阈值部分取maxvalue ( 最大值 )，否则取0
# cv2.THRESH_BINARY_INV    THRESH_BINARY的反转
# cv2.THRESH_TRUNC            大于阈值部分设为阈值，否则不变
# cv2.THRESH_TOZERO          大于阈值部分不改变，否则设为0
# cv2.THRESH_TOZERO_INV  THRESH_TOZERO的反转

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret1, thresh1 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
ret2, thresh2 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV)
ret3, thresh3 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_TRUNC)
ret4, thresh4 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_TOZERO)
ret5, thresh5 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_TOZERO_INV)

titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
