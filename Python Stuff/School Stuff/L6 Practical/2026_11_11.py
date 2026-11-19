# https://www.codewars.com/kata/5a331ea7ee1aae8f24000175/python

Start_Row = str(input("1st row: "))
list1 = []
list2 = []
for x in range(len(Start_Row)):
    list1.append(Start_Row[x])
print (list1)
while len(list1) > 1:
    for x in range(len(list1) - 1):
        if list1[x] == list[x+1]:
            list2.append(list1.x)
        elif list1[x] 