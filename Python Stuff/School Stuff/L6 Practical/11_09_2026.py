def Q1():
    x = int(input("X: "))
    y = int(input("Y: "))
    if x == 10 or y == 10 or (x + y) == 10:
        print("Yes")

def Q2():
    n = int(input("Enter a number: "))
    if n in range(90,111):
        print("True")
    else:
        print("False")

def Q3():
    n = int(input("Enter a number: "))
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")

def Q4():
    UserName = input("Enter your name: ")
    Date_Of_Birth = input("Enter your date of birth (DD-MM-YYYY): ")
    Year_Of_Birth = int(Date_Of_Birth.split("-")[2])
    Month_Of_Birth = int(Date_Of_Birth.split("-")[1])
    Day_Of_Birth = int(Date_Of_Birth.split("-")[0])
Q4()