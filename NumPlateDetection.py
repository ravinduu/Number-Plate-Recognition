import cv2
import numpy as np 

#read the image
original_image = cv2.imread('./images/car.png')

#Display the original image
cv2.imshow('Original Image', original_image)

cv2.waitKey(0)