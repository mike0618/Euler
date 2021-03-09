# Largest palindrome product
from time import time
from tqdm import tqdm

n = int(input("Enter the number of digits: "))


def e4():  # the largest palindrome made from the product of two n-digit numbers
    if n < 1:
        return 'Please enter a number greater than 0'
    if n > 9:
        return 'This is not possible, try a lower number'
    if n > 5:
        conf = input('It may take too long! Are you ready? y/n: ')
        if conf == '' or conf[0] != 'y' and conf[0] != 'Y':
            return 'Good bye!'
    start = time()
    a = 10 ** (n - 1)
    b = 10 ** n - 1
    for i in tqdm(range(b ** 2, a ** 2, -1)):
        if i == int(str(i)[::-1]):  # check if palindrome
            for j in range(b, a, -1):
                if i % j == 0 and i // j <= b:
                    print("Runtime =", time() - start)
                    return f'{j} * {i // j} = {i}, is the largest palindrome'


print(e4())  # 906609 if 3 digits
