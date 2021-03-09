# Multiples of 3 and 5
from time import time

start = time()


def e1():
    return sum(f for f in range(3, 1000, 3)) + sum(b for b in range(5, 1000, 5) if b % 15)


print(e1())  # 233168
print('Runtime:', time() - start)
