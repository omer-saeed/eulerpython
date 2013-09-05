import math
__author__ = 'omer.saeed'
__name__ = 'primes'

primes = [2, 3]

def nextPrime(n):
    index = len(primes)
    if n < index:
        return primes[n]

    currentPrime = primes[n-1]
    while True:
        currentPrime += 2
        if checkPrime(currentPrime):
            primes.append(currentPrime)
            if len(primes) - 1 == n:
                return currentPrime


def checkPrime(n):
    if n <= 1:
        return False
    elif n < 4:
        return True
    elif n % 2 == 0:
        return False
    elif n < 9:
        return True
    elif n % 3 == 0:
        return False
    else:
        r=math.floor(math.sqrt(n))
        f=5
        while f <=r:
            if n % f == 0:
                return False
            if n % (f+2) == 0:
                return False
            f += 6
        return True


#ref #18,67
def longestDistance(tNumbers, a):
    h = v = a
    while v > 0:
        v -= 1
        while h > 0:
            h -= 1
            if v+1 < a:
                if tNumbers[v+1][h]['tWeight'] > tNumbers[v+1][h+1]['tWeight']:

                    tNumbers[v][h] = {'nodeWeight': tNumbers[v][h], 'tWeight': tNumbers[v][h] + tNumbers[v+1][h]['tWeight'], 'direction': 0}
                else:
                    tNumbers[v][h] = {'nodeWeight': tNumbers[v][h], 'tWeight': tNumbers[v][h] + tNumbers[v+1][h+1]['tWeight'], 'direction': 1}
            else:
                tNumbers[v][h] = {'nodeWeight': tNumbers[v][h], 'tWeight': tNumbers[v][h], 'direction': -1}
        h = v
    return tNumbers

def sumDigits(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10

    return sum

def sumProperDivisors(n):
    if n == 0:
        return 0
    index=math.floor(math.sqrt(n))
    sum = 1
    while index > 1:
        if not n % index:
            div = n // index
            sum += index
            if div != index:
                sum += div

        index -= 1

    return sum

def panDigital(numbers, minRange, rangeMax):
    seq = ''
    for n in numbers:
        seq += repr(n)

    if len(seq) > rangeMax - minRange + 1:
        return False
    for x in range(minRange, rangeMax+1):
        if seq.find(repr(x)) < 0:
            return False

    return True

def digitizeNumber(num):
    digits = []
    while num > 0:
        digits.append(num % 10)
        num = num // 10

    return digits

def checkPalindrome(str):
    isPalindrome = True
    for i in range(0, int(len(str) / 2)):
        if str[i] != str[len(str) - 1 - i]:
            isPalindrome = False
            break

    return isPalindrome

