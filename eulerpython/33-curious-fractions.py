from fractions import Fraction
from functools import reduce
import utils


__author__ = 'omer.saeed'

finalFraction = Fraction(1,1)
for n in range(11,99):
    for d in range(n+1,100):
        if n % 10 == d % 10 == 0:
            continue

        num = utils.digitizeNumber(n);
        den = utils.digitizeNumber(d);
        for numx in num:
            for denx in den:
                if numx == denx:
                    den.remove(numx)
                    num.remove(numx)
                    break

        if len(den) == 2:
            continue

        # check if there are any 0s in the den
        try:
            frTest = Fraction(reduce(lambda x, y: x * y, num, 1), reduce(lambda x, y: x * y, den, 1))
        except:
            continue

        fr = Fraction(n, d)

        if fr == frTest:
            finalFraction = finalFraction * fr
            print(fr, finalFraction)






