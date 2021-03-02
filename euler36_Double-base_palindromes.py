# Double-base palindromes
from time import time

start = time()


def ispln(n):  # here is a function determines if the number is a palindrome
    return n == n[::-1]


def str6(n):  # here is a function to create 6-digit 10-base palindromes
    sn = str(n)
    if n < 10:
        s = sn + '0000' + sn
    elif n < 100:
        s = sn[::-1] + '00' + sn
    else:
        s = sn[::-1] + sn
    return int(s)


def str45(n, m=10):  # here is a function to create 4 and 5-digit 10-base palindromes
    sn = str(n)
    if m == 10 and n < 10:
        s = sn + '00' + sn
    elif m == 10:
        s = sn[::-1] + sn
    elif n < 10:
        s = sn + '0' + str(m) + '0' + sn
    else:
        s = sn[::-1] + str(m) + sn
    return int(s)


def e36():
    # return sum(n for n in range(1, 1000000, 2) if ispln(str(n)) and ispln(bin(n)[2:]))
    sump = 0
    for n in range(1, 100, 2):
        if n > 10 and n % 11 == 0 and ispln(bin(n)[2:]):  # determinating 2-digit palindromes
            sump += n
        n4 = str45(n)
        if ispln(bin(n4)[2:]):  # determinating 4-digit palindromes
            sump += n4
        for m in range(0, 10):
            if n == 1 and m % 2 != 0 and ispln(bin(n)[2:]):  # determinating 1-digit palindromes
                sump += m
            n5 = str45(n, m)
            if ispln(bin(n5)[2:]):  # determinating 5-digit palindromes
                sump += n5
    for n in range(1, 1000, 2):
        if n > 100 and n // 100 == n % 10 and ispln(bin(n)[2:]):  # determinating 3-digit palindromes
            sump += n
        n6 = str6(n)
        if ispln(bin(n6)[2:]):  # determinating 6-digit palindromes
            sump += n6
    return sump


print('Double-base palindromes sum =', e36())  # 872187
end = time() - start
print('Runtime =', end)
