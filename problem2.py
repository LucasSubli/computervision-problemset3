# USAGE
# python problem2.py --image image/image1.jpg

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
(width, height) = grey.shape
filtered = grey

#As the problem requests we will it from n=0 to n=30
for i in range(0,31):

	#preallocate some memory
	cmFiltered = np.zeros((256, 256))
	cmResidual = np.zeros((256, 256))
	residual = grey - filtered;

	#Calculate the co-occurrence matrix
	for x in range(0,width-1):
		for y in range(0,height-1):
			#coocurrence matrix of the filtered image
			cmFiltered[filtered[x,y], filtered[x+1,y]] += 1
			cmFiltered[filtered[x,y], filtered[x-1,y]] += 1
			cmFiltered[filtered[x,y], filtered[x,y+1]] += 1
			cmFiltered[filtered[x,y], filtered[x,y-1]] += 1

			#Coocurrence matrix of the residual image
			cmResidual[residual[x,y], residual[x+1,y]] += 1
			cmResidual[residual[x,y], residual[x-1,y]] += 1
			cmResidual[residual[x,y], residual[x,y+1]] += 1
			cmResidual[residual[x,y], residual[x,y-1]] += 1

	#preallocate more memory
	homogeneityFiltered = 0
	homogeneityResidual = 0
	uniformityFiltered = 0
	uniformityResidual = 0
	#get the sum of the elements on coocurrence matrixes
	nFiltered = cmFiltered.sum()
	nResidual = cmResidual.sum()


	#Get some insight from the matrixes
	for x in range(0,256):
		for y in range(0,256):
			#As defined on the slides provided =
			p = cmFiltered[x,y]/nFiltered
			homogeneityFiltered += (p)/(1 + abs(x-y))
			uniformityFiltered += p ** 2

			p = cmResidual[x,y]/nResidual
			homogeneityResidual += (p)/(1 + abs(x-y))
			uniformityResidual += p ** 2

	#print it all as a CSV
	print(
		str(i) + "," + 
		str(homogeneityFiltered) + "," +
		str(uniformityFiltered) + "," + 
		str(homogeneityResidual) + "," + 
		str(uniformityResidual))

	#update the blurred image for the next iteration
	filtered = cv2.boxFilter(filtered, -1, (3,3))

cv2.imshow("Blurred", filtered)
cv2.imshow("Residual", residual)
cv2.waitKey(0)
cv2.destroyAllWindows()