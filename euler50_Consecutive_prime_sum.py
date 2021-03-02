# Consecutive prime sum
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


def e50():
    prs = [2, 3, 5, 7]
    n = prs[-1] + 2
    while sum(prs) < 1000000:
        for p in prs:
            if not n % p:
                break
        else:
            prs.append(n)
        n += 2
    a = len(prs[:-1]) - 1
    for i in range(a, 0, -2):  # here is the "window"-method
        for j in range(a - i + 1):
            sump = sum(prs[1 + j:i + j + 1])
            if j == 0 and isprime(sump + 2):
                return sump + 2
            if isprime(sump):
                return sump


print('Prime =', e50(), 'is the longest sum of consecutive primes')  # 997651
print('Runtime =', time() - start)
