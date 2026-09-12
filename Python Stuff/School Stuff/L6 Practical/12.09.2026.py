import random

def Q5():
    n = int(input("Enter a number greater than 2: "))
    if n <= 2:
        print("This number is not greater than 2")
        Q5()
    else:
        prime = f"{n} is a prime number"
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                prime = f"{n} is not a prime number"
                break
        print(prime)

def Q6():
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    num3 = random.randint(1,10)
    num4 = random.randint(1,10)
    num5 = random.randint(1,10)
    print(f"The average of the five random numbers is: {(num1+num2+num3+num4+num5)/5}")

Q6()