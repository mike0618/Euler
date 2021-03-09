# Square root convergents
from time import time

start = time()


def e57():
    # Let's drop 1 at the beginning and use it then...
    n = 1
    d0 = 2
    cnt = 0
    for it in range(999):
        d = 2 * d0 + n
        n = d0
        d0 = d
        if len(str(n + d0)) > len(str(d0)):
            cnt += 1

    return cnt


print('Amount of fractions with more digits in numerator =', e57())  # 153
print('Runtime =', time() - start)
