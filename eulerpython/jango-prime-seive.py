import memcached


__author__ = 'omer.saeed'

#initialize; Assume all are primes
def initializeSieve(size, sieve):
    for N in range(size):
        sieve[N] = 0b11111111

def removeComposites(i, size, maxSize, sieveList):
    checkN = i*2
    maxNum = maxSize * 30
    while checkN <= maxNum:
        sieveChunk = checkN // (size * 30)
        divN = (checkN // (size * 30)) - 1
        remN = checkN % 30

        if remN == 1:
            sieveList[sieveChunk][divN] &= 0b11111110
        elif remN == 7:
            sieveList[sieveChunk][divN] &= 0b11111101
        elif remN == 11:
            sieveList[sieveChunk][divN] &= 0b11111011
        elif remN == 13:
            sieveList[sieveChunk][divN] &= 0b11110111
        elif remN == 17:
            sieveList[sieveChunk][divN] &= 0b11101111
        elif remN == 19:
            sieveList[sieveChunk][divN] &= 0b11011111
        elif remN == 23:
            sieveList[sieveChunk][divN] &= 0b10111111
        elif remN == 29:
            sieveList[sieveChunk][divN] &= 0b01111111

        checkN += i

# Initialize Sieve:
if __name__ == '__main__':
    size = 1024
    maxSize = size*6
    starters = [2,3,5,7,11,13,17,19,23,29]
    sieve
    sieveList = {}
    threadList = []

    for i in range(6):
        sieveList[i] = Array('b', size, lock=False)
        t = Process(target=initializeSieve, args=(size, sieveList[i]))
        threadList.append(t)
        t.start()

    for t in threadList:
        t.join()

    # Seed in the first byte numbers, the rest will plainly follow
    threadList.clear()
    for i in starters:
        t = Process(target=removeComposites, args=(i, size, maxSize, sieveList))
        threadList.append(t)
        t.start()

    for t in threadList:
        t.join()

    print (sieveList[1][8])
# Do a multi-threaded sieve test :-)
# for N in range(0, size):
#    if not N % 1000:
#        print(N, maxsize)
#
#    testN = (N+1) * 30
#    if 0b10000000 & sieve[N]:
#        Thread(removeComposites, args=(testN+1,)).start()
#    if 0b1000000 & sieve[N]:
#        Thread(removeComposites, args=(testN+7,)).start()
#    if 0b100000 & sieve[N]:
#        Thread(removeComposites, args=(testN+11,)).start()
#    if 0b10000 & sieve[N]:
#        Thread(removeComposites, args=(testN+13,)).start()
#    if 0b1000 & sieve[N]:
#        Thread(removeComposites, args=(testN+17,)).start()
#    if 0b100 & sieve[N]:
#        Thread(removeComposites, args=(testN+19,)).start()
#    if 0b10 & sieve[N]:
#        Thread(removeComposites, args=(testN+23,)).start()
#    if 0b1 & sieve[N]:
#        Thread(removeComposites, args=(testN+29,)).start()
#
# #write the sieve !
# f = open("sieve-6gb.txt", "wb")
# f.write(sieve)
# f.close()