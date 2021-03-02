# Large sum. The first ten digits of the sum of the following 100 50-digit numbers.
def e13():
	f=open("100x50digits.txt")
	summ=0
	for line in f:
		summ+=int(line[:11])
	print(int(summ/1000))
	f.close()
e13()
