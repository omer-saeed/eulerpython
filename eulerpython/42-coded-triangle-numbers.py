import re
__author__ = 'omer.saeed'
list = [x for x in re.split(',|\"', open('42/words.txt', 'r').readline()) if not x == '']

triangleNumbers = [ (n * (n+1)) / 2 for n in range(1,1000) ]

index = 0
count = 0
for x in list:
    wordsum = 0
    for y in x:
        wordsum += ord(y) - 64

    if wordsum in triangleNumbers:
        count += 1

print(count)
