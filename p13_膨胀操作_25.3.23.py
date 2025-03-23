# -*- coding: utf-8 -*-
# @Author :Xiaoju
# Time : 2025/3/23 下午11:10

import cv2
import numpy as np

img = cv2.imread('01_Picture/05_Dige.png')
cv2.imshow('img', img)

kernel = np.ones((5, 5), np.uint8)
erosion = cv2.erode(img, kernel, iterations=1)

cv2.imshow('erosion', erosion)

kernel = np.ones((5, 5), np.uint8)
dilate = cv2.dilate(erosion, kernel, iterations=1)

cv2.imshow('dilate', dilate)

pie = cv2.imread('01_Picture/06_pie.png')

kernel = np.ones((30, 30), np.uint8)
dilate_1 = cv2.dilate(pie, kernel, iterations=1)
dilate_2 = cv2.dilate(pie, kernel, iterations=2)
dilate_3 = cv2.dilate(pie, kernel, iterations=3)
res = np.hstack((dilate_1, dilate_2, dilate_3))
cv2.imshow('res', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
