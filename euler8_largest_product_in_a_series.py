# The largest product in a series
from time import time


def e8():
    ln = int(input('enter a length: '))
    start = time()
    n = ''
    with open('e8.txt') as f:
        for s in f:
            n += s.strip()
    maxpr = 1
    pr = 1
    ind = piece = None
    for i in range(len(n) - ln + 1):
        if '0' not in n[i:i + ln]:
            for j in n[i:i + ln]:
                pr *= int(j)
            if pr > maxpr:
                maxpr = pr
                piece = n[i:i + ln]
                ind = i
            pr = 1
    if maxpr > 1:
        print('Place index:', ind)
        print('Adjacent digits are:', piece)
        print('Max Product is:', maxpr)
    else:
        print('Max Product is: 0')
    print('Runtime:', time() - start)


e8()  # if adjacent length = 13, max product = 23514624000
