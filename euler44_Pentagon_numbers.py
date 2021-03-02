# Pentagon numbers
from time import time

start = time()


def ispent(p):  # here is a function determines if the number is pentagonal
    return not (((p * 24 + 1) ** 0.5 + 1) / 6) % 1


def pent(n):  # here is a function to create pentagonal numbers
    return n * (3 * n - 1) / 2


def e44():
    k = 4
    while True:
        pk = pent(k)
        for j in range(k - 1, 8 * k // 17, - 2):    # I don't know exactly but P(k) + P(j) < P(k+1)
            pj = pent(j)                            # when j is about half of k (not acceptable)
            if ispent(pk + pj) and ispent(pk - pj):
                print(int(pk + pj))
                print(int(pk))
                print(int(pj))
                return int(pk - pj)
        k += 1


print('D =', e44())  # 5482660
print('Runtime =', time() - start)
