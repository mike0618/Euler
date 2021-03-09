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


class Rank:
    def __init__(self, values, flush):
        self.four = 0
        self.three = 0
        self.pair1 = 0
        self.pair2 = 0
        self.values = values
        self.flush = flush

    def ranks(self):
        straight = isstraight(self.values)
        for n in range(2, 15):
            if self.values.count(n) == 4:
                self.four = n
                break
            if self.values.count(n) == 3:
                self.three = n
                if self.pair1:
                    break
            if self.values.count(n) == 2:
                if self.pair1:
                    self.pair2 = n
                    break
                self.pair1 = n
                if self.three:
                    break
        if self.flush and straight:
            return 8
        if self.four:
            return 7
        if self.three and self.pair1:
            return 6
        if self.flush:
            return 5
        if straight:
            return 4
        if self.three:
            return 3
        if self.pair1 and self.pair2:
            return 2
        if self.pair1:
            return 1
        return 0

    def scores(self):
        add1 = (self.four + self.pair1) * 14 ** 5
        add2 = (self.three + self.pair2) * 14 ** 6
        return sum(self.values[i] * 14 ** i for i in range(5)) + add1 + add2


def e54():
    with open('p054_poker.txt') as f:
        wins = 0
        for s in f:
            h1 = s[:14]
            h2 = s[15:-1]
            pl1 = Rank(vals(h1), isflush(h1))
            pl2 = Rank(vals(h2), isflush(h2))
            rank1 = pl1.ranks()
            rank2 = pl2.ranks()
            if rank1 > rank2:
                wins += 1
            elif rank1 == rank2:
                if pl1.scores() > pl2.scores():
                    wins += 1
        return wins


print('Player 1 won', e54(), 'times.')  # 376
print('Runtime =', time() - start)
