# Distinct powers
import time

start = time.time()


def e29():
    seq = set()
    for a in range(2, 101):
        for b in range(2, 101):
            seq.add(a ** b)
    return len(seq)


print('terms =', e29())  # 9183
# print(len(set(a ** b for a in range(2, 101) for b in range(2, 101))))
end = time.time() - start
print("Runtime =", end)
