#CHris CHen
#1/7/25
#Init
import random
wins = 0
ties = 0
losses = 0
#Function
def game():
    wins = 0
    ties = 0
    losses = 0
    print("Welcome to Rock Paper Scissors!")
    while True:
        print("Make your move. Pick one of the following: ROCK, PAPER, SCISSORS")
        player = input("Rock, Paper, Scissors, Go: ")
        system = random.randint(1,3)
        if system == 1:
            system = "ROCK"
        if system == 2:
            system = "PAPER"
        if system == 3:
            system = "SCISSORS"
        if player == "ROCK" and system == "PAPER":
            print("You Lose! The computer picked: " + system)
            losses = losses + 1
        if player == "ROCK" and system == "ROCK":
            print("The game ended in a tie! The computer picked: " + system)
            ties = ties + 1
        if player == "ROCK" and system == "SCISSORS":
            print("You win! The computer picked: " + system)
            wins = wins + 1
        if player == "PAPER" and system == "ROCK":
            print("You win! The computer picked: " + system)
            wins = wins + 1
        if player == "PAPER" and system == "PAPER":
            print("The game ended in a tie! The computer picked: " + system)
            ties = ties + 1
        if player == "PAPER" and system == "SCISSORS":
            print("You Lose! The computer picked: " + system)
            losses = losses + 1
        if player == "SCISSORS" and system == "ROCK":
            print("You Lose! The computer picked: " + system)
            losses = losses + 1
        if player == "SCISSORS" and system == "PAPER":
            print("You win! The computer picked: " + system)
            wins = wins + 1
        if player == "SCISSORS" and system == "SCISSORS":
            print("The game ended in a tie! The computer picked: " + system)
            ties = ties + 1
        playagain = input("Would you like to play again?")
        if playagain == "No":
                break

#Main
game()

























