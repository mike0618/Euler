def e9():
	for a in range(2,500):
		for b in range(a,500):
			if a**2 + b**2 == (1000-(a+b))**2:
				pr=a*b*(1000-(a+b))
				print('a =', a)
				print('b =', b)
				print('c =', 1000-(a+b))
				print('a*b*c =', pr)
				return pr
e9()
