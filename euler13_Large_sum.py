# Large sum. The first ten digits of the sum of the following 100 50-digit numbers.
from time import time

start = time()


def e13():
    with open("100x50digits.txt") as f:
        summ = 0
        for line in f:
            summ += int(line[:11])  # sum 11 first digits each time, finally we have 13-digit number
        return int(summ / 1000)  # then we get rid of the 3 digits. It does not affect the result


print(e13())  # 5537376230
print('Runtime =', time() - start)
