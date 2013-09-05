import math


__author__ = 'omer.saeed'

f1 = 1
f2 = 1
term = 2
while True:
    term += 1
    f3 = f1 + f2
    f1 = f2
    f2 = f3
    if math.log(f3,10) > 999:
        print(term)
        break
