# Number spiral diagonals
import time

start = time.time()


def e28():
    summ = 1
    point = 1
    for n in range(2, 1001, 2):
        for p in range(4):
            point += n
            summ += point
    return summ


print('diag sum =', e28())  # 669171001
end = time.time() - start
print("Runtime =", end)
