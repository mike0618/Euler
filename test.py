from time import time
import math
import itertools

start = time()

# for p in itertools.permutations('987654321', 4):
#     if int(p[0]) < 6:
#         break
#     s = ''
#     for d in p:
#         s += d
#     if len(set(s + str(int(s) * 2) + '0')) == 10:
#         print(s + ' ' + str(int(s) * 2))
#
# for p in itertools.permutations('321987654', 3):
#     if int(p[0]) > 3:
#         break
#     s = ''
#     for d in p:
#         s += d
#     if len(set(s + str(int(s) * 2) + str(int(s) * 3) + '0')) == 10:
#         print(s + ' ' + str(int(s) * 2) + ' ' + str(int(s) * 3))
#
# s9 = s1 = ''
# for n in range(1, 10):
#     if n < 6:
#         s9 += str(9 * n) + ' '
#     s1 += str(n) + ' '
# print(s9[:-1])
# print(s1[:-1])


prs = [2, 3, 5, 7]

print(prs[-5:-2])


print("Runtime =", time() - start)
