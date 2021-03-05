# Combinatoric selections
from time import time
from math import factorial

start = time()


def check(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r)) > 1000000


def e53():
    summ = 0
    for n in range(23, 101):
        for r in range(2, n):
            if check(n, r):
                summ += n + 1 - 2 * r
                break
    return summ


print('Number of values =', e53())  # 4075
print('Runtime =', time() - start)
