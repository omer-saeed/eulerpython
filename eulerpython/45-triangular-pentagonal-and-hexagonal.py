__author__ = 'omersaeed'

# Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
# Pentagonal	 	Pn=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
# Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...

a = 0
b = 0
c = 0
while True:
    an = a * (a + 1) / 2
    bn = b * ((3*b) - 1) / 2
    cn = c * (2*c - 1)

    if an == bn == cn:
        print(an)
        a += 1
    elif an <= bn and an <= cn:
        a += 1
    elif bn <= an and bn <= cn:
        b += 1
    elif cn <= an and cn <= bn:
        c += 1
    else:
        print("CRAP!")
