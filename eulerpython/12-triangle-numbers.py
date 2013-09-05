from functools import reduce
import utils

__author__ = 'omer.saeed'

target = 500
start = 1
sum = 1
while True:
    start +=  1
    sum += start

    primeIndex = 0
    divisor = 0
    curSum = sum
    primeFactors = {}
    while curSum > 1 and divisor < curSum:
        # find prime divisors
        divisor = utils.nextPrime(primeIndex)
        if not curSum % divisor:
            try:
                primeFactors[divisor] += 1
            except:
                primeFactors[divisor] = 2
            curSum /= divisor
        else:
            primeIndex += 1

    if(reduce(lambda x,y: x * y, primeFactors.values(), 1) > target):
        break

print(sum)




