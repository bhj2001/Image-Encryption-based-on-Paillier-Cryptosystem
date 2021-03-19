def expoMod(base,exponent,mod):
	ans = 1
	while(exponent != 0 ):
		if((exponent&1)):
			ans = ans*base
			ans = ans%mod
		base = (base*base)%mod
		exponent >>= 1
	return ans