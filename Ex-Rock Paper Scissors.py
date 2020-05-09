"""
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them.
print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
"""

def rps():
    usr1 = input("Enter your name user 1: \n")
    usr2 = input("Enter your name user 1: \n")
    ans1 = input("{0} What do you want to pick rock, paper or scissor: \n".format(usr1))
    ans2 = input("{0} What do you want to pick rock, paper or scissor: \n".format(usr2))
    
    
    if ans1 == ans2:
        print("Match Draw.")
    
    elif ans1 == 'rock':
        if ans2 == 'scissor':
            print("{0} Won.".format(usr1))
        else:
            print("{0} Won.".format(usr2))

    elif ans1 == 'scissor':
        if ans2 == 'paper':
            print("{0} Won.".format(usr1))
        else:
            print("{0} Won.".format(usr2))
    elif ans1 == 'paper':
        if ans2 == 'rock':
            print("{0} Won.".format(usr1))
        else:
            print("{0} Won.".format(usr2))

rps()

while input("Do you want to play again: 'y/n' \n") == "y":
    rps()
else:
    print("Bbye. Game Over. \n")
 
