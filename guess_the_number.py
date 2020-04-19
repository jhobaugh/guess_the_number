
'''
2. Guess the Number
The Goal: Similar to the first project,
this project also uses the random module in Python.
The program will first randomly generate a number unknown to the user.
The user needs to guess what that number is. (In other words, the user needs to be able to input information.)
If the user’s guess is wrong, the program should return some sort of indication as to how wrong (e.g. The number is too high or too low).
If the user guesses correctly, a positive indication should appear.
You’ll need functions to check if the user input is an actual number, to see the difference between the inputted number and the randomly generated numbers, and to then compare the numbers.
'''

# my 1st attempt

'''import random

retry_loop = True
correct = True
looper = True
while retry_loop:
    secret_number = random.randint(1, 5000)
    print(secret_number)
#    correct = True
    while correct:
        guess = int(input("Guess the number (1 - 5000: "))
        looper = True
        while looper:
            if guess > secret_number:
                print("Too high! Try again!: ")
                looper = False
            elif guess < secret_number:
                print("Too low! Try again!: ")
                looper = False
            else:
                print("Correct! Good Job!")
                looper = False
                correct = False
                retry_loop = False
                break 
retry = str(input("Want to try again? (y/n): "))
if retry == "y" or "Y":
    print("")
else:
    print("Thanks for playing!")
    looper = False
    retry_loop = False
    correct = False'''

# example found online
'''
import random

print("Number guessing game")

# randint function to generate the
# random number b/w 1 to 9
number = random.randint(1, 9)

# number of chances to be given
# to the user to guess the number
# or it is the inputs given by user
# into input box here number of
# chances are 5
chances = 0

print("Guess a number (between 1 and 9):")

# While loop to count the number
# of chances
while chances < 5:

    # Enter a number between 1 to 9
    guess = int(input())

    # Compare the user entered number
    # with the number to be guessed
    if guess == number:

        # if number entered by user
        # is same as the generated
        # number by randint function then
        # break from loop using loop
        # control statement "break"
        print("Congratulation YOU WON!!!")
        break

    # Check if the user entered
    # number is smaller than
    # the generated number
    elif guess < number:
        print("Your guess was too low: Guess a number higher than", guess)

        # The user entered number is
    # greater than the generated
    # number
    else:
        print("Your guess was too high: Guess a number lower than", guess)

        # Increase the value of chance by 1
    chances += 1

# Check whether the user
# guessed the correct number
if not chances < 5:
    print("YOU LOSE!!! The number is", number)
'''

import random

print("Number guessing game:\nPick a number between 1 and 500: ")

keepgoing = True

number = random.randint(1, 500)
print(number)
while keepgoing:
    guess = int(input(""))

    if guess == number:
        print("Congrats! YOU WIN!!")
        keepgoing = False
    elif guess > number:
        print("Number too high! Guess a number lower than", guess)
    else:
        print("Guess was too low! Guess a number higher than", guess)
