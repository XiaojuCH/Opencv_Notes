import cv2

img = cv2.imread("01_Picture/01_cat.jpg")
print(img)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
