from functools import reduce
import utils
import math

__author__ = 'omer.saeed'

palindromesSum = 0

for i in range (0, 1000000):
    if utils.checkPalindrome(str(i)) and utils.checkPalindrome(bin(i)[2:]):
        palindromesSum += i
        print(i)
        print(bin(i)[2:])

print(palindromesSum)