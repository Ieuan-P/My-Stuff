# Develop an algorithm, using either python or a flowchart, that checks if the user has entered a string that represents a valid machine code instruction.
# The machine code instruction is valid if it contains exactly eight characters and all of those characters are either '0' or '1'.

# The algorithm should:
# - prompt the user to enter an 8-bit machine code instruction and store it in a variable
# - check that the instruction only contains the characters '0' or '1'
# - check that the instruction is exactly eight characters long
# - output 'ok' when the instruction is valid, otherwise it should output 'wrong'

#  For example:
# - if the user enters the string '00101110' it should output 'ok'
# - if the user enters the string '11110' it should output 'wrong'
# - if the user enters the string '1x011001' it should output 'wrong'.


def check(string):
    length_8 = False
    Only_0_or_1 = True
    
    if len(string) == 8:
        length_8 = True
    
    for char in string:
        if char not in "01":
            Only_0_or_1 = False
    
    if length_8 == True and Only_0_or_1 == True:
        print("ok")
    else:
        print("wrong")

check(input("Enter an 8-bit machine code instruction: "))