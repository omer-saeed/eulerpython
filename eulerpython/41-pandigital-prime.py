import math
import utils
import itertools

__author__ = 'omer.saeed'

largest_prime = 0
pandigital = []
for i in range(1,10):
    pandigital.append(i)
    for comb in list(itertools.permutations(pandigital)):
        prime = int(''.join(str(x) for x in comb))
        if utils.checkPrime(prime) == True:
            if prime > largest_prime:
                print(prime)
                largest_prime = prime

print(largest_prime)
