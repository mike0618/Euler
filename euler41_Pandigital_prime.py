# Pandigital prime
from time import time
import itertools

start = time()


def isprime(n):  # here is a function determines if the number is prime
    if n == 2:
        return True
    if n > 2 and n % 2 != 0:
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    return False


def e41():
    ds = '987654321'
    for n in range(9, 0, -1):
        digits = ds[len(ds) - n:]
        if sum(int(d) for d in digits) % 3 == 0:  # if sum of digits is divisible by 3, the number is too
            continue
        for p in itertools.permutations(digits, n):
            s = ''
            for d in p:
                s += d
            if isprime(int(s)):
                return s


print('The largest pandigital prime =', e41())  # 7652413
print('Runtime =', time() - start)
