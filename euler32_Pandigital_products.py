# Pandigital products
from time import time

start = time()


def e32():  # we have to achieve 9 digits at all
    # pretty easy math analyze shows: we have to take 1d * 4d or 2d * 3d and get 4d product
    setp = set()
    a = 1234  # min 4-digit multiplier
    for n in range(2, 81):  # 1 and >80 are not acceptable, 9876/81 < 123 is not ok
        if n < 9 or (n > 11 and n % 11 != 0 and n % 10 != 0):  # a little optimization here, maybe it's redundant
            if n > 11:
                a = 123  # min 3-digit multiplier
            for m in range(a, 9876 // n + 1):  # 9876 must be the max 4-digit product
                if len(set(str(m) + str(n) + "0")) == 6:  # a little optimization here, maybe it's redundant
                    p = n * m  # we have only 4-digit products here
                    if len(set(str(p) + str(m) + str(n) + "0")) == 10:  # check if 9 different digits except 0 are here
                        setp.add(p)
                        print(n, '*', m, '=', p)  # bonus!
    return sum(setp)


print("Sum of products =", e32())  # 45228
end = time() - start
print("Runtime =", end)
