# Prime digit replacements
from time import time

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


def e51():
    """
    The simple math analyze shows: if we would replace 1 or 2 digits,
    we would exactly get 3 numbers divisible by 3,
    because we increase the sum of digits in the number
    Consequently we can not get 8 primes this way.
    Let's check 3-digit replacing!
    """

    n = 56993
    while True:
        n += 2
        for p in range(3, int(n ** 0.5) + 1, 2):
            if not n % p:
                break
        else:
            for d in ['0', '1', '2']:
                sn = str(n)
                if sn[:-1].count(d) == 3:  # last digit exception - 5 evens aren't prime!
                    cnt = 1
                    for i in range(int(d) + 1, 10):
                        rep = sn[:-1].replace(d, str(i)) + sn[-1]
                        if isprime(int(rep)):
                            cnt += 1
                            if cnt == 8:
                                return sn


print('Prime =', e51())  # 121313
print('Runtime =', time() - start)
