import cv2
import numpy as np 
# import imutils

#read the image
original_image = cv2.imread('images/car.jpg',1)

#resize original image (width = 500)
# resized_image = imutils.resize(original_image, width=500)

#grayscale
grayscale_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
#denoising
denoised_image = cv2.medianBlur(grayscale_image, 3)

#edges
edges = cv2.Canny(denoised_image,100,200)

#Display the original image
cv2.imshow('Original Image', original_image)

#Display the resized image
# cv2.imshow('Resized Image', resized_image)

#Display the grayscale image
cv2.imshow('Gray Image', grayscale_image)
#Display the denoised image
cv2.imshow('Denoised Image', denoised_image)

cv2.imshow('Edges', edges)

cv2.waitKey(0)
cv2.destroyAllWindows()