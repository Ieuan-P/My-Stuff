def P0():
    print("Exiting...")

def P1():
    print("Welcome. Go pick a program...")
    MainMenu()

def P2():
    while True:
        try:
            Number = int(input("Enter a number"))
            break
        except ValueError:
            print("Enter a number and nothing else...")
            P2()
    if Number in range(1,100):
        print(f"The number {Number} is in the range of 1 to 100")
    else:
        print(f"The number {Number} is not in the range of 1 to 100")

def P3():
    while True:
        try:
            Age = int(input("Enter your age in years: "))
            break
        except ValueError:
            print("Only enter numbers...")
            P3()
    if Age >= 18:
        print(f"You can vote!")
    else:
        print(f"You must be 18 years old to vote. Your are {Age} years old. You cannot vote!")

def P4():


def MainMenu():
    while True:
        try:
            MenuInput = int((input(f"0: Exit Program\n1: Welcome\n2: Input Range Validation\n3: Age Verification\n4: Username Validation\n5: Password Strength Checker\n6: Phone Number Verification\n7: Email Validation\n8: Palindrome Checker\n9: Valid Username and Password Checker\nPick a program (0-10): ")))
            break
        except ValueError:
            print("Int / String Error")
            

MainMenu()