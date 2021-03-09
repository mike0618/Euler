# The largest prime factor
from time import time

start = time()


def e3(n):
    d = 2
    while d * d <= n:
        if n % d == 0:
            n //= d
        elif d == 2:
            d += 1
        else:
            d += 2
    return n


print(e3(600851475143))  # 6857
print('Runtime:', time() - start)
