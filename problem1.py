# USAGE
# python problem1.py --image image/image1.jpg

# import the necessary packages
import numpy as np
import argparse
from matplotlib import pyplot as plt
import math
import cv2


# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
	help = "Path to the image to be scanned")
args = vars(ap.parse_args())


#Loading the image and making it a grey level one
image = cv2.imread(args["image"])
grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#threshold the grey level image to make it binary
tret,thresh = cv2.threshold(grey,127,255,cv2.THRESH_BINARY)

#COunt the blackpizels
blackPixels = (thresh == 0).sum();

#The n of white pixels is the diference between total and black
print("Black Pixels Count: " + str(blackPixels))
print("White Pixels Count: " + str(thresh.size - blackPixels))

#Run edge detection on the thresholded image
edged = cv2.Canny(thresh, 75, 200)

#find the countours
(_, cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

#sort the countours by size
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)

# loop over the contours
for c in cnts:

	#create a copy of the image to make iteration easier
	imgCopy = image.copy()

	#print the header
	print("\n\n\n")
	print("COUNTOUR INFO")
	# approximate the contour
	peri = c.size
	print("Perimeter: " + str(peri))
	#get the area
	area = cv2.contourArea(c)
	print("Area: " + str(math.ceil(area)))

	#Find the minimum enclosing circle
	(x,y),radius = cv2.minEnclosingCircle(c)
	center = (int(x),int(y))
	radius = int(radius)
	cv2.circle(imgCopy,center,radius,(0,0,255),2)
	print("Diameter: " + str(2*radius))

	#draw all of that
	cv2.drawContours(imgCopy, c, -1, (0, 255, 0), 2)
	cv2.imshow("Original Image", imgCopy)
	cv2.waitKey(0)

cv2.destroyAllWindows()