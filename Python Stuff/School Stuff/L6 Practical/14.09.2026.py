import random

Money_Types = [2000, 1000, 500, 100, 50, 10, 5, 2, 1]

def main():
    value = random.randint(1, 10000)
    print (f"Value: £{value / 100}")
    for money in Money_Types:
        count = value // money
        if count > 0:
            print (f"{count} x £{money / 100}")
            value -= count * money

main()

