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

Q5()