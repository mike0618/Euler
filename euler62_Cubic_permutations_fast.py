# Cubic permutations
from time import time

start = time()


def e62(n):
    d = {}
    i = 0
    while True:
        i += 1
        cube = i ** 3
        value = ''.join(sorted(str(cube)))
        d[value] = d.get(value, []) + [cube]
        if len(d[value]) == n:
            return min(d[value])


if __name__ == "__main__":
    print('The smallest cube =', e62(5))  # 127035954683
    print('Runtime =', time() - start)
