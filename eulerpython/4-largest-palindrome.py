__author__ = 'omer.saeed'
max_num = 999
while max_num > 100:
    max_num = max_num - 1
    palindrome = max_num * 1000 + ((max_num % 10) * 100) + (((max_num % 100) // 10) * 10) + (max_num // 100)

    #attempt to find a three digit number that divides this palindrome
    divisor = 999
    while divisor >= 100:
        if palindrome // divisor > 1000:
            break
        if palindrome % divisor == 0:
            print(palindrome)
            exit(0)
        divisor = divisor - 1
