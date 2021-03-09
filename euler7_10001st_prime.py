# 10001st prime
from time import time


def e7():
    i = 3
    n = int(input("Enter a number of prime: "))
    start = time()
    while n > 2:
        i += 2
        for j in range(3, int(i ** 0.5) + 1, 2):
            if i % j == 0:
                break
        else:
            n -= 1
    print("Runtime =", time() - start)
    return i


print("Prime is:", e7())
