# Pandigital multiples
from time import time
import itertools

start = time()


def e38():
    for p in itertools.permutations('987654321', 4):
        s = ''
        for d in p:
            s += d
        if len(set(s + str(int(s) * 2) + '0')) == 10:
            return s + str(int(s) * 2)


print('The largest pandigital =', e38())  # 932718654
print('Runtime =', time() - start)
