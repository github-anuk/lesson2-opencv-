import cv2 
import numpy as np 
image1=cv2.imread("ash.png")
image2=cv2.imread("pika1.png")
result=cv2.subtract(image1,image2)

cv2.imshow("subtracted image",result)

cv2.waitKey(0)
cv2.destroyAllWindows()