import re


__author__ = 'omer.saeed'
list = [x for x in re.split(',|\"', open('22/names.txt', 'r').readline()) if not x == '']
list.sort()

index = 0
sum = 0
for x in list:
    index += 1
    wordsum = 0
    for y in x:
        wordsum += ord(y) - 64

    sum += wordsum * index

print(sum)
