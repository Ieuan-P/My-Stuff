import random

Money_Types = [2000, 1000, 500, 100, 50, 10, 5, 2, 1]

def Task1():
    value = random.randint(1, 10000)
    print (f"Value: £{value / 100}")
    for money in Money_Types:
        count = value // money
        if count > 0:
            print (f"{count} x £{money / 100}")
            value -= count * money

Task1()

def Task2():
    value = random.randint(1, 4000)
    print(f"Value: {value}")
    roman_numerals = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }
    result = ""
    for num in sorted(roman_numerals.keys(), reverse=True):
        while value >= num:
            result += roman_numerals[num]
            value -= num 
    print(f"Roman Numerals: {result}")

Task2()