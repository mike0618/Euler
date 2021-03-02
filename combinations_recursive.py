# Combinations
from time import time

n = int(input('Enter the number of elements: '))
start = time()
elements = 'abcdefghijklmnopqrstuvwxyz'[:n]


def combs(els):
    if len(els) == 0:
        return ['']
    combinations = []
    for el in combs(els[1:]):
        combinations += [el, el + els[0]]
    return combinations


# print(combs(elements)[1:])  # Bonus!
print('Number of combinations =', len(combs(elements)) - 1)
print('Runtime =', time() - start)
