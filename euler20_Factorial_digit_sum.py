# Factorial digit sum
from time import time


def e20():
    n = int(input("Enter a number: "))
    start = time()
    fact = 1
    summ = 0
    for m in range(2, n + 1):
        fact *= m
    for a in str(fact):
        summ += int(a)
    end = time() - start
    print('Runtime =', end)
    return summ


print(e20())  # 648 if n = 100
