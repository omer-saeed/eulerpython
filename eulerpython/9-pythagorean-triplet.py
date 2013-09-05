import math


__author__ = 'omer.saeed'

sumNeeded = 1000

# Look for numbers a & b around this where the sum of squares is a perfect square

num1 = 1
num2 = sumNeeded-1
while True:
    #decrement num2 until (a^2 + b^2)^ .5 is a whole number
    factor = math.pow(math.pow(num2,2)+math.pow(num1,2), 0.5)
    if factor + num1 + num2 == 1000:
        print(num1 * num2 * factor)
        break
    num2 -= 1
    if num2 < 1:
        num1 += 1
        num2 = sumNeeded - num1

    if num2 == 0:
        break