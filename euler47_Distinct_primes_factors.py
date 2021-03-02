# Distinct primes factors
from time import time

start = time()


def pfactors(n):  # here is the function returns prime factors
    pfs = []
    p = 2
    while p * p <= n:  #
        if not n % p:
            if len(pfs) > 0 and not pfs[-1] % p:
                pfs[-1] *= p
            else:
                pfs.append(p)
            n //= p
        elif p == 2:
            p += 1
        else:
            p += 2
    if n > 1:
        if len(pfs) > 0 and not pfs[-1] % n:
            pfs[-1] *= n
        else:
            pfs.append(n)
    return pfs


def e47():
    n = 123845  # 16th prime is 53, so here is the middle: 47*31*17*5, and it's 10 times faster
    total = 0
    while total < 4:
        pfsn = pfactors(n)
        if not len(pfsn) % 4:
            total += 1
        else:
            total = 0
        n += 1
    return n - 4


print(e47())  # 134043
print('Runtime =', time() - start)
