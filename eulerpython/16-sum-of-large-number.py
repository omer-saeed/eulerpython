import math

__author__ = 'omer.saeed'
powerBase = 2
power = 1000

number = powerBase
while power > 1:
    number *= powerBase
    power -= 1

sum = 0
while number > 0:
    print(number, sum)
    sum += number % 10
    number //= 10

print (sum)