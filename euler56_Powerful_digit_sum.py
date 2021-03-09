# Powerful digit sum
from time import time

start = time()


def e56():
    maxs = 0
    for a in range(99, 9, -1):
        if a % 10:
            for b in range(100, 9, -1):
                s = str(a ** b)
                if len(s) < 100:  # tricky optimization
                    break
                summ = sum(int(d) for d in s)
                if summ > maxs:
                    maxs = summ
                # if maxs - summ > 100:  # extreme optimization
                #     break
    return maxs


print('Max digital sum =', e56())  # 972
print('Runtime =', time() - start)
