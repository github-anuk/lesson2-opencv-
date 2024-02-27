import cv2 
import numpy as np 
image1=cv2.imread("ash.png")
image2=cv2.imread("pika1.png")
weightedsum=cv2.addWeighted(image1,0.5,image2,0.4,0)

cv2.imshow("weighited image",weightedsum)

cv2.waitKey(0)
cv2.destroyAllWindows()