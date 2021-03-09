# Smallest multiple
from time import time

x = int(input('Enter the max of range: '))
start = time()


def smmult():
    sm = 1
    for n in range(2, x + 1):
        if sm % n != 0:
            d = 2  # divider to try
            while d * d <= n:
                if n % d == 0:
                    sm *= d
                    break
                elif d == 2:
                    d += 1
                else:
                    d += 2
            else:
                sm *= n
    return sm


print(smmult(), 'is the smallest num that evenly divisible by all the nums from 1 to', x)
print('Runtime:', time() - start)
