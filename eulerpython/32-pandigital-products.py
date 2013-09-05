import math
import utils


__author__ = 'omer.saeed'

# Probable range of numbers to contain all 0-9 in pandigital product sum
bigSum = 0
for x in range (999, 9999):
    # Find all factors and look for them being pandigital
    for y in range(1, math.floor(math.sqrt(x))):
        if x % y == 0:
            if utils.panDigital([x,y, x//y], 1, 9):
                bigSum += x
                break

print(bigSum)






