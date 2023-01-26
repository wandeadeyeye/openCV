# import library
import cv2
import random

# load the image
img = cv2.imread('assets/apple.jpg', -1)

# print the image
print(img)

# type of img
print(type(img))

# shape of img
print(img.shape)

# first roll in img
print(img[0])

# copy image
tag = img[400:700, 300:600] # copy square image
img[300:600, 550:850] = tag # paste image

# display the image
cv2.imshow('Image', img)

# save an image
cv2.imwrite('02_new_apple.jpg', img)

# wait time after image is loaded '0' = infinity, '10' = 10 seconds
cv2.waitKey(0)

# to distroy all windows
cv2.destroyAllWindows()