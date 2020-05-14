


import numpy as np
import cv2





# load the image
image = cv2.imread("redcar.png")

# define the color bounds
blue = [
	([86, 31, 4], [220, 88, 50])
]
red = [
    ([0, 20, 100], [68, 70, 220])
]
green = [
    ([0, 45, 0], [65, 255, 65])
]


def dec(color):
	for (lower, upper) in color:
		# create NumPy arrays from the boundaries 
		lower = np.array(lower, dtype = "uint8")
		upper = np.array(upper, dtype = "uint8")

		
		mask = cv2.inRange(image, lower, upper)
		output = cv2.bitwise_and(image, image, mask = mask)
		ret,thresh=cv2.threshold(output,0,200,cv2.THRESH_BINARY_INV)
 	
	 
		cv2.imshow("output",thresh)

		area = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)

		print('area =', cv2.countNonZero(area))
		return(area)

bluearea=dec(blue)
greenarea=dec(green)
redarea=dec(red)
	
ba = np.sum(bluearea)
ga = np.sum(greenarea)
ra = np.sum(redarea)
print(ba, ga, ra)


if (ba >= ra) and (ba >= ga): 
	maincolor = ("blue")
	
if (ra >= ba) and (ra >= ga): 
	maincolor = ("red")
	
if (ga >= ba) and (ga >= ra): 
	maincolor = ("green")
	
 

print(maincolor)

cv2.waitKey(0)