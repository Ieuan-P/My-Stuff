import math

def Q9():
    n = int(input("Enter a number: "))
    Nsum = sum(int(d) for d in str(n))
    print(f"The sum of the digits of {n} is: {Nsum}")

#Q9()

def Q10():
    xstring = str(input("Enter a string: "))
    xstring = xstring.lower()
    xlist = list(xstring.strip("*"))
    if xlist[0] == "v" and xlist[1] == "e" and xlist[2] == "r" and xlist[3] == "y":
        print(xstring)
    else:
        print("very"+xstring)

#Q10()

def Q11():
    xstring = str(input("Enter a string: "))
    nint = int(input("Enter a number: "))
    xlist = list(xstring)
    xlist.pop(nint-1)
    xstring = ''.join(xlist)
    print(xstring)

#Q11()

def Q12():
    xstring = str(input("Enter a string: "))
    xlist = list(xstring)
    temp1 = xlist[0]
    temp2 = xlist[(len(xlist)-1)]
    xlist[0] = temp2
    xlist[len(xlist)-1] = temp1
    xstring = ''.join(xlist)
    print(xstring)

#Q12()

