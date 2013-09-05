import math
import utils

__author__ = 'omer.saeed'

sumDivs = [0 for x in range(100000)]
a = 9999
sums = 0
while a > 1:
    b = sumDivs[a]
    if not b:
        b = utils.sumProperDivisors(a)
        sumDivs[a] = b

    if a > b:
        v = sumDivs[b]
        if not v:
            v = utils.sumProperDivisors(b)
            sumDivs[b] = v

        if v == a:
            sums += a + b

    a -= 1

print(sums)