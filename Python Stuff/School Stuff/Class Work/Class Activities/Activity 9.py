# Activity 9
def p1():    
    Array1 = [1,2,3,4,5,6,7,8,9,10]
    Array2 = [1,3,5,9,11,13]
    Output = []
    for x in Array1:
        if x in Array2:
            Output.append(x)
    print(Output)
p1()

