# Non-abundant_sums
import time
from tqdm import tqdm

start = time.time()


def ab(n):  # here is the function determines the abundant number
    sumd = 1
    for div in range(2, int(n ** 0.5) + 1):
        if n % div == 0:
            if div != n // div:
                sumd += (div + n // div)
            else:
                sumd += div
    return sumd > n


def e23():
    abund = set()
    sumn = 0

    def absum(i):  # this function determines that a number is the sum of two abundant numbers
        for a in abund:
            if (i - a) in abund:
                return True

    for n in tqdm(range(1, 28124)):
        if ab(n):
            abund.add(n)
        if not absum(n):
            sumn += n
    return sumn


print(e23())  # 4179871


# numbers = []
# excess_numbers = []
# sum_excess_numbers = []
#
# for i in tqdm(range(1, 28124)):
#     sum_of_divider = 0
#     numbers.append(i)
#     for j in range(1, int(i / 2) + 1):
#         if i % j == 0:
#             sum_of_divider += j
#             if sum_of_divider > i:
#                 excess_numbers.append(i)
#                 break
#
# for i in tqdm(range(len(excess_numbers))):
#     for j in range(i + 1):
#         sum_excess_numbers.append(excess_numbers[i] + excess_numbers[j])
#
# numbers = set(numbers)
# sum_excess_numbers = set(sum_excess_numbers)
# numbers.difference_update(sum_excess_numbers)
#
# print(sum(numbers))


end = time.time() - start
print("Runtime =", end)
