import math


def isPrime(number):
    if(number<=1): return 0

    for i in range(2, int(math.sqrt(number))):
        if(number%i==0): return 0

    return 1


number = int(input("Enter the number:"))
print(isPrime(number))