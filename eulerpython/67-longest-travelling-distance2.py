import utils

__author__ = 'omer.saeed'
__name__ = 'longestdistance'

sNumbers = []

with open('67/triangle.txt', 'r') as f:
    for line in f:
        sNumbers.append([int(i) for i in line.split()])

print(utils.longestDistance(sNumbers,100))