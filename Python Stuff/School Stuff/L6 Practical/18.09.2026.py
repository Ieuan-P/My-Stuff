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

#CardNumber = input("Enter a credit card number: ")
#CardNumber = CardNumber.replace(" ", "")

#if Luhn(CardNumber):
    print("The credit card number is valid.")
#else:
    print("The credit card number is invalid.")

def Q14():
     int1 = int(input("Enter a number: "))
     int2 = int(input("Enter a number: "))
     final = 0
     val1 = int1
     for i in range(int2):
          final += val1
          val1 = val1 * 10 + int1
     print(f"The final value is: {final}")

#Q14()

def Q15():
     sentence = str(input("Enter a sentence: "))
     words = sentence.split()
     print(f"The longest word in the sentence is: {max(words, key=len)}")

Q15()