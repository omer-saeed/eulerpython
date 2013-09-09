__author__ = 'omer.saeed'

import math
import utils
import itertools

sum = 0
pandigital = [0,1,2,3,4,5,6,7,8,9]
for comb in list(itertools.permutations(pandigital)):
    num1 = int(''.join(str(x) for x in comb[1:4]))
    if num1 % 2 is 0:
        num2 = int(''.join(str(x) for x in comb[2:5]))
        if num2 % 3 is 0:
            num3 = int(''.join(str(x) for x in comb[3:6]))
            if num3 % 5 is 0:
                num4 = int(''.join(str(x) for x in comb[4:7]))
                if num4 % 7 is 0:
                    num5 = int(''.join(str(x) for x in comb[5:8]))
                    if num5 % 11 is 0:
                        num6 = int(''.join(str(x) for x in comb[6:9]))
                        if num6 % 13 is 0:
                            num7 = int(''.join(str(x) for x in comb[7:10]))
                            if num7 % 17 is 0:
                                num = int(''.join(str(x) for x in comb))
                                print(num)
                                sum += num

print(sum)