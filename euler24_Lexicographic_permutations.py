# Lexicographic permutations
import time
import itertools

start = time.time()


def e24():
    perms = itertools.permutations('0123456789')
    cnt = 0
    for p in perms:
        cnt += 1
        if cnt == 1000000:
            p = str(p).strip("('')").replace("', '", "")
            return p


print(e24())  # 2783915460
end = time.time() - start
print("Runtime =", end)
