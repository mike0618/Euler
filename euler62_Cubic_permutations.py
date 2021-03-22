# Cubic permutations
from time import time

start = time()


def e62():
    digitsmin = []
    cubemin = 0
    cnt = 0
    n = 5000
    maxc = 0
    while cnt < 5:
        cube0 = n ** 3
        digits = []
        cube = cube0
        while cube > 0:
            digits.append(cube % 10)
            cube //= 10
        digits.sort()
        if cnt == 0:
            cnt += 1
            maxc = sum(d * 10 ** i for i, d in enumerate(digits))
            cubemin = n
            digitsmin = digits
        elif cube0 > maxc:
            n = cubemin
            cnt = 0
        elif digitsmin == digits:
            cnt += 1
        n += 1
    return cubemin ** 3


if __name__ == "__main__":
    print('The smallest cube =', e62())  # 127035954683
    print('Runtime =', time() - start)
