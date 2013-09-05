from collections import Set
import math


__author__ = 'omer.saeed'

numbers = set()

for a in range(2,101):
    for b in range (2,101):
        numbers.add(math.pow(a,b))

print(len(numbers))
