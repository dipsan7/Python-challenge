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
print(logo)

def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2    
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
operation ={"+":add,
            "-":subtract,
            "*":multiply,
            "/":divide
}
def calculator():
    num1=float(input("what is your 1st number"))
    for symbol in operation:
        print(symbol)
    should_continue=True

    while should_continue:
        operation_symbol=input("pick an operation ")
        num2=float(input("what is your next number"))
        calculation=operation[operation_symbol]
        answer=calculation(num1,num2)
        print(f"{num1}{operation_symbol}{num2} is {answer}")
        continues=input("do you want to continue if yes type 'yes'else 'no'for new calculation")
        if continues=='yes':
            num1=answer
            
        else:
            should_continue=False
            calculator()
calculator()
