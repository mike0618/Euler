# Square digit chains
from time import time
from tqdm import tqdm

start = time()


def flight(s):
    return sum(int(c) ** 2 for c in s)


def e92():
    nums89 = {89}
    maxsum = 7 * 9 ** 2 + 1
    for n in range(2, maxsum):
        if n in nums89:
            continue
        nums = {n}
        while True:
            num = flight(str(n))
            if num in nums89:
                nums89.update(nums)
                break
            elif num == 1:
                break
            else:
                n = num
                nums.add(num)

    cnt = len(nums89)

    for n in tqdm(range(maxsum, 10000000)):
        num = flight(str(n))
        if num in nums89:
            cnt += 1

    return cnt


if __name__ == "__main__":
    print('There are', e92(), 'numbers arrived to 89')  # 8581146
    print('Runtime =', time() - start)
