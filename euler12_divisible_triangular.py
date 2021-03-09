# Highly divisible triangular number
from time import time


def e12():
    start = time()
    tri = 1
    nat = 1
    div = 4  # Every even number that is greater than 2 is divisible by 1, 2, half and itself without a reminder.
    while div < 501:
        nat += 1
        tri += nat
        if tri % 2 == 0 and tri > 250000:  # I don't know exactly, I took only even numbers > 500 ** 2
            div = 4
            for j in range(3, int(tri ** 0.5) + 1):
                if tri % j == 0:
                    div += 2  # Each time we have 2 divisors
    print("Triangular number:", tri)
    print("Divisors:", div)
    print("Runtime =", time() - start)


e12()  # 76576500
