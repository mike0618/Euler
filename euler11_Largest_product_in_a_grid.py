# Largest product in a grid
from time import time


def e11():
    start = time()
    lst = []
    gprh = 0
    gprv = 0
    gprd1 = 0
    gprd2 = 0
    with open("grid.txt") as f:
        for st in f:
            lst.extend(st.split())
    for i in range(0, 400, 20):
        for j in range(i, i + 17):
            prh = int(lst[j]) * int(lst[j + 1]) * int(lst[j + 2]) * int(lst[j + 3])
            if prh > gprh:
                gprh = prh
    gpr = gprh
    for j in range(340):
        prv = int(lst[j]) * int(lst[j + 20]) * int(lst[j + 40]) * int(lst[j + 60])
        if prv > gprv:
            gprv = prv
    if gprv > gpr:
        gpr = gprv
    for i in range(0, 337, 20):
        for j in range(i, i + 17):
            prd1 = int(lst[j]) * int(lst[j + 21]) * int(lst[j + 42]) * int(lst[j + 63])
            if prd1 > gprd1:
                gprd1 = prd1
    if gprd1 > gpr:
        gpr = gprd1
    for i in range(3, 340, 20):
        for j in range(i, i + 17):
            prd2 = int(lst[j]) * int(lst[j + 19]) * int(lst[j + 38]) * int(lst[j + 57])
            if prd2 > gprd2:
                gprd2 = prd2
    if gprd2 > gpr:
        gpr = gprd2
    print("Greatest horizontal product:", gprh)
    print("Greatest vertical product:", gprv)
    print("Greatest diagonal \\ product:", gprd1)
    print("Greatest diagonal / product:", gprd2)
    print("Greatest product:", gpr)
    print("Runtime =", time() - start)


e11()  # 70600674
