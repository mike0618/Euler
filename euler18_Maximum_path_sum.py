# Maximum path sum I
from time import time

start = time()


def e18():
    with open("num_triangle.txt") as f:
        summ = []
        for s in f:
            slst = s.split()
            lst = [int(item) for item in slst]
            if len(lst) <= 1:
                summ = lst
            else:
                for i in range(len(lst)):
                    if i == 0:
                        lst[i] += summ[i]
                    elif i == len(lst) - 1:
                        lst[i] += summ[i - 1]
                    elif (lst[i] + summ[i - 1]) > (lst[i] + summ[i]):
                        lst[i] += summ[i - 1]
                    else:
                        lst[i] += summ[i]
                summ = lst
        return max(summ)


print(e18())  # 1074
print('Runtime =', time() - start)
