import csv
from datetime import datetime

FILE_NAME = "expense_record.csv"

def create_file():
    try:
        file = open(FILE_NAME,'x',newline="")
        write = csv.writer(file)
        write.writerow(['DATE', 'TIME', 'CATEGORY', 'AMOUNT', 'DISCRIPTION'])
    except FileExistsError:
        pass
    

def add_expences():
    date = input("Enter date [DD-MM-YYYY] or press Enter for today: ")
    if not date:
        date = datetime.today().strftime("%d-%m-%Y")
    time = datetime.today().strftime("%H:%M:%S")
    
    category = input("Enter category [ex. Education, Food, Transport, etc.]: ")
    amount = input("Enter expense amount:")
    discription = input("Enter some short discription about expense: ")
    
    file = open(FILE_NAME,'a', newline="")
    writer = csv.writer(file)
    writer.writerow([date, time, category, amount, discription])
    print("Expense added successfully!\n")
    
  
def show_expenses():
    print("Your expenses are:\n")
    
    file = open(FILE_NAME, 'r')
    reader = csv.reader(file)
    for row in reader:
        print(", ".join(row))
    print()


def menu():
    print("***** Expense Tracker *****")
    print("1. Add Expense")
    print("2. View Expenses") 
    print("3. Exit")
    

def evaluate_expense():
    while True:
        menu()
        choice = input("Enter your choice from above: ")

        if choice == '1':
            add_expences()
        elif choice == '2':
            show_expenses()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Please enter valid choice!!")
        
                   
create_file()
evaluate_expense()