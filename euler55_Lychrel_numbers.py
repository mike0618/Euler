# Lychrel numbers
from time import time

start = time()


def e55():
    cnt = 0
    for p in range(19, 10000):
        for it in range(49):
            p += int(str(p)[::-1])
            if p == int(str(p)[::-1]):
                break
        else:
            cnt += 1
    return cnt


print('Amount of Lychrel numbers:', e55())  # 249
print('Runtime =', time() - start)
