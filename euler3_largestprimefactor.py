# The largest prime factor
def largestprime(n):
    d = 2
    while d * d <= n:
        if n % d == 0:
            n //= d
        elif d == 2:
            d += 1
        else:
            d += 2
    if n > 1:
        return n


print(largestprime(600851475143))
