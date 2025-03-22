# -*- coding: utf-8 -*-
# @Author :Xiaoju
# Time : 2025/3/22 下午12:45

import cv2
import numpy as np

img = cv2.imread('01_Picture/05_Dige.png')

cv2.imshow('img', img)

kernel = np.ones((5, 5), np.uint8)
erosion = cv2.erode(img, kernel, iterations=1)  # iterations 迭代次数
cv2.imshow('erosion', erosion)

pie = cv2.imread('01_Picture/06_pie.png')

cv2.imshow('pie', pie)

kernel = np.ones((30, 30), np.uint8)
erosion_1 = cv2.erode(pie, kernel, iterations=1)
erosion_2 = cv2.erode(pie, kernel, iterations=2)
erosion_3 = cv2.erode(pie, kernel, iterations=3)
res = np.hstack((erosion_1, erosion_2, erosion_3))
cv2.imshow('res', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
