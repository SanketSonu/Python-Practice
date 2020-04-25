"""
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them.
print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
"""
import sys

def compare():
    user1 = input("Enter your name. Player 1: \n")
    user2 = input("Enter your name. Player 2: \n")

    a = input("{0} Choose any 1 from Rock, Paper and Scissor: \n".format(user1))
    b = input("{0} Choose any 1 from Rock, Paper and Scissor: \n".format(user2))

    if a == b:
        print("It's a tie!")
    elif a == 'rock':
        if b == 'scissors':
            print("Rock wins!")
        else:
            print("Paper wins!")
    elif a == 'scissors':
        if b == 'paper':
            print("Scissors win!")
        else:
            print("Rock wins!")
    elif a == 'paper':
        if b == 'rock':
            print("Paper wins!")
        else:
            print("Scissors win!")

compare()

while input("Do you want to play again: y/n \n") == 'y':
    compare()
else:
    print("Bbye")
    exit(0)
 
