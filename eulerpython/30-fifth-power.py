import math


__author__ = 'omer.saeed'

nums = []
bigsum = 0
pow = 5
for a in range(10,999999):
    digs = a
    sum = 0
    while digs > 0:
        sum += math.pow(digs % 10,5)
        digs = digs // 10

    if sum == a:
        print(a)
        nums.append(a)
        bigsum += a

print(bigsum, nums)
