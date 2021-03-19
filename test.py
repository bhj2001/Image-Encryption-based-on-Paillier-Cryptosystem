def L(x,n):
	return (x-1)//n
def modinv(base,expo,mod):
	return (base**expo)%mod
import math

def modInverse(a, m):
    m0 = m
    y = 0
    x = 1
    if (m == 1):
        return 0
    while (a > 1):
        q = a // m
        t = m
        m = a % m
        a = t
        t = y
        y = x - q * y
        x = t
    if (x < 0):
        x = x + m0
    return x
p = 7
q = 11
n = p*q
n2 = n*n
lam = ((p-1)*(q-1))//math.gcd(p-1,q-1)
print(lam,n2)
for g in range(2,3,1):
	# g = 8
	g = n+1
	mu = L((g**lam)%n2,n)
	# if(mu>=n):
	# 	continue
	bc = mu
	print(mu)
	# mu = modinv(mu,n-2,n)%nmu
	mu = (mu**(((p-1)*(q-1)-1)))%n
	# mu = modInverse(mu,n)
	# if((bc*mu)%n!=1):
	# 	continue
	m = 14
	r = 3
	c = ((g**m)*(r**n))%n2
	print(bc,mu,g**m%n2,r**n%n2)
	d = (L((c**lam)%n2,n)*mu)%n
	print("ye dekh",g,lam,n,(p-1)*(q-1))
	if(m==d):
		print(bc,mu,(bc*mu)%n)
		# print(math.gcd(bc,n),bc)
		print("hhloo",m,c)