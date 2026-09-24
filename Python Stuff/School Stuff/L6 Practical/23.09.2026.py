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
    while True:
        try:
            UserName = str(input("Enter Username: "))
            break
        except:
            print("Something went wrong. Try again...")
            P4()
    Valid1 = True
    for i in UserName:
        if i.isalpha():
            pass
        else:
            Valid = False
    Valid2 = True
    if len(UserName) in range (5,16):
        pass
    else:
        Valid2 = False
    if Valid1 and Valid2:
        print("Username is valid")
    else:
        print("Username is invalid")

def P5():
    while True:
        try:
            Password = str(input("Enter Password: "))
            break
        except:
            print("Something went wrong. Try again...")
            P5()
    Contains_Upper = False
    Contains_Lower = False
    Contains_Digit = False
    Contains_Special = False
    for i in Password:
        if i.isupper():
            Contains_Upper = True
        if i.islower():
            Contains_Lower = True
        if i.isdigit():
            Contains_Digit = True
        if i.isalnum():
            Contains_Special = True
    if Contains_Upper and Contains_Lower and Contains_Digit and Contains_Special:
        print("Password is valid")
    else:
        print("Password is invalid")

def P6():
    while True:
        try:
            Phone = int(input("Enter phone number: "))
            break
        except ValueError:
            print("Only enter numbers...")
    if len(str(Phone)) == 10:
        print("Phone number is valid")
    else:
        print("Phone number is invalid")

def P7():
    while True:
        try:
            Email = str(input("Enter email: "))
            break
        except:
            print("Something went wrong. Try again...")
    AtSign = 0
    for i in len(Email):
        if Email[i] == "@":
            AtSign = i
    if AtSign == 0:
        print("Email is invalid")
    Before_AtSign = []
    for i in range(AtSign - 1):
        Before_AtSign.append(1,Email[i])
    After_AtSign = []
    for i in range(AtSign + 1, len(Email)):
        After_AtSign.append(Email[i])
    if Before_AtSign == [] and After_AtSign == []:
        print("Email is invalid")
    else:
        print("Email is valid")

P7()

def MainMenu():
    while True:
        try:
            MenuInput = int((input(f"0: Exit Program\n1: Welcome\n2: Input Range Validation\n3: Age Verification\n4: Username Validation\n5: Password Strength Checker\n6: Phone Number Verification\n7: Email Validation\n8: Palindrome Checker\n9: Valid Username and Password Checker\nPick a program (0-10): ")))
            break
        except ValueError:
            print("Int / String Error")
            

#MainMenu()