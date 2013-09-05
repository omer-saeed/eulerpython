__author__ = 'omer.saeed'

basePermutation = [0,1,2,3,4,5,6,7,8,9]
max = 10
def permuteNext():
    k = max - 1
    while k > 0:
        k -= 1
        if basePermutation[k] < basePermutation[k+1]:
            l = max
            while l > k:
                l -= 1
                if basePermutation[k] < basePermutation[l]:
                    t = basePermutation[l]
                    basePermutation[l] = basePermutation[k]
                    basePermutation[k] = t
                    x = k+1
                    y = max - 1
                    while x < y:
                        t = basePermutation[x]
                        basePermutation[x] = basePermutation[y]
                        basePermutation[y] = t
                        x += 1
                        y -= 1
                    break

            break

num = 1
while num < 1000000:
    permuteNext()
    num += 1

print(basePermutation)
