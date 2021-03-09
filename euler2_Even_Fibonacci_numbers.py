# Even Fibonacci numbers
from time import time

start = time()


def e2(n):
    ff = 2
    fff = 3
    summ = ff
    while True:
        f = ff + fff
        ff = f + fff
        fff = f + ff
        summ += ff
        if ff > n:
            return summ - ff


print(e2(4000000))  # 4613732
print('Runtime:', time() - start)
