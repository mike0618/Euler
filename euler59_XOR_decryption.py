# XOR decryption
from time import time

start = time()


def e59():
    keys = []
    with open("p059_cipher.txt") as f:
        encrypted = f.read().split(',')
    for i in range(3):
        for k in range(ord('a'), ord('z') + 1):
            string = ''
            for ch in encrypted[i::3]:
                decr = chr(int(ch) ^ k)
                if not decr.isprintable():
                    break
                string += decr
            else:
                if string.count('e') / len(string) > 0.085:  # matched manually 'e' is the most frequetly in English
                    keys.append(k)
    ki = 0
    decryptedtext = ''
    summ = 0
    for ch in encrypted:
        val = int(ch) ^ keys[ki]
        decryptedtext += chr(val)  # Bonus!
        summ += val
        if ki == 2:
            ki = 0
            continue
        ki += 1
    print('Keys:', [chr(k) for k in keys], '\n', decryptedtext)
    return summ


print('The sum of ASCII values in the original text = ', e59())  # 129448
print('Runtime =', time() - start)
