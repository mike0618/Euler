# Truncatable primes
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


def trunc(s):  # here is a function determines the truncatable prime
    ls = len(s)
    if ls > 1 and s[0] != 1 and s[0] != 9 and s[-1] != 1 and s[-1] != 9 and isprime(int(s)):
        for i in range(1, ls):
            if not isprime(int(s[i:])) or not isprime(int(s[:-i])):
                return False
        return True
    return False


def e37():
    cnt = 11
    digits = 1
    sump = 0
    while cnt != 0:
        for p in itertools.product('1379', repeat=digits):  # 1,3,7,9 digits are acceptable
            strn = ''
            for d in p:
                strn += d
            if trunc(strn):
                cnt -= 1
                sump += int(strn)
                print(strn)
            if trunc('2' + strn):  # 2 and 5 are acceptable as first digit, check them too
                cnt -= 1
                sump += int('2' + strn)
                print('2' + strn)
            if trunc('5' + strn):
                cnt -= 1
                sump += int('5' + strn)
                print('5' + strn)
        digits += 1

    return sump


print('Sum of truncatable primes =', e37())  # 748317
end = time() - start
print("Runtime =", end)
