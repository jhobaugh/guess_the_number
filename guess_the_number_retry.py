
# import random

import random

# create loop boolean
retry = True
#Create a while loop to loop the game if they want to try again
while retry:
    # UI asking for rules
    rules = input(str("Thanks for playing Guess the Number!!\nWould you like to see the rules of the game? (y/n): "))
    # rules if statement
    if rules == "y":
        print("You have 10 guesses!\nGuess a number between 1 and 500 and it will tell you if you are too high or too "
              "low.")
    # random number generator
    ran_num = random.randint(1, 500)
    # guess and tries variable
    guess = 0
    tries = 10
    # while loop for the guess
    while tries != 0:
        print("You have ", tries, " guesses left!")
        # guess input
        guess = int(input("Guess a number between 1 and 500: "))
        # guessing conditional
        if guess == ran_num:
            print("You win!!\n")
            break
        elif guess > ran_num:
            print("Too high! Try again!\n")
            tries -= 1
        else:
            print("Too low!! Try again!\n")
            tries -= 1
    # if else to see if you won or not
    # looping variable
    keep_going = ""
    if tries == 0:
        keep_going = input("You lose!! Would you like to try again? (y/n): ")
        if keep_going != "y":
            print("Thanks for playing!")
            break
    else:
        keep_going = input("Would you like to try again? (y/n): ")
        if keep_going != "y":
            print("Thanks for playing!")
            break





