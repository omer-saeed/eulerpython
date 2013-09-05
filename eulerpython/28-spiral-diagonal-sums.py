__author__ = 'omer.saeed'
spiralSize = 1001

loopSize = (spiralSize - 1) // 2

num = 1
sum = 1
for n in range(1,loopSize+1):
    distance = n*2
    sum += (4*num) + (10*distance)
    num += (distance*4)
    print (num, sum)


