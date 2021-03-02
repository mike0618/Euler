# Champernowne's constant
from time import time

start = time()


def e40():
    lst = [10 ** d for d in range(7)]
    sm = 1
    d = 1
    prod = 1
    for n in lst:
        while True:
            s = 9 * d * 10 ** (d - 1)
            if s + sm > n:
                break
            sm += s
            d += 1
        dn = int(str((n - sm) // d + 10 ** (d - 1))[(n - sm) % d])
        prod *= dn
        print(n, '=>', dn)
    return prod


print('Product =', e40())  # 210
print('Runtime =', time() - start)
