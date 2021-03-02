def e11():
    f = open("grid.txt")
    lst = []
    gpr = 0
    gprh = 0
    gprv = 0
    gprd1 = 0
    gprd2 = 0
    for st in f:
        lst.extend(st.split())
    for i in range(0, 400, 20):
        for j in range(i, i + 17):
            prh = int(lst[j]) * int(lst[j + 1]) * int(lst[j + 2]) * int(lst[j + 3])
            if prh > gprh:
                gprh = prh
            if prh > gpr:
                gpr = prh
    for j in range(340):
        prv = int(lst[j]) * int(lst[j + 20]) * int(lst[j + 40]) * int(lst[j + 60])
        if prv > gprv:
            gprv = prv
        if prv > gpr:
            gpr = prv
    for i in range(0, 337, 20):
        for j in range(i, i + 17):
            prd1 = int(lst[j]) * int(lst[j + 21]) * int(lst[j + 42]) * int(lst[j + 63])
            if prd1 > gprd1:
                gprd1 = prd1
            if prd1 > gpr:
                gpr = prd1
    for i in range(3, 340, 20):
        for j in range(i, i + 17):
            prd2 = int(lst[j]) * int(lst[j + 19]) * int(lst[j + 38]) * int(lst[j + 57])
            if prd2 > gprd2:
                gprd2 = prd2
            if prd2 > gpr:
                gpr = prd2
    print("The greatest product:", gpr)
    print("The greatest horizintal product:", gprh)
    print("The greatest vertical product:", gprv)
    print("The greatest diagonal \\ product:", gprd1)
    print("The greatest diagonal / product:", gprd2)
    f.close()


e11()
