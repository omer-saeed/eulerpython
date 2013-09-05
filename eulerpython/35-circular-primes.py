from functools import reduce
import utils
import math

__author__ = 'omer.saeed'

target = 1000000
primes = 0
prime = 0
currentPrime = 0
while True:
    prime = utils.nextPrime(currentPrime)
    if prime > target:
        break

    #Calculate rotation of a given number
    allPrimes = True
    nextPrime = prime
    for rotations in range (0, int(math.log10(prime))):
        nextPrime = int(int(nextPrime / 10) + ((nextPrime % 10) * int(math.pow(10, int(math.log10(prime))))))
        if utils.checkPrime(nextPrime) == False:
            allPrimes = False
            break

    if allPrimes == True:
        primes += 1
        print(prime)

    currentPrime += 1

print(primes)