# Coin sums
from time import time
from math import ceil

start = time()
coins = (2, 5, 10, 20, 50, 100, 200)


def e31(amount, maxc):
    ways = 0
    for coin in coins:
        if coin < maxc:  # take coins less then present to correct completion of remainders
            ways += amount // coin  # here we count the same coin ways only
            if coin > 2:  # here are more ways for coins greater then 2
                remain = amount
                for n in range(ceil(amount / coin) - 1):
                    remain -= coin  # figuring out all the remainders for possible numbers of each coin
                    ways += e31(remain, coin)  # run recursion for each remainder to figure out all the ways

    return ways


print("Number of ways =", e31(200, 201) + 1)  # 73682 (+ 1 is for 200 * 1p way, we didn't count it in e31 function)
end = time() - start
print("Runtime =", end)
