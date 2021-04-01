import cv2
import paillier
import numpy as np
import ImageOperations as cryp
path = 'images/a.png'
# path = 'images/acolor.tiff'
# path = 'images/1000px-image.jpg'
img = cv2.imread(path,0)
c = np.copy(img)
naive = np.copy(img)
pr,pb = paillier.generateKeypair(9)
print(pb,pr)
bb = []
mod = 256
for i in range(len(c)):
	bb.append([0]*len(c[i]))
	for j in range(len(c[i])):
		E = paillier.encrypt(pb,int(c[i][j]))
		bb[i][j] = E
		c[i][j] = E%mod
# cv2.imshow('Encrypted',c)
m = np.copy(c)
bc = 5
for i in range(len(c)):
	for j in range(len(c[i])):
		m[i][j] = paillier.decrypt(pr,pb,int(bb[i][j]))
			# m[i][j][k] = paillier.decrypt(pr,pb,int(bb[i][j][k]*mod)+int(c[i][j][k]))
v = 100
# xx = cryp.Secure_Image_Adjustment_Brightness_Control(bb,v,pb)
# xx = cryp.Secure_Image_Adjustment_Image_negation(bb,v,pb)
xx = cryp.Secure_Noise_Reduction_LPF(bb,1,1,pb)
for i in range(len(c)):
	for j in range(len(c[i])):
		m[i][j] = min(255,paillier.decrypt(pr,pb,xx[i][j]))
		# print(paillier.decrypt(pr,pb,xx[i][j]))
		# exit()
		naive[i][j] = max(0,255-img[i][j])
# cv2.imshow('Naive',naive)
cv2.imshow('Pasys',m)
cv2.waitKey(0)
cv2.destroyAllWindows()
