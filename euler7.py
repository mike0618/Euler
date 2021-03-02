def e7():
    i=3
    n=int(input("Enter a number of prime: "))
    while n>2:
        i+=2
        for j in range(3,int(i**0.5)+1,2):
            if i%j==0:
                break
        else:
            n-=1
    print("Prime is:", i)
e7()
