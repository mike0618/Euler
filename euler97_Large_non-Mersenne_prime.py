# Large non-Mersenne prime
from time import time

start = time()


def e97():
    mod = 10 ** 10
    return (pow(2, 7830457, mod) * 28433 + 1) % mod


print('The last ten digits are', e97())  # 8739992577
print('Runtime =', time() - start)
