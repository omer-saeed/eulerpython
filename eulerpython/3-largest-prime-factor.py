__author__ = 'omer.saeed'

def checkPrime(num):
    check = 2
    while check <= num / 2:
        if num % check == 0:
            return False
        check = check + 1
    return True;

def nextPrime(last):
    while True:
        if last == 2:
            last = last + 1
        elif  last > 2:
            last = last+2

        if checkPrime(last) == True:
            return last

sourceNum = 600851475143
currentFactor = sourceNum
biggestFactor = 1

while True:
    currentPrime = 2
    while currentFactor % currentPrime != 0:
        currentPrime = nextPrime(currentPrime)

    currentFactor = currentFactor / currentPrime
    if currentPrime > biggestFactor:
        biggestFactor = currentPrime

    if currentFactor == 1:
        print("Biggest Factor = ", biggestFactor)
        break

