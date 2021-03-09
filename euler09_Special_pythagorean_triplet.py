# Special Pythagorean triplet
from time import time

start = time()


def e9():
    for a in range(200, 499):
        for b in range(a + 1, 500):
            if a ** 2 + b ** 2 == (1000 - (a + b)) ** 2:
                print('a =', a)
                print('b =', b)
                print('c =', 1000 - (a + b))
                return a * b * (1000 - (a + b))


print('a*b*c =', e9())  # 31875000
print('Runtime:', time() - start)
