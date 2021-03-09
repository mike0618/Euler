# Amicable numbers
import time


def d(n):  # here is the function determines the sum of the proper divisors
    sumd = 1
    for div in range(2, round(n ** 0.5)):
        if n % div == 0:
            sumd += (div + n // div)
    return sumd


def e21():
    maxn = int(input("Enter the max. number: "))
    start = time.time()
    suma = 0
    for a in range(2, maxn):
        if a < d(a) and a == d(d(a)):  # conditions are here
            suma += (a + d(a))
    end = time.time() - start
    print("Runtime =", end)
    return suma


print(e21())  # answer is 31626 if max is 10000
