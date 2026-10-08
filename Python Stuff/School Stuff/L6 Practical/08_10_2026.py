def checkstring(xstring):
    
    if len(xstring) not in range(5,8):
        return f"({xstring}) String must be between 5 and 7 characters in length (inclusive)"
    
    for char in xstring:
    
        if char.isalpha() != True:
            return f"({xstring}) String must contain only letters"
            break
    
        if char.islower():
            return f"({xstring}) String must contain only uppercase letters"
            break
    
        if sum(1 for item in xstring if item == char) != 1:
            return f"({xstring}) String must contain only unique characters"
            break
    
    if sum(ord(item) for item in xstring) not in range (420,601):
        return f"({xstring}) Sum of ASCII values must be between 420 and 600 (inclusive)\nCurrent sum is: {sum(ord(item) for item in xstring)}"
    
    else:
        return f"({xstring}) String is Valid"

def main():
    UserInput = input("Enter a string: ")
    IsValid = checkstring(UserInput)
    print(IsValid)
    if IsValid != f"({UserInput}) String is Valid":
        main()

main()