import math

class PublicKey:
	def __init__(self,n,g):
		self.n = n
		self.g = g
		self.n2 = n*n
	def __repr__(self):
		return "Public Key : (%s, %s)" %(self.n,self.g)
class PrivateKey:
	def __init__(self,l,mu):
		self.l = l
		self.mu = mu
	def __repr__(self):
		return "Private Key : (%s, %s)" %(self.l,self.mu)


def expoMod(base,exponent,mod):
	ans = 1
	while(exponent != 0 ):
		if((exponent&1)):
			ans = ans*base
			ans = ans%mod
		base = (base*base)%mod
		exponent >>= 1
	return ans

def L(x,n):
	return (x-1)//n

def generateKeypair(bits):
	p = 7
	q = 11
	n = p*q
	phi = (p-1)*(q-1)
	l = phi//math.gcd(p-1,q-1)
	g = n+1
	n2 = n*n
	while(math.gcd(expoMod(g,l,n2),n)!=1):
		g += 1
	#Inverse mod
	mu = expoMod(L(expoMod(g,l,n2),n),phi-1,n)
	return PrivateKey(l,mu), PublicKey(n,g)

def encrypt(pb,msg):
	#generate a prime
	r = 3
	while(math.gcd(r,pb.n)!=1):
		r+=1
	
	cipher = expoMod(r,pb.n,pb.n2)
	cipher = cipher*(expoMod(pb.g,msg,pb.n2))
	cipher = cipher%pb.n2
	return cipher

def decrypt(pr,pb,c):
	m = L(expoMod(c,pr.l,pb.n2),pb.n) * pr.mu
	m = m%pb.n
	return m

pr,pb = generateKeypair(5)
print(repr(pb),repr(pr))
print(encrypt(pb,14),decrypt(pr,pb,encrypt(pb,14)))