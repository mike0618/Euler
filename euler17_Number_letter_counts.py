# Number letter counts
from time import time


def e17():
    start = time()
    n1 = (0, 3, 3, 5, 4, 4, 3, 5, 5, 4)  # 1 to 9
    n10 = (0, 3, 6, 6, 5, 5, 5, 7, 6, 6)  # 10 to 90
    n11 = (0, 6, 6, 8, 8, 7, 7, 9, 8, 8)  # 11 to 19
    n = (7, 10, 11)  # hundred, hundred and, one thousand

    n1to99x10 = (sum(n1) * 9 + n10[1] + sum(n11) + sum(n10[2:]) * 10) * 10  # from 1 to 99 all
    n100to900all = n[0] * 9 + n[1] * 99 * 9 + sum(n1) * 100  # from 100 to 900

    letters = n1to99x10 + n100to900all + n[2]
    print("Runtime =", time() - start)

    return letters


print(e17())  # 21124
