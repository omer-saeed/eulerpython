__author__ = 'omer.saeed'
number_chars = {1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4, 10:3, 11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8, 20:6, 30:6, 40:5, 50:5, 60:5, 70:7, 80:6, 90:6, 100:7, 1000: 8 }
and_chars = 3
total_hundreds = 10

sum = ((number_chars[1]+ number_chars[1000]) +
       (99 * (total_hundreds - 1) * and_chars) +
       (number_chars[100] * 100 * (total_hundreds -1)) +
       ((number_chars[90] +  number_chars[80] + number_chars[70] + number_chars[60] + number_chars[50] + number_chars[40]+ number_chars[30] + number_chars[20]) * 10 * total_hundreds) +
       ((number_chars[19] +  number_chars[18] + number_chars[17] + number_chars[16] + number_chars[15] + number_chars[14]+ number_chars[13] + number_chars[12] + number_chars[11] + number_chars[10]) * total_hundreds) +
       ((number_chars[9] +  number_chars[8] + number_chars[7] + number_chars[6] + number_chars[5] + number_chars[4]+ number_chars[3] + number_chars[2] + number_chars[1]) * ((9 * 10)+100))
    )

print(sum)