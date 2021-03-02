# Goldbach's other conjecture
from time import time

start = time()


def e46():
    odd = 9
    primes = [2, 3, 5, 7]
    while True:
        ispr = True
        cant = True
        for p in primes:
            if not odd % p:
                ispr = False
            if not ((odd - p) / 2) ** 0.5 % 1:
                cant = False
        if ispr:
            primes.append(odd)
        if cant and not ispr:
            return odd
        odd += 2


print('The smallest odd =', e46())  # 5777
print('Runtime =', time() - start)
