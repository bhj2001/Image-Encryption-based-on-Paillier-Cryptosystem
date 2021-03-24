import cv2
import paillier
import numpy as np
import math
path = 'images/a.png'
# path = 'images/acolor.tiff'
img = cv2.imread(path,0)
img = cv2.GaussianBlur(img,(3,3),0)
# sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)  # x
# sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)
kerX = [[1,0,-1],[2,0,-2],[1,0,-1]]
kerY = [[1,2,1],[0,0,0],[-1,-2,-1]]

maxi = 1
def sobelOperator(img):
	c = np.copy(img)
	c.fill(0)
	for i in range(len(img)-2):
		for j in range(len(img[i])-2):
			subMat = []
			for k in range(i,i+3):
				tmp = []
				for l in range(j,j+3):
					tmp.append(img[k][l]);
				subMat.append(tmp)
			g = np.multiply(subMat,kerX)
			gx = np.sum(g)
			g = np.multiply(subMat,kerY)
			gy = np.sum(g)
			c[i][j] = min(255,np.sqrt(gx*gx+gy*gy))
	return c

cv2.imshow('Original',img)
cv2.imshow('Sobel',sobelOperator(img))
cv2.waitKey(0)
cv2.destroyAllWindows()