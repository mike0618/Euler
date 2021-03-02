# Digit factorials
from time import time
from math import factorial
from tqdm import tqdm

start = time()


def e34():
    # return sum(n for n in tqdm(range(24, 2000000)) if n == sum(factorial(int(d)) for d in str(n)))
    sumn = 0
    f = factorial(9)
    for n in tqdm(range(24, 2000000)):
        sn = str(n)
        if '9' not in sn and n > 188888:
            continue
        if '9' in sn and n < f:
            continue
        if n == sum(factorial(int(d)) for d in sn):
            sumn += n
    return sumn


print('Sum =', e34())  # 40730
end = time() - start
print("Runtime =", end)
