__author__ = 'omer.saeed'

def fib(last, cur):
    if cur > 4000000:
        return 0
    if cur % 2 == 0:
        return cur + fib(cur, last + cur)
    else:
        return fib(cur, last + cur)

print(fib(1,2))
