"""
CREDIT CARD VALIDATION SYSTEM
Check if a credit card number is valid or not.
Use the Luhn algorithm to validate the card number.
"""

from random import randint as random


# provider = '37'
# bin = str(random(1111, 9999))
banks = ['547155','547156','547086','542073','557764','406447','400185','400187','400191','400195','400196','400197','400199','400217','400225','400234','400235','400236','400237','400238','400239','400242','400243','400245','400247']
bin = banks[random(0, len(banks)-1)]
bin = '418076'
account_number = str(random(111111111, 999999999))

card_number = bin + account_number
# print(card_number)

lenght = len(card_number)

if lenght % 2 == 0:
    start_dup = 1
    start_reg = 0
else:
    start_dup = 0
    start_reg = 1

def iterate(factor1, factor2, operator):
    factor1 = int(factor1)
    factor2 = int(factor2)
    if operator == '+':
        factor1 += factor2
    elif operator == '-':
        factor1 -= factor2
    elif operator == '*':
        factor1 *= factor2
    elif operator == '/':
        factor1 /= factor2
    return str(factor1)

def luhn_algorithm(card_number):
    digit_sum = 0
    for i in range(start_dup, lenght, 2):

        curr_num = int(card_number[i])
        double_digit = iterate(curr_num, 2, '*')

        if int(double_digit) > 9:
            double_digit = iterate(double_digit[0], double_digit[1], '+')
        digit_sum += int(double_digit)
    
    for i in range(start_reg, lenght, 2):
        digit_sum += int(card_number[i])
    return digit_sum



digit_sum = luhn_algorithm(card_number)
print(digit_sum)

if digit_sum % 10 == 0:
    print("Card is valid")
else:
    print("Fixing your card")
    missing_num = 10 - (digit_sum % 10)
    card_number += str(missing_num)
print(card_number)


        