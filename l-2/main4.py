import cv2 
import numpy as np 

img=cv2.imread("pika1.png")
cv2.imshow("OG",img)

kernel = np.ones((5,5), np.uint8)
print(kernel)

image = cv2.erode(img,kernel)
cv2.imshow("eroded image",image)

cv2.waitKey(0)
cv2.destroyAllWindows()