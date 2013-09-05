import utils


__author__ = 'omer.saeed'

def quadratic(n, a, b):
    return (n*n) + (a * n) + b


largestN = 0
largestA = 0
largestB = 0
for a in range(-10000, 10000):
    for b in range(-10000, 10000):
        #print("checking for ", a, b)
        #initial Checks
        N = largestN
        if a == 1 and b == 41:
            pass
        while N < 1000:
            if utils.checkPrime(quadratic(N,a,b)):
                N += 1
            else:
                if N > largestN:
                    X = 0
                    while X < largestN:
                        if not utils.checkPrime(quadratic(X,a,b)):
                            break

                        X += 1

                    if X == largestN:
                        largestN = N
                        largestA = a
                        largestB = b
                        print(N, a, b, a*b)
                    break
                break