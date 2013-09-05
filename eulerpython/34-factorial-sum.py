from functools import reduce
import math
import utils


__author__ = 'omer.saeed'

totalSum = 0
#http://math.stackexchange.com/questions/35723/what-is-the-theoretical-upper-bound-of-factorion-numbers
# for the logic for this limit.
factorials = [1,1,2, 6, 24, 120, 720, 5040, 40320, 362880]
for num in range (10, 2540160):
    digits = utils.digitizeNumber(num)
    if reduce(lambda x, y: x + factorials[y], digits, 0) == num:
        totalSum += num

print(totalSum)