"""
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""

import random

count = 0
def game():
    a = random.randint(1, 9)
    b = int(input("Enter any number between 1 and 9: \n"))

    if b == a:
        print("You are right")
    elif b < a:
        print("Your guessed number is too low. ")
    else:
        print("Your guessed number is too high.")

game()

while input("Do you want to play again: y or q \n") == "y":
    count += 1
    game()
    

else:
    print("You played this game {0} times. Bbye..!!".format(count+1))


    
