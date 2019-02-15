# code taken from https://qiita.com/hitomatagi/items/2c3a2bfefe73ab5c86a4

import cv2

ORG_WINDOW_NAME = "org"
GRAY_WINDOW_NAME = "gray"
CANNY_WINDOW_NAME = "canny"

IMG_FILE_NAME = "img.jpg"
GRAY_FILE_NAME = "gray.png"
CANNY_FILE_NAME = "canny.png"

org_img = cv2.imread(IMG_FILE_NAME, cv2.IMREAD_UNCHANGED)

gray_img = cv2.imread(IMG_FILE_NAME, cv2.IMREAD_GRAYSCALE)

canny_img = cv2.Canny(gray_img, 50, 110)

cv2.namedWindow(ORG_WINDOW_NAME)
cv2.namedWindow(GRAY_WINDOW_NAME)
cv2.namedWindow(CANNY_WINDOW_NAME)

cv2.imshow(ORG_WINDOW_NAME, org_img)
cv2.imshow(GRAY_WINDOW_NAME, gray_img)
cv2.imshow(CANNY_WINDOW_NAME, canny_img)

cv2.imwrite(GRAY_FILE_NAME, gray_img)
cv2.imwrite(CANNY_FILE_NAME, canny_img)

print('Press 0 to quit')
cv2.waitKey(0)
cv2.destroyAllWindows()
