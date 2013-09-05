__author__ = 'omer.saeed'

totalComp = 0
for _2P in range(2):
    for _1P in range(3):
        for _50p in range(5):
            for _20p in range(11):
                for _10p in range(21):
                    for _5p in range(41):
                        for _2p in range(101):
                            #the jump rule comes here but not now anyway
                                if ((200 * _2P) + (100 * _1P) + (50 * _50p) + (20 * _20p) + (10 * _10p) + (5 * _5p) + (2 * _2p)) <= 200:
                                    totalComp += 1
                                    print(_2P, _1P, _50p, _20p, _10p, _5p, _2p)

print(totalComp)