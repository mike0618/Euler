# Names scores
import time


def e22():
    start = time.time()
    f = open("p022_names.txt")
    names = sorted(f.readline().replace('"', '').split(','))
    f.close()
    total = 0
    for i in range(len(names)):
        avalue = 0
        for char in names[i]:           # determination of the alphabetical value
            avalue += (ord(char) - 64)  # of the name
        total += (avalue * (i + 1))
    end = time.time() - start
    print("Runtime =", end)
    return total


print('Total scores is:', e22())  # 871198282
