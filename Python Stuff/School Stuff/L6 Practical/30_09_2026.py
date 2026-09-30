def checkstring(xstring):
    
    if len(xstring) not in range(5,8):
        return "String must be between 5 and 7 characters in length (inclusive)"
    
    for char in xstring:
    
        if char.isalpha() != True:
            return "String must contain only letters"
            break
    
        if char.islower():
            return "String must contain only uppercase letters"
            break
    
        if sum(1 for item in xstring if item == char) != 1:
            return "String must contain only unique characters"
            break
    else:
        return "String is Valid"

def main():
    IsValid = checkstring(input("Enter a string: "))
    print(IsValid)
    if IsValid != "String is Valid":
        main()

#main()
nstring = "abcde"
print()