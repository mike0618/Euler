# Triangular, pentagonal, and hexagonal
from time import time

start = time()


def hexa(n):  # here is a function to create hexagonal numbers
    return n * (2 * n - 1)


def ispent(p):  # here is a function determines if the number is pentagonal
    return not (((p * 24 + 1) ** 0.5 + 1) / 6) % 1


def e45():
    n = 144
    while True:
        h = hexa(n)
        if ispent(h):  # tri's check is redundant because all hex's are tri's
            return h
        n += 1


print(e45(), 'is next.')  # 1533776805
print('Runtime =', time() - start)

# def ishex(h):  # here is a function determines if the number is hexagonal
#     return not (((h * 8 + 1) ** 0.5 + 1) / 4) % 1
