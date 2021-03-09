# Summation of primes
from time import time
import sympy

n = int(input("Enter a max of prime: "))
start = time()


def e10():
    if n >= 3:
        sump = 5
        for i in range(5, n + 1, 2):
            for j in range(3, int(i ** 0.5) + 1, 2):
                if i % j == 0:
                    break
            else:
                sump += i
    elif n == 2:
        sump = 2
    else:
        sump = 0
    return sump


print(f"The sum of all primes below {n} =", e10())  # if n = 2000000, the sum is 142913828922
print('Runtime =', time() - start)
start2 = time()
print('The sum with sympy lib =', sum(sympy.primerange(2, n)))  # with sympy it's 2 times faster when n = 2000000
print('Runtime with sympy lib =', time() - start2)
