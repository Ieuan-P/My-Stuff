def numbers(n):
        return [int(d) for d in str(n)]

def Luhn(number):
    digits = numbers(number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(numbers(d * 2))
    return checksum % 10 == 0

CardNumber = input("Enter a credit card number: ")
CardNumber = CardNumber.replace(" ", "")

if Luhn(CardNumber):
    print("The credit card number is valid.")
else:
    print("The credit card number is invalid.")