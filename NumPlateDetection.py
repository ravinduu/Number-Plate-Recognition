import cv2
import numpy as np 

#read the image
original_image = cv2.imread('./images/car.png')

#Display the original image
cv2.imshow('Original Image', original_image)

#resize original image (width = 500)
resized_image = imutils.resize(original_image, width=500)

#Display the resized image
cv2.imshow('Resized Image', resized_image)

#grayscale
grayscale_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

#Display the grayscale image
cv2.imshow('Gray Image', grayscale_image)

cv2.waitKey(0)
cv2.destroyAllWindows()