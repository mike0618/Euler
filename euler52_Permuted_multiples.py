# Permuted multiples
from time import time

start = time()


def pf(num):  # comparison preparation function
    # return set(str(num))  # it's a little faster but not an exact solution
    return ''.join(sorted(str(num)))


def e52():
    smax = '16666'
    while True:
        smax += '6'
        for n in range(10 ** (len(smax) - 1) + 2, int(smax), 3):  # n must be divisible by 3
            if pf(n) == pf(n * 2) == pf(n * 3) == pf(n * 4) == pf(n * 5) == pf(n * 6):
                return n


print('Answer =', e52())  # 142857
print('Runtime =', time() - start)
