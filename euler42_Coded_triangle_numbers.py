# Coded triangle numbers
from time import time

start = time()


def istri(t):  # here is a function determines if the number is triangle
    return not (((t * 8 + 1) ** 0.5 - 1) / 2) % 1


def e42():
    l0 = (ord('A') - 1)
    cnt = 0
    with open('p042_words.txt') as f:
        data = f.read().replace('"', '').split(',')
    for word in data:
        wval = 0
        for ltr in word:
            wval += ord(ltr) - l0
        if istri(wval):
            print(word, wval)  # Bonus!
            cnt += 1
    return cnt


print('Triangle words =', e42())  # 162
print('Runtime =', time() - start)
