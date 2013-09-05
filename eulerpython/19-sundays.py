__author__ = 'omer.saeed'
yearData = [2,5,5,1,3,6,1,4,0,2,5,0]
year = 1901
sundays=0

while year < 2001:
    i = 0
    while i < 12:
        if not yearData[i]:
            sundays += 1

        yearData[i] += 1

        if not year % 4 and not year % 400 and year % 100 and i > 1:
            yearData[i] += 1

        if yearData[i] > 6:
            yearData[i] = yearData[i] % 7

        i += 1

    year += 1

print(sundays)
