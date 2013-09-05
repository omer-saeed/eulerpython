import utils

__author__ = 'omer.saeed'
abundantNumbers = [0 for x in range(28124)]

utils.sumProperDivisors(4)

# mark abundant numbers
for x in range(28124):
    if utils.sumProperDivisors(x) > x:
        abundantNumbers[x] = 1

sum = 0
for x in range(28124):
    sum += x
    for y in range(x):
        if abundantNumbers[y] and abundantNumbers[x-y]:
            sum -= x
            break

print(sum)