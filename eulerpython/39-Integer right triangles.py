__author__ = 'omersaeed'
import math

maxp = 1
maxsolutions = 0

for p in range(1, 1001):
    solutions = 0
    solutionsp = 0
    for a in range(1, p):
        for b in range(a, p):
            c = math.sqrt((a * a) + (b * b))
            check = a + b + c
            if check > p:
                break
            elif check == p:
                solutions += 1

    if solutions > maxsolutions:
        maxsolutions = solutions
        maxp = p

print(maxp, maxsolutions)


