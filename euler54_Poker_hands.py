# Poker hands
from time import time

start = time()


def isflush(h):
    return h[1] == h[4] == h[7] == h[10] == h[13]


def vals(h):
    val = h[0] + h[3] + h[6] + h[9] + h[12]
    repl = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    return sorted([int(repl.get(v, v)) for v in val])


def isstraight(v):
    return v[0] + 4 == v[1] + 3 == v[2] + 2 == v[3] + 1 == v[4]


def scores(values, flush):
    straight = isstraight(values)
    if flush and straight:
        return 1270000 + values[0]
    three = 0
    pair1 = 0
    pair2 = 0
    for n in range(2, 15):
        if values.count(n) == 4:
            sc = 1260000 + n * 14
            if values[0] == n:
                return sc + values[-1]
            else:
                return sc + values[0]
        if values.count(n) == 3:
            three = n
            if pair1:
                break
        if values.count(n) == 2:
            if pair1:
                pair2 = n
                break
            pair1 = n
            if three:
                break
    if three and pair1:
        return 1250000 + three * 14 + pair1
    if flush:
        return 660020 + sum(values[i] * 14 ** i for i in range(5))
    if straight:
        return 660000 + values[0]
    if three:
        sc = 655000 + three * 14 ** 2
        if three == values[0]:
            return sc + values[-1] * 14 + values[-2]
        elif three == values[-1]:
            return sc + values[1] * 14 + values[0]
        else:
            return sc + values[-1] * 14 + values[0]
    if pair1 and pair2:
        sc = 650000 + pair2 * 14 ** 2 + pair1 * 14
        if values[0] < pair1:
            return sc + values[0]
        elif values[-1] > pair2:
            return sc + values[-1]
        else:
            return sc + values[2]
    if pair1:
        sc = 600000 + pair1 * 14 ** 3
        if pair1 == values[0]:
            return sc + values[4] * 14 ** 2 + values[3] * 14 + values[2]
        elif pair1 == values[-1]:
            return sc + values[2] * 14 ** 2 + values[1] * 14 + values[0]
        elif values[1] == values[2]:
            return sc + values[4] * 14 ** 2 + values[3] * 14 + values[0]
        else:
            return sc + values[4] * 14 ** 2 + values[1] * 14 + values[0]
    return sum(values[i] * 14 ** i for i in range(5))


def e54():
    with open('p054_poker.txt') as f:
        wins = 0
        for s in f:
            h1 = s[:14]
            h2 = s[15:-1]
            if scores(vals(h1), isflush(h1)) > scores(vals(h2), isflush(h2)):
                wins += 1
        return wins


print('Player 1 won', e54(), 'times.')  # 376
print('Runtime =', time() - start)
