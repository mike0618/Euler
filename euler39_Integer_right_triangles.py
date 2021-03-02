# Integer right triangles
from time import time
import math

start = time()


def e39():
    sin45 = math.sin(math.pi / 4)
    hm = 2 * sin45 + 1  # the hypotenuse is min when the angles = 45deg and the legs are equal
    maxs = 0            # p = 2 * leg + hmin; leg = hmin * sin45; hmin = p / (2 * sin45 + 1)
    maxp = 0
    for p in range(100, 1001, 2):  # perimeter is always even
        sol = 0
        for h in range(int(p / hm) + 1, p // 2):  # here is hypotenuse, from min to max
            bsq = (p - h) ** 2  # for the square equasion: leg**2-(p-h)*leg+((p-h)**2-h**2)/2 = 0
            dis = bsq - 2 * (bsq - h ** 2)  # discriminant: b**2-4*a*c
            leg = (p - h + dis ** 0.5) / 2
            if leg == int(leg):
                sol += 1
                # print(p, h, leg, p - h - leg)
        if sol > maxs:
            maxs = sol
            maxp = p
    return f'For p = {maxp}, the number of solutions = {maxs}'


print(e39())  # 840
# lim = 1000
# max_cnt = max_v = 0
# for p in range(lim // 10, lim + 1, 2):
#     n = p * p // 2
#     cnt = 0
#     i = p // 2 + 1
#     while i * i <= n:
#         if n % i == 0:
#             cnt += 1
#         i += 1
#     if cnt > max_cnt:
#         max_cnt = cnt
#         max_v = p
# print(max_v, max_cnt)
print('Runtime =', time() - start)
