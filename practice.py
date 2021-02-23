import cv2

orig_img = cv2.imread('assets/image 1.jpg', 1)
img = cv2.resize(orig_img, (0,0), fx=2, fy=2)
cv2.imwrite('new_img.jpg',img)

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()