# USAGE
# python problem3.py --image image/image1.jpg

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
tret,thresh = cv2.threshold(grey,127,255,cv2.THRESH_BINARY)

blackPixels = (thresh == 0).sum();

print("Black Pixels Count: " + str(blackPixels))
print("White Pixels Count: " + str(thresh.size - blackPixels))

edged = cv2.Canny(thresh, 75, 200)

(_, cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

cnts = sorted(cnts, key = cv2.contourArea, reverse = True)

# loop over the contours
for c in cnts:
	imgCopy = image.copy()

	print("\n\n\n")
	print("COUNTOUR INFO")
	# approximate the contour
	peri = c.size
	print("Perimeter: " + str(peri))

	area = cv2.contourArea(c)
	print("Area: " + str(math.ceil(area)))


	(x,y),radius = cv2.minEnclosingCircle(c)
	center = (int(x),int(y))
	radius = int(radius)
	cv2.circle(imgCopy,center,radius,(0,0,255),2)
	print("Diameter: " + str(2*radius))


	

	cv2.drawContours(imgCopy, c, -1, (0, 255, 0), 2)
	cv2.imshow("Original Image", imgCopy)
	cv2.waitKey(0)
	

# show the contour (outline) of the piece of paper
# cv2.imshow("Original Image", image)
# cv2.drawContours(image, cnts, -1, (0, 255, 0), 2)
# cv2.imshow("Countours", image)
cv2.destroyAllWindows()

# # mouse events for the image
# def on_mouse_click(event,x,y,flags,param):
# 	#define the k for the window size (will be 2k +1, 41 in this case)
# 	if event == cv2.EVENT_LBUTTONDOWN:
# 		img = cv2.imread(args["image"])
# 		img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 		img = threshold_adaptive(img, 251, offset = 10)

# 		#we have to use copy to avoid pointers interfering with edge detection after
# 		#we draw the rectangle in the next few lines
# 		img2 = img.copy()[y-size:y+size, x-size:x+size]

# 		#Draw the window
# 		cv2.rectangle(img,(x-size,y+size),(x+size,y-size), (0, 255, 0), 2)
# 		cv2.imshow("Image2", img)

# 		#take the DFT
# 		dft = cv2.dft(np.float32(img2),flags = cv2.DFT_COMPLEX_OUTPUT)
# 		#Avoid the warning of log 0
# 		dft[dft == 0] = 0.0000001

# 		#Take the magnitude and phases
# 		magnitudeWindow, phaseWindow = 20*np.log(cv2.cartToPolar(dft[:,:,0],dft[:,:,1]))

# 		#Apply some edge detection on the image
# 		img2 = cv2.Canny(img2,100,200)

# 		#Apply some edge detection on the magnitude
# 		slicemagnitude = np.uint8(magnitudeWindow)
# 		magnitude2 = cv2.Canny(slicemagnitude,100,300)

# 		#Apply some edge detection on the phase
# 		slicephase = np.uint8(phaseWindow)
# 		phase2 = cv2.Canny(slicephase,100,300)

# 		#Print all the edge detections
# 		cv2.imshow("Spacial", img2)
# 		cv2.imshow("Magnitude", magnitude2)
# 		cv2.imshow("Phase", phase2)

# 		#Threshold everything for the nfinal result
# 		img2 = img2[img2>150]
# 		magnitude2 = magnitude2[magnitude2>150]
# 		phase2 = phase2[phase2>150]

# 		#Print the info we are looking for
# 		print('Window edges = ',img2.size)
# 		print('Magnitude edges = ',magnitude2.size)
# 		print('Phase edges = ',phase2.size)
		
# 		#helper text
# 		print('Click on the image or press ENTER to exit\n')

# #draw the initial window
# cv2.namedWindow('Image2')

# #prepare the mouse callback
# cv2.setMouseCallback('Image2',on_mouse_click)

# #helper info
# print('Click on the image or press ENTER to exit\n')

# #keep the program running
# while(1):
# 	cv2.imshow('Image2',img)
# 	k = cv2.waitKey(0)
# 	if k:
# 		break

# #destroy all windows
# cv2.destroyAllWindows()
		