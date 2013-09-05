import math

__author__ = 'omer.saeed'

def checkPrime(n):
    if n == 1:
        return false
    elif n < 4:
        return True
    elif n % 2 == 0:
        return False
    elif n < 9:
        return True
    elif n % 3 == 0:
        return False
    else:
        r=math.floor(math.sqrt(n))
        f=5
        while f <=r:
            if n % f == 0:
                return False
            if n % (f+2) == 0:
                return False
            f += 6
        return True

currentPrime = 3
primeSum = 5
while currentPrime < 2000000:
    currentPrime += 2
    if checkPrime(currentPrime):
        primeSum += currentPrime
        print(currentPrime)

print(primeSum)

