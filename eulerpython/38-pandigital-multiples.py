__author__ = 'omersaeed'

import utils
import math

__author__ = 'omer.saeed'

number = 1
maxPanDigital = 0
while number < 50000:
    for i in range(1, 10):
        numbers = []
        for j in range(1, i+1):
            numbers.append(number * j)

        if utils.panDigital(numbers, 1, 9) == True:
            panDigital = int(''.join(str(x) for x in numbers))
            if panDigital > maxPanDigital:
                maxPanDigital = panDigital
                print(panDigital)
                print(numbers)

    number += 1
