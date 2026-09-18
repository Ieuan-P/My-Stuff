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

number = input("Enter a credit card number: ")

if Luhn(number):
    print("The credit card number is valid.")
else:
    print("The credit card number is invalid.")