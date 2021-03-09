# Digit fifth powers
import time
from tqdm import tqdm

start = time.time()


def e30():
    pwr = 5
    summ = 0
    for n in tqdm(range(2, pwr * 9 ** pwr)):
        if n == sum(int(d) ** pwr for d in str(n)):
            summ += n
    return summ


print('sum =', e30())  # 443839
end = time.time() - start
print("Runtime =", end)
