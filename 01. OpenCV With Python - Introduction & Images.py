# import library
import cv2

# load the image
img = cv2.imread('assets/apple.jpg', -1)

# '-1' cv2.IMREAD_COLOR: loads a color image. any transparency will be neglected. it is the default flag
#  '0' cv2.IMREAD_GRAYSCALE: loads images in a grayscale mode
#  '1' cv2.IMREAD_UNCHANGED: loads image as such including alpha channel 

# resize an image
img = cv2.resize(img, (0,0), fx= 0.6, fy= 0.6)

# rotating an image clockwise
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

# save an image
cv2.imwrite('new_apple.jpg', img)

# display the image
cv2.imshow('Image', img)

# wait time after image is loaded '0' = infinity, '10' = 10 seconds
cv2.waitKey(0)

# to distroy all windows
cv2.destroyAllWindows()