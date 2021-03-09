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


def ranks(values, flush):
    rank = 0
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
        rank = 8
    elif four:
        rank = 7
    elif three and pair1:
        rank = 6
    elif flush:
        rank = 5
    elif straight:
        rank = 4
    elif three:
        rank = 3
    elif pair1 and pair2:
        rank = 2
    elif pair1:
        rank = 1
    return rank, four, three, pair1, pair2


def scores(values, rank):
    add1 = (rank[1] + rank[3]) * 14 ** 5
    add2 = (rank[2] + rank[4]) * 14 ** 6
    return sum(values[i] * 14 ** i for i in range(5)) + add1 + add2


def e54():
    with open('p054_poker.txt') as f:
        wins = 0
        for s in f:
            val1 = vals(s[:14])
            val2 = vals(s[15:-1])
            fl1 = isflush(s[:14])
            fl2 = isflush(s[15:-1])
            rank1 = ranks(val1, fl1)
            rank2 = ranks(val2, fl2)
            if rank1[0] > rank2[0]:
                wins += 1
            elif rank1[0] == rank2[0]:
                if scores(val1, rank1) > scores(val2, rank2):
                    wins += 1
        return wins


print('Player 1 won', e54(), 'times.')  # 376
print('Runtime =', time() - start)
