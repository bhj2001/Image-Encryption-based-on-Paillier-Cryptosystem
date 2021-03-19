import cv2
import paillier
import numpy as np
path = 'images/a.png'
path = 'images/acolor.tiff'
# path = 'images/1000px-image.jpg'
img = cv2.imread(path,1)
c = np.copy(img)
pr,pb = paillier.generateKeypair(5)
bb = []
mod = 256
for i in range(len(c)):
	bb.append([0]*len(c[i]))
	for j in range(len(c[i])):
		bb[i][j] = [0]*3
		for k in range(3):
			E = paillier.encrypt(pb,int(c[i][j][k]))
			bb[i][j][k] = E//mod
			c[i][j][k] = E%mod
cv2.imshow('Encrypted',c)
m = np.copy(c)
bc = 5
for i in range(len(c)):
	for j in range(len(c[i])):
		for k in range(3):
			m[i][j][k] = paillier.decrypt(pr,pb,int(bb[i][j][k]*mod)+int(c[i][j][k]))

cv2.imshow('Decrypted',m)
cv2.waitKey(0)
cv2.destroyAllWindows()
