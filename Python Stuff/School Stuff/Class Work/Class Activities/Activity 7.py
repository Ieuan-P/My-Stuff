# Write a for loop so that every element in the list "ANIMALS" is displayed with an sensible output.

ANIMALS = ["koala", "cat", "fox", "panda", "chipmunk", "sloth", "penguin", "dolphin"]
p1x = 1
CF = 1
CFX = 1


def P1():
    for p1x in range(1,8):
        print (ANIMALS[p1x])

# Write a program to convert temperature between Celsius and Fahrenheit

def P2():
    CF = input("Celsius or Fahrenheit? (Celsius or Fahrenheit)").lower()
    CFX = int(input("Temperature? (Intiger)"))
    if CF == "celsius":
        print(CFX * (9/5) + 32,"°F (Fahrenheit)")
    elif CF == "fahrenheit":
        print((CFX - 32) * (5/9),"°C (Celsius)")
P1()