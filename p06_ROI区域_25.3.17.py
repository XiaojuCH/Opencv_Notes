import cv2

#  ROI == Region of interest 你感兴趣的区域

img = cv2.imread("01_Picture/01_cat.jpg")
cat = img[0:200, 0:200]

b, g, r = cv2.split(cat)
# 此处自夸一下，刚学到列表和循环就用上了~
channel = [b, g, r]
for i in range(3):
    print(channel[i].shape)

image = cv2.merge((b, g, r))
print(image.shape)

cv2.imshow("cat", cat)

# 只保留R
onlyR = img.copy()
onlyR[:, :, 0] = 0
onlyR[:, :, 1] = 0
cv2.imshow("onlyR", onlyR)

# 只保留G
onlyG = img.copy()
onlyG[:, :, 0] = 0
onlyG[:, :, 2] = 0
cv2.imshow("onlyG", onlyG)

# 只保留B
onlyB = img.copy()
onlyB[:, :, 1] = 0
onlyB[:, :, 2] = 0
cv2.imshow("onlyB", onlyB)

cv2.waitKey(0)
cv2.destroyAllWindows()
