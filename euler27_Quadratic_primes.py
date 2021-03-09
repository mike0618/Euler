# Quadratic primes
import time

start = time.time()


def isprime(n):  # here is a function determines if the number is prime
    if n == 2:
        return True
    if n > 2 and n % 2 != 0:
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    return False


def e27():
    maxn = 1
    maxa = 1
    maxb = 1
    for b in range(3, 1000, 2):  # b must be prime if we want to get a prime result when n = 0
        if isprime(b):
            for a in range(-int(2 * b ** 0.5 + 1), int(2 * b ** 0.5 + 1)):
                if a % 2 != 0:
                    n = 1
                    while isprime(n ** 2 + a * n + b):
                        n += 1
                    if n > maxn:
                        maxn = n
                        maxa = a
                        maxb = b
    print('(n ** 2) + (a * n) + b = prime\n0 <= n <=', maxn - 1, '\na =', maxa, '\nb =', maxb)
    return maxa * maxb


print('a * b =', e27())  # -59231
end = time.time() - start
print("Runtime =", end)
