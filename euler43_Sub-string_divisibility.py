# Sub-string divisibility
from time import time
import itertools

start = time()


def e43():
    sump = 0
    setn = set('0123456789')
    for n in range(100, 1000):
        if 500 <= n <= 600 or n % 17:
            continue
        sn = str(n)
        if n < 500:
            sn13 = str(int(sn[0]) + 5) + sn[:2]
        else:
            sn13 = str(int(sn[0]) - 6) + sn[:2]
        if int(sn13) % 13:
            continue
        sn11 = '5' + sn13 + sn[-1]
        if len(set(sn11)) != 5:
            continue
        for sn7 in setn - set(sn11):
            if int(sn7 + sn11[:2]) % 7:
                continue
            sn7 += sn11
            for n3 in range(2, 99, 2):
                sn3 = str(n3)
                if len(sn3) == 1:
                    sn3 = '0' + sn3
                sn3 += sn7
                set3 = set(sn3)
                if len(set3) != len(sn3) or int(sn3[:3]) % 3:
                    continue
                for p in itertools.permutations(setn - set3, 2):
                    sn1 = p[0] + p[1] + sn3
                    print(sn1)
                    sump += int(sn1)
    return sump


print('Sum =', e43())  # 16695334890
print('Runtime =', time() - start)
