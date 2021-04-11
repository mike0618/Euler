# Passcode derivation
from time import time
from itertools import permutations

start = time()


def helpfunc(d, d1, k):
    if len(d) == 1:
        ans = ''.join(d)
        if len(d1) == 1:
            ans += ''.join(d1)
        return ans
    elif len(d1) > 1:
        return ''.join(d.intersection(d1)) + ''.join(d.difference(d1))
    else:
        for p in permutations(d):
            s = ''.join(p)
            for key in k:
                if s in key:
                    return s


def e79():
    keyset = set()
    digit0 = set()
    digit1 = set()
    digit2 = set()

    with open('p079_keylog.txt') as f:
        for s in f:
            keyset.add(s[:-1])
            digit0.add(s[0])
            digit1.add(s[1])
            digit2.add(s[2])

    firsttwo = digit0.difference(digit2)
    middle = digit0.intersection(digit2)
    lasttwo = digit2.difference(digit0)
    passcode = ''.join(firsttwo.difference(digit1)) + ''.join(firsttwo.intersection(digit1))
    passcodeend = ''.join(lasttwo.intersection(digit1)) + ''.join(lasttwo.difference(digit1))

    middlekeys = []
    for key in keyset:
        if set(key) <= middle:
            middlekeys.append(key)

    digit0 = set()
    digit1 = set()
    digit2 = set()
    for key in middlekeys:
        digit0.add(key[0])
        digit1.add(key[1])
        digit2.add(key[2])

    passcode += helpfunc(digit0, digit1, keyset) + helpfunc(digit2, digit1, keyset)

    return passcode + passcodeend


print('The passcode is', e79())  # 73162890
print('Runtime =', time() - start)
