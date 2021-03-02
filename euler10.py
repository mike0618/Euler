import time
n=int(input("Enter a max of prime: "))
start = time.time()
def e10(n):
	if n>=3:
		sump=5
		for i in range(5,n+1,2):
			for j in range(3,int(i**0.5)+1,2):
				if i%j==0:
					break
			else:
				sump+=i
	elif n==2:
		sump=2
	else: sump=0
	print(f"The sum of all primes below {n} =", sump)
	end = time.time() - start
	print("Runtime =", end)
e10(n)
