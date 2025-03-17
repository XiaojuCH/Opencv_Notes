import cv2


def cv_show(name, img):
    cv2.imshow(name, img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    print(img.shape)


cv_show('image', cv2.imread('01_Picture/01_cat.jpg'))

image = cv2.imread('01_Picture/01_cat.jpg', cv2.IMREAD_GRAYSCALE)
cv_show('gray', image)  # 用灰度图后通道数为0了
cv2.waitKey(0)
cv2.destroyAllWindows()
