# Digit cancelling fractions
from time import time

start = time()


def e33():
    n = 1
    d = 1
    for den in range(13, 99):
        if den % 10 != 0 and den % 11 != 0:
            for num in range(12, den):
                if num % 10 != 0 and num % 11 != 0:
                    if str(den)[0] == str(num)[1]:
                        if int(str(num)[0]) / int(str(den)[1]) == num / den:
                            print(num, "/", den)
                            n *= int(str(num)[0])
                            d *= int(str(den)[1])
    print("Product =", n, "/", d)
    if d % n == 0:
        return d // n
    for m in range(n // 2, 0, -1):
        if n % m == 0 and d % m == 0:
            return d // m


print('Lowest common denominator =', e33())  # 100
end = time() - start
print("Runtime =", end)
