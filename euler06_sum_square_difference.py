# Sum square difference
from time import time


def e6():
    num = int(input('Enter the max natural number: '))
    start = time()
    sumsq = 0
    sumn = 0
    for n in range(num + 1):
        sumsq += n ** 2
        sumn += n
    print('Runtime:', time() - start)
    return sumn ** 2 - sumsq


print('The square of the sum minus the sum of the squares =', e6())  # if max = 100, diff = 25164150
