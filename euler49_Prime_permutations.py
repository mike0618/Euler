# Prime permutations
from time import time

start = time()


def isprime(n):  # here is a function determines if the number is prime
    if n == 2:
        return True
    if n > 2 and n % 2 != 0:
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    return False


def e49():
    # determination of the first term
    for d3 in (1, 3, 7, 9):  # here are acceptable static last digits.
        for d0 in (1, 2):  # d0 < 4 and can't be 3 too (3+3=6, 6+3=9, 9+3=(1)2 => 3,6,9,2 is > 3 digits)
            for circ in (1, 2):  # there are 2 directions of circulation 3 digits
                if circ == 1:
                    d1 = d0 + 3
                    d2 = d1 + 4  # d0 + 10 - 3
                else:
                    d1 = d0 + 7  # d0 + 10 - 3
                    d2 = d0 + 4  # d1 - 3
                term = int(str(d0) + str(d1) + str(d2) + str(d3))
                if term != 1487 and isprime(term) and isprime(term + 3330) and isprime(term + 6660):
                    return str(term) + str(term + 3330) + str(term + 6660)


print('Number =', e49())  # 296962999629
print('Runtime =', time() - start)
