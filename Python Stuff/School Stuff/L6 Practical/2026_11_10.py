Num1 = 0
Num2 = 0

class Calculator:
    def __init__(self):
        pass

    def add(self, Num1, Num2):
        return (Num1 + Num2)
    def sub(self, Num1, Num2):
        return (Num1 - Num2)
    def mult(self, Num1, Num2):
        return (Num1 * Num2)
    def div(self, Num1, Num2):
        return (Num1 / Num2)
    def Action(self, Action, Num1, Num2):
        if Action == "add":
            return self.add(Num1, Num2)
        elif Action == "sub":
            return self.sub(Num1, Num2)
        elif Action == "mult":
            return self.mult(Num1, Num2)
        elif Action == "div":
            return self.div(Num1, Num2)
        
 
MyCalc = Calculator()

def main():
    
    while True: # Num1 is less than or equal to 12 digits in length

        while True: # Num1 is a numerical value
            
            try:
                Num1 = int(input("Number 1: "))
                break
            
            except ValueError:
                print("\n\n\n\n\n\n\n\n\n\nError: input must be a positive numerical integer\n\n\n\n\n\n\n\n\n\n")
        
        if len(str(Num1)) <= 12: break
        
        else: print("Error: input must not exceed 12 digits in length")
    
    while True: # Num2 is less than or equal to 12 digits in length
        
        while True: # Num1 is a numerical value
            
            try:
                Num2 = int(input("Number 2: "))
                break
            
            except ValueError:
                print("\n\n\n\n\n\n\n\n\n\nError: input must be a positive numerical integer\n\n\n\n\n\n\n\n\n\n")
        
        if len(str(Num1)) <= 12: break
        
        else: print("Error: input must not exceed 12 digits in length")
    
    while True:
        
        Action = input("Enter either 'add', 'sub', 'mult', or 'div': ").lower()
        
        if Action in {
            
            "add",
            "sub",
            "mult",
            "div"
        
        }: break
        
        print("\n\n\n\n\n\n\n\n\n\nError: enter a type from the list\n\n\n\n\n\n\n\n\n\n")

    result = MyCalc.Action(Action, Num1, Num2)
    
    if Action == "add":
        print(f"{Num1} + {Num2} = {result}")
    
    elif Action == "sub":
        print(f"{Num1} - {Num2} = {result}")
    
    elif Action == "mult":
        print(f"{Num1} x {Num2} = {result}")
    
    elif Action == "div":
        print(f"{Num1} / {Num2} = {result}")

main()