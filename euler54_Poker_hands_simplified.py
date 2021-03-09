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
    score = sum(values[i] * 14 ** i for i in range(5))
    straight = isstraight(values)
    four = 0
    three = 0
    pair1 = 0
    pair2 = 0
    for n in range(2, 15):
        if values.count(n) == 4:
            four = n
            break
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
    if flush and straight:
        return score + values[0] * 14 ** 11
    if four:
        return score + four * 14 ** 10
    if three and pair1:
        return score + three * 14 ** 9 + pair1 * 14 ** 5
    if flush:
        return score + 14 ** 9
    if straight:
        return score + values[0] * 14 ** 8
    if three:
        return score + three * 14 ** 7
    if pair1 and pair2:
        return score + pair2 * 14 ** 6 + pair1 * 14 ** 5
    if pair1:
        return score + pair1 * 14 ** 5
    return score


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
