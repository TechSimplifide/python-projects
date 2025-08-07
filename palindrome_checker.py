import re

def clean_text(text):
    return re.sub(r'[^a-zA-Z0-9]','',text).lower()

def save_to_file(text):
    file = open('palindrome_data.txt','a')
    file.write(f"{text}\n")
    file.close()


def display_palindrome():
        try: 
            file = open('palindrome_data.txt','r')
            palindromes = file.readlines()
            file.close()
            
            if palindromes:
                print("\nFollowing are the list of palindromes:")
                for line in palindromes:
                    print(line.strip())
            else:
                print("No palindromes saved yet.")

        except FileNotFoundError:
            print("\n No such file found")
    
    

def menu():
    print("=+=+=+=MENUE=+=+=+=")
    print("1. Check palindrome")
    print("2. Show list of all palindromes")
    # print("3. Display the total number of palindromes")
    print("3. Exit")

    
def check_palindrome_logic():
    text = input("\nEnter a word to check if it's palindrome: ").strip()
    normal_text = clean_text(text)
    reverse_text = normal_text[::-1]
    
    if normal_text == reverse_text:
        save_to_file(text)
        print("It is palindrome")   
    else:
        print("It is not palindrome")


def menu_logic():
    while True:
        menu()
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                check_palindrome_logic()
                continue
            
            elif choice == 2:
                display_palindrome()
                continue    
            
            # elif choice == 3:
            #     pass

            elif choice == 3:
                print("Exiting...")
                break
            else:
                print("Please enter valid option [1, 2 or 3]")
        
        except ValueError:
            print("Please enter a valid number [1, 2, or 3].")
            continue
        
    


def palindromeChecker():

        menu_logic()
        

palindromeChecker()


