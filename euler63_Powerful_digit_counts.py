# Powerful digit counts
from time import time

start = time()


def e63():
    ints = 0
    p = 1
    while True:
        a = 1
        for n in range(a, 10):
            ln = len(str(n ** p))
            if ln == p:
                ints += 1
            elif ln < p:
                a += 1
        if a == 10:
            return ints
        p += 1


if __name__ == "__main__":
    print('There are', e63(), 'n-digit & n-power positive integers.')  # 49
    print('Runtime =', time() - start)
