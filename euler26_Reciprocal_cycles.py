# Reciprocal cycles
import time
from tqdm import tqdm

start = time.time()


def e26():
    maxln = 0
    ans = 0
    for d in tqdm(range(1, 1000, 2)):
        if d % 5 != 0:
            ln = 1
            while ln < d and (10 ** ln) % d != 1:  # (ln < d) is just for safety ;)
                ln += 1
            if ln > maxln:
                maxln = ln
                ans = d
    print("Max cycle length =", maxln)
    return ans


print('d =', e26())  # 983
end = time.time() - start
print("Runtime =", end)
