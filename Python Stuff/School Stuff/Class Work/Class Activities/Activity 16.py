#Activity 16

#Sorting numbers
Numbers = [45, 88, 65, 12, 42, 99]
Numbers = sorted(Numbers)
ReverseNumbers = sorted(Numbers, reverse=True)
print ("\nSorting Numbers: ")
print (Numbers)
print (ReverseNumbers)

#Sorting upper case and lower case into two lists
Input = "Once A Upon A Time, There was"
UpperCase = []
LowerCase = []
for char in Input:
    if char.isupper():
        UpperCase.append(char)
    elif char.islower():
        LowerCase.append(char)
print ("\nSorting Upper Case and Lower Case Letters: ")
print("Upper Case Letters: ", UpperCase)
print("Lower Case Letters: ", LowerCase)

#Find the largest and smallest number without using Max and Min
Numbers2 = [11, 99, 55, 33, 22, 88, 66, 77, 44]
Largest = Numbers2[0]
Smallest = Numbers2[0]
for num in Numbers2:
    if num > Largest:
        Largest = num
    if num < Smallest:
        Smallest = num
print ("\nFinding Largest and Smallest Numbers: ")
print("Largest Number: ", Largest)
print("Smallest Number: ", Smallest)

#Sort Words by Length in Ascending Order
Input2 = "Whilst this is that make no sense"
Words = Input2.split()
Words = sorted(Words, key=len)
print ("\nSorting Words by Length: ")
print(Words)