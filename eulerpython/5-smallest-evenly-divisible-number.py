__author__ = 'omer.saeed'
number = 40

while True:
    check = 10
    while check < 20:
        if number % check != 0:
            break;
        check += 1
    if check == 20:
        print(number)
        break;
    number = number + 20