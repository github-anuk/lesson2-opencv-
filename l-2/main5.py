import cv2 

img = cv2.imread("pika1.png",1)
cv2.imshow("OG ",img)

# Gaussian Blur - used mostly in machine learning preprocessing steps
#Gaussian blur describes blurring an image by a Gaussian function. 
#It is a widely used effect in graphics software, typically to reduce image noise and reduce detail.

#(img, Kernal_size ,std_dev)

# Median Blur -widely used in digital image processing because, under certain conditions, 
# it preserves edges while removing noise.

#(img,Kernal_size)
# Bilateral Blur - only sharp edges are preserved here
#(img,diameter of each pixel neighborhood,sigmaColor,sigmaSpace)

Gaussian = v=cv2.GaussianBlur(img,(7,7),0)
cv2.imshow("gaussian bluring",Gaussian)

median = v=cv2.medianBlur(img,5)
cv2.imshow("median blur",median)


bilateral = v=cv2.bilateralFilter(img,9,75,75)
cv2.imshow("bilateral bluring",bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows()

bilateral = v=cv2.bilateralFilter(img,9,75,75)
cv2.imshow("bilateral bluring",bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows()