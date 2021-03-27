import paillier
import modOperations as modOp
def Secure_Image_Adjustment_Brightness_Control(enc_img, v, pb):
	"""
	enc_img : encrypted image
	v : encrypted v(brightness changer)
	"""
	n,m = len(enc_img), len(enc_img[0])
	ret_img = enc_img.copy()
	for i in range(n):
		for j in range(m):
			ret_img[i][j] = paillier.homomorphicAddP(pb,enc_img[i][j],v)
	return ret_img

def Secure_Image_Adjustment_Image_negation(enc_img, l,pb):
	"""
	enc_img : encrypted image
	l : encrypted L(grey levels in the range [0,L−1].)
	"""
	l = 255
	enc_l = paillier.encrypt(pb,l)
	n,m = len(enc_img), len(enc_img[0])
	ret_img = enc_img.copy()
	for i in range(n):
		for j in range(m):
			ret_img[i][j] = paillier.homomorphicSubCC(pb,enc_l,enc_img[i][j])
	return ret_img

def Secure_Noise_Reduction_LPF(enc_img, px, py,pb):
	"""
	Mean filter, average over nearest n * m pixels patch
	enc_img : encrypted image
	px : patch lenght
	py : patch height
	"""
	n,m = len(enc_img), len(enc_img[0])
	ret_img = enc_img.copy()

	for i in range(n):
		for j in range(m):
			tmp_ij = paillier.encrypt(pb,0)
			den = 0
			for ii in range(max(0, i - px), min(n - 1, i + px)):
				for jj in range(max(0, j - py), min(m - 1, j + py)):
					den += 1
					tmp_ij = paillier.homomorphicAddC(pb,tmp_ij,enc_img[ii][jj])
			# tmp_ij = paillier.homomorphicMul(pb,tmp_ij,1/den)
			tmp_ij = (1/den)**tmp_ij
			tmp_ij = int(tmp_ij)
			tmp_ij %= pb.n2
			ret_img[i][j] = tmp_ij
	return ret_img

# def sobelOperator(enc_img,kerX,kerY,pb):
# 	ret_img = enc_img.copy()
# 	n,m = len(enc_img), len(enc_img[0])
# 	for i in range(n-2):
# 		for j in range(m-2):
# 			subMat = []
# 			for k in range(i,i+3):
# 				tmp = []
# 				for l in range(j,j+3):
# 					tmp.append(enc_img[k][l]);
# 				subMat.append(tmp)
# 			for k in range(len(kerX)):

# 			g = np.multiply(subMat,kerX)
# 			gx = np.sum(g)
# 			g = np.multiply(subMat,kerY)
# 			gy = np.sum(g)
# 			c[i][j] = min(255,np.sqrt(gx*gx+gy*gy))
# 	return c