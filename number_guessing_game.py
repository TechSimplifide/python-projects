import random
 
rand_number = random.randint(1,100)

def play_number_guessing():   

    while True:
        try:
            num = int(input("Guess the number between 1 and 100: "))

            if num == rand_number:
                print("Congratulations! You guessed the number.")
                break
            
            elif num < rand_number:
                print("Too low!") 

            elif num > rand_number:
                print("Too high!")

        except ValueError:
            print("Please enter a valid number!")


def play_game():
    while True:
        print("Let's go to play Number guess game!")
        userOp = input("Want to continue game? [y/n]: ")
        if userOp.lower() == 'y':
            play_number_guessing()
        elif userOp.lower() == 'n':
            print("Exiting...")    
            break
    
    
    
    
play_game()


