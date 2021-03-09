# Lattice paths
from time import time


def e15():
    x = int(input("Enter X of grid: "))
    y = int(input("Enter Y of grid: "))
    start = time()
    lst = list(range(1, x + 2))
    while lst[1] != y + 1:
        i = 0
        for n in lst[1:]:
            i += 1
            lst[i] = n + lst[i - 1]
    print(f"There are {lst[-1]} routes in {x}x{y} grid!")
    print('Runtime =', time() - start)


e15()

