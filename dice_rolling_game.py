import random

def diceScrolling():
    while True:
        
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)

        userInp = input("Roll the dice? (y/n): ")

        if userInp in {'Y','y'}:

            print(f"({dice1}, {dice2})")

        elif userInp in {'n','N'}:

            print("Thank you for playing!")
            break        
        else:
            print("Invalid choice!")
    

diceScrolling()

