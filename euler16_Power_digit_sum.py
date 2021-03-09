# Sum of digits in 2**1000
from time import time

start = time()


def e16():
    return sum(int(n) for n in str(2 ** 1000))


print(e16())
print('Runtime =', time() - start)
