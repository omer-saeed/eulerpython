__author__ = 'omer.saeed'

noOfCells = 20
tableHeight=noOfCells+1
yVector = [0]*(tableHeight)
lastVector = [0]*(tableHeight)
for xIndex in range(1,tableHeight):
    yIndex = 0
    while yIndex <= xIndex:
        if not yIndex:
            yVector[yIndex] = 1
        elif not yIndex - xIndex:
            yVector[yIndex] = yVector[yIndex-1] * 2
        else:
            yVector[yIndex] = yVector[yIndex-1] + lastVector[yIndex]

        yIndex += 1
    lastVector = yVector
    yVector = [0]*(tableHeight)

print(lastVector)

