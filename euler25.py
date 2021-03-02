# 1000-digit Fibonacci number
import time

start = time.time()


def e25(n):
    f = 0
    ff = 1
    cnt = 0
    maxd = 10 ** (n - 1)
    while True:
        cnt += 2
        f += ff
        ff += f
        if ff > maxd:
            break
    if f > maxd:
        print(f)
        return cnt
    print(ff)
    return cnt + 1


print(e25(1000))  # 4782
end = time.time() - start
print("Runtime =", end)
