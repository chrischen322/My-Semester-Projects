#Chris Chen
#1/29/25

#Init
import random
global points
#Function
symbols = ["7","♣","♠"]
spin =[]
points = 100
print("""Welcome to the Diamond Casino.
If you are here it must mean one thing.
You are here to GAMBLE!!!
Landing on 3 of the same symbol will result in a win.
Landing on 3 of the number 7 however, is a JACKPOT.
Otherwise you lose.""")
while True:
    action = input("Would you like to make your spin? YES/NO ")
    if action in ["Yes", "yes", "y", "Y"]:
        bet = int(input("Enter your bet amount: "))
        points = points - bet
        if points < 0:
            print("You ran out of money.")
            break
        print("You now have " + str(points) + " points.")
        print("The slots are rolling!")
        for i in range(3):
            print("Rolling ...")
        spin = []  # Clear the spin list for each new spin
        for i in range(3):
            weights = [1, 3, 3]
            symbol = random.choices(symbols, weights = weights)[0]
            spin.append(symbol)
            print(symbol)
        if spin == ["7", "7", "7"]:
            points = points + 1000
            print("YOU WIN THE JACKPOT!!!!")
            print("You won 1000 more points!")
        elif spin == ["♣", "♣", "♣"]:
            print("You beat the casino!")
            print("You won 100 more points!")
            points = points + 100
        elif spin == ["♠", "♠", "♠"]:
            print("You beat the casino!")
            print("You won 100 more points!")
            points = points + 100
        else:
            print("You lost all your money.")
        playAgain = input("Would you like to play again? YES/NO ")
        if playAgain not in ["Yes", "yes", "y", "Y"]:
            break

#Main

