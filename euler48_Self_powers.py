# Self powers
from time import time

start = time()


def e48():
    # print(sum(n ** n for n in range(1, 1001)))  # Bonus - the whole number!
    return str(sum(n ** n for n in range(1, 1000) if n % 10))[-10:]


print(e48())  # 9110846700
print('Runtime =', time() - start)
