# Longest Collatz sequence
import time
start = time.time()
def e14():
	nmax=0
	lmax=2
	for sn in range(3,1000000,2):
		l=1
		n=sn
		while n>1:
			if n%2==0:
				n=n/2
			else:
				n=n*3+1
			l+=1
		if l>lmax:
			lmax=l
			nmax=sn
	print("The longest chain number is:", nmax)
	print("Chain length is:", lmax)
	end = time.time() - start
	print("Runtime =", end)
e14()
