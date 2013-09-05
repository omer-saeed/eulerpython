__author__ = 'omer.saeed'

n = 999999
maxNum = 1
maxChain = 1
numList = {}

def collatz(n):
    if n == 1:
        return 1
    else:
        try:
            return numList[n]
        except:
            if n % 2 == 0:
                n //= 2
            else:
                n = (3 * n) + 1

            count = collatz(n) + 1
            numList[n] = count
            return count

while  n > 1:
    try:
        numList[n]
    except:
        chain = collatz(n)
        if chain > maxChain:
            maxChain = chain
            maxNum = n
    n -= 1

print(maxNum, maxChain)