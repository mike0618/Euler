# Spiral primes
from time import time
from sympy import isprime  # it's 20 times faster

start = time()


# def isoddprime(n):  # here is a simplified function determines if the number is prime
#     for i in range(3, int(n ** 0.5) + 1, 2):
#         if n % i == 0:
#             return False
#     return True


def e58():
    primes = 0
    point = 1
    add = 0
    ratio = 1
    while ratio > 0.1:
        add += 2
        for p in range(3):
            point += add
            if isprime(point):
                primes += 1
        point += add
        ratio = primes / (add * 2 + 1)
    return add + 1


print('The square side length for diagonal prime ratio < 10% =', e58())  # 26241
print("Runtime =", time() - start)
