import cv2
import numpy as np 
import imutils
import sys

#Display the images
# cv2.imshow('Original Image', original_image)
# cv2.imshow('Resized Image', resized_image)
# cv2.imshow('Gray Image', grayscale_image)
# cv2.imshow('Denoised Image', denoised_image)
# cv2.imshow('Edges', edges)


def identifyNumberplateArea(edges,resized_image):
    print("***Finding the numberplate section")
    try:
        contours, hierarchy=cv2.findContours(edges,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

        for c in contours:
                peri = cv2.arcLength(c, True)
                approx = cv2.approxPolyDP(c, 0.02 * peri, True)
                if len(approx) == 4:  
                    NumberPlateCnt = approx 
                    break

        cv2.drawContours(resized_image, [NumberPlateCnt], -1, (0,255,0), 3)# # Drawing the selected contour on the original image
        cv2.imshow("Final Image With Number Plate Detected", resized_image)
        
        # print(contours)
        # print('Numbers of contours found=' + str(len(contours)))

        cv2.drawContours(resized_image,contours,-1,(0,255,0),3)
        cv2.imshow('contours',resized_image)
    except Exception as e:
        print("Error..",e)
        sys.out()

def cleanImage():
    print('***image cleaning***')
    try: 
        original_image = cv2.imread('images/car.jpg',1)#read the image
        resized_image = imutils.resize(original_image, width=500) # resize original image (width = 500)
        grayscale_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY) #grayscale
        denoised_image = cv2.medianBlur(grayscale_image, 3)#denoising
        edges = cv2.Canny(denoised_image,100,200)#denoising
        print('***image successfully cleaned***')
        identifyNumberplateArea(edges, resized_image)

    except FileNotFoundError as f:
        print("Error..",f)
        sys.out()


def main():
    cleanImage()
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()