def Q3():
    n = int(input("Enter a number: "))
    listn = []
    for i in range(1,51):
        if i % n == 0:
            listn.append(i)
    print(listn)

#Q3()

def Q4():
    sentence = input("Enter a sentence: ")
    sentence_without_spaces = []
    for word in sentence.split():
        sentence_without_spaces.append(word)
    print("".join(sentence_without_spaces))

#Q4()

def Q4Compact():
    print("".join(input("Enter a Sentence: ").split()))


#Q4Compact()

def Q12():
    Letters_and_Digits = input("Enter a string: ")
    Letters_in_string = 0
    Digits_in_string = 0
    for i in Letters_and_Digits:
        if i.isalpha():
            Letters_in_string += 1
        elif i.isdigit():
            Digits_in_string += 1
    print("Letters: "+str(Letters_in_string))
    print("Digits: "+str(Digits_in_string))

#Q12()

def Q12Compact():
    print(f"{(Sen := input("Enter a string: ")).replace(Sen,"")}Letters: {sum(i.isalpha() for i in Sen)}\nDigits: {sum(i.isdigit() for i in Sen)}")

#Q12Compact()

def Q13():
    Username = input("Enter a username: ")
    if Username == "admin":
        while True:
            Password = input("Enter your password: ")
            if Password == "123":
                print("Success")
                break
            else:
                print("Invalid password")
                return Q13()
    else:
        print("Invalid username")
        return Q13()

#Q13()