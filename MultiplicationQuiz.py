#Chris CHen
#1/9/25

#Init
import random
global score
#Function
def quiz():
    while True:
        score = 0
        questions = input("How many questions would you like to answer?")
        for i in range(int(questions)):
            x = random.randint(1,10)
            y = random.randint(1,10)
            answer = input("What is " + str(x) + " times " + str(y) + "?")
            z = (x*y)
            if (int(answer)) == z:
                print("The answer is correct.")
            else:
                print("The answer is incorrect.")
            if (int(answer)) == z:
                score = (score + 1)
                print("Your score is " + str(score))
        playagain = input(("Would you like to play again? YES/NO"))
        if playagain == ("NO"):
            break


#Main
quiz()
