__author__ = 'omersaeed'

pentagonNumbers = [x * ((3 * x) - 1) / 2 for x in range(1, 1000002)]

for candidate in range(1, 1000001):
    # see if it is a sum of two other numbers
    left = candidate
    right = candidate
    cp = pentagonNumbers[candidate]
    print(candidate)
    for a in range (candidate+1, 1000001):
        breakExternal = False
        for b in range (candidate-1, 0, -1):
            if pentagonNumbers[a] - pentagonNumbers[b] == cp:
                if pentagonNumbers[a] + pentagonNumbers[b] in pentagonNumbers:
                    print(cp)
                    exit()

            if pentagonNumbers[a] - pentagonNumbers[b] > cp:
                if b == candidate-1:
                    breakExternal = True
                break
        if breakExternal == True:
            break

