# Longest Collatz sequence
from time import time


def e14():
    start = time()
    nmax = 0
    lmax = 2
    for sn in range(3, 1000000, 2):
        ln = 1
        n = sn
        while n > 1:
            if n % 2 == 0:
                n = n // 2
            else:
                n = n * 3 + 1
            ln += 1
        if ln > lmax:
            lmax = ln
            nmax = sn
    print("The longest chain number is:", nmax)
    print("Chain length is:", lmax)
    print("Runtime =", time() - start)


e14()  # chain 525, number 837799, runtime > 10 s
