import time
from tqdm import tqdm


def palindrome():  # the largest palindrome made from the product of two n-digit numbers
    n = int(input("Enter the number of digits: "))
    start = time.time()
    a = 10 ** (n - 1)
    b = 10 ** n - 1
    for i in tqdm(range(b ** 2, a ** 2, -1)):
        if i == int(str(i)[::-1]):  # check if palindrome
            for j in range(b, a, -1):
                if i % j == 0 and i // j <= b:
                    print(j)
                    print(i // j)
                    end = time.time() - start
                    print("Runtime =", end)
                    return i


print(palindrome())
