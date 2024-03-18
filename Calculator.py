logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

#addition
def add(a,b):
    return a+b
    
#subtraction
def sub(a,b):
    return a-b
    
#multiplication
def mul(a,b):
    return a*b

#division
def div(a,b):
    return a/b
    
#exponentiation
def power(a,b):
    return a**b
    
#square
def square(a):
    return a**2
    
#squareroot
def root(a):
    return a**0.5
    
operators=dict()
operators["+"]=add
operators["-"]=sub
operators["*"]=mul
operators["/"]=div
operators["**"]=power
operators["sqr"]=square
operators["root"]=root

def calculator():
    
    print(logo)
    
    num1=float(input("enter first number: "))
    
    for i in operators:
        print(i)
    
    repeat=True
    
    while repeat:
        
        operator=input("choose the operation from the above: ")
        
        if operator=="sqr" or operator=="root":
            result=operators[operator](num1)
            print(f"{operator} of {num1} = {result}")
        else:
            num2=float(input("enter next number: "))
            result=operators[operator](num1,num2)
            print(f"{num1} {operator} {num2} = {result}")
            
        cont=input("if you want to continue with previous input, type 'y' or 'n' \nor if you want to restart with a new input type 'a': ")
        
        if cont=="y":
            num1=result
        elif cont=="n":
            repeat=False
        else:
            calculator()

calculator()
