# Circular primes
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


def e35():
    cnt = 13  # circular primes below 100
    digits = 3  # go from 100, lowest 3-digit number
    while digits <= 6:  # to highest 6-digit number 999999
        for p in itertools.product('1379', repeat=digits):  # 1,3,7,9 digits are acceptable only
            strn = ''
            for d in p:
                strn += d
            for i in range(0, digits):  # circulation is here
                sn = strn[i:] + strn[:i]
                if not isprime(int(sn)):
                    break
            else:
                cnt += 1
        digits += 1

    return cnt


print('Circular primes =', e35())  # 55
end = time() - start
print("Runtime =", end)
