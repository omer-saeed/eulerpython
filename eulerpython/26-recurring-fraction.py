from fractions import Fraction


__author__ = 'omer.saeed'
def longDivision(n, d):
    if d == 0:
        return 0, "NAN"

    decimalDigits = []
    remainders = []
    div = n // d
    retVal = repr(div) + "."
    rem = n % d
    loopLength = 0
    while True:
        if rem in remainders:
            # TODO: Determine the loop and return
            loopIndex = remainders.index(rem)
            length = len(decimalDigits)
            loc = 0
            while loc < loopIndex:
                retVal += repr(decimalDigits[loc])
                loc += 1

            retVal += '('
            while loc < length:
                retVal += repr(decimalDigits[loc])
                loc += 1

            retVal += ')'
            loopLength =  length - loopIndex
            break

        remainders.append(rem)
        n = rem * 10
        div = n // d
        rem = n % d
        decimalDigits.append(div)

        # Ofcourse this could potentially run out of memory, but we don't care

    return loopLength, retVal

lenMax = 0
d = 0
for i in range(10000000):
    length, num = longDivision(1, i)
    if length > lenMax:
        lenMax = length
        d = i
        print (d, longDivision(1,d))
