import time

start = time.time()


def e12():
    i = 1
    n = 1
    ok = 4
    while ok < 500:
        n += 1
        i += n
        if i % 2 == 0 and i > 250000:
            ok = 4
            for j in range(3, int(i ** 0.5)):
                if i % j == 0:
                    ok += 2
    print(i)
    end = time.time() - start
    print("Runtime =", end)


e12()
