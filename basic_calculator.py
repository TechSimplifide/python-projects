def menu():
    lists = "Menu"
    print(lists.center(40,"="))
    print("[ 1 for ADD ]")
    print("[ 2 for SUB ]")
    print("[ 3 for MUL ]")
    print("[ 4 for DIV ]")
    print("[ 5 for POW ]")


def take_options():
    fixed_options = ['1','2','3','4','5']
    while True:
        options = input("Enter the operation from above given lists: ")
    
        if options not in fixed_options:
            print("Please enter the valid options!")
            continue
        return options
    

def evaluations():
    op = take_options()
    try:    
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Please enter valid number!")
        return

    match op:
        case '1':
            print(f"The sum is: {num1 + num2}") 
        case '2':
            print(f"The subtraction is: {num1 - num2}") 
        case '3':
            print(f"The multiplication is: {num1 * num2}") 
        case '4':
            if num2 == 0:
                print("Value can't divide by zero!")
                return
            else:
                print(f"The division is: {num1 / num2}") 
        case '5':
            print(f"The power is: {num1 ** num2}") 
        

    
    
def calculator():
    menu()
    evaluations()

    
            
while True:
    val = input("You want to continue then enter (yes,no): ")         
    if val in {"yes","YES",'y','Y'}:
        calculator()
    else:
        print("The program is exit..")
        break    
