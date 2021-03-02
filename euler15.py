# Lattice paths
import time


def e15():
    x = int(input("Enter X of grid: "))
    y = int(input("Enter Y of grid: "))
    start = time.time()
    lst = list(range(1, x + 2))
    while lst[1] != y + 1:
        i = 0
        for n in lst[1:]:
            i += 1
            lst[i] = n + lst[i - 1]
    print(f"There are {lst[-1]} routes in {x}x{y} grid!")
    end = time.time() - start
    print("Runtime =", end)


e15()
# start = time.time()
# def memoize(f):
# memo = {}

# def helper(x):
# if x not in memo:
# memo[x] = f(x)
# return memo[x]
# return helper


# @memoize
# def search(node):
# n = 0
# if node[0] == k and node[1] == k:
# return 1
# if node[0] < k+1 and node[1] < k+1:
# n += search((node[0] + 1, node[1]))
# n += search((node[0], node[1] + 1))
# return n

# k = 200
# print(search((0, 0)))
# end = time.time() - start
# print("Runtime =", end)
