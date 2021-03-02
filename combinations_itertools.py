# Combinations
from time import time
import itertools


def combs():
    n = int(input('Enter the number of elements: '))
    start = time()
    elements = 'abcdefghijklmnopqrstuvwxyz'
    count = 0
    for number in range(1, n + 1):
        for p in itertools.combinations(elements[:n], number):
            count += 1
            if n < 10:
                print(p)  # Bonus!
    print('Runtime =', time() - start)
    return count


print('Number of combinations =', combs())  # 9 - 511
