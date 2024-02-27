import cv2 

img = cv2.imread("pika1.png",1)
cv2.imshow("OG ",img)

resized= cv2.resize(img,(500,250))
cv2.imshow("reduced image",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()