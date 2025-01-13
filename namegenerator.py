#Chris CHen
#10/18/24

#Init
#Function
def crunchy_or_rainy():
    answer = input("Would you say you're more Crunchy(1) or Rainy(2)?")
    if answer.lower() == "crunchy" or answer == "1":
         print("Your favorite color is: Orange")
         return True
    elif answer.lower() == "rainy" or answer == "2":
        print("Your favorite color is: Blue")
        return True
    else:
        print("Please enter a valid response")
def hot_or_cold():
    answer = input("Would you say you prefer being hot(1) or cold(2)?")
    if answer.lower() == "hot" or answer == "1":
         print("Your favorite color is: Green")
         return True
    elif answer.lower() == "cold" or answer == "2":
        print("Your favorite color is: Cyan")
        return True
    else:
        print("Please enter a valid response")
def sweet_or_sour():
    answer = input("Would you say you prefer more sweet(1) or sour(2)?")
    if answer.lower() == "sweet" or answer == "1":
        print("Your favorite color is: Red")
        return True
    elif answer.lower() == "sour" or answer == "2":
        print("Your favorite color is: Yellow")
        return True
    else:
        print("Please enter a valid response")
def lovely_or_wine():
    answer = input("Would you say you prefer more lovely(1) or wine(2)?")
    if answer.lower() == "lovely" or answer == "1":
        print("Your favorite color is: Pink")
        return True
    elif answer.lower() == "wine" or answer == "2":
        print("Your favorite color is: Purple")
        return True
    else:
        print("Please enter a valid response")
        return False
def pumpkin_or_melon():
    answer = input("Would you say you prefer more pumpkins(1) or melons(2)?")
    if answer.lower() == "pumpkins" or answer == "1":
        go = False
        while go == False:
            go = crunchy_or_rainy()
    elif answer.lower() == "melons" or answer == "2":
        go = False
        while go == False:
            go = hot_or_cold()
    else:
        print("Please enter a valid response")
        return False
def berry_or_grape():
    answer = input("Would you say you prefer more berry(1) or grape(2)?")
    if answer.lower() == "berry" or answer == "1":
        go = False
        while go == False:
            go = sweet_or_sour()
    elif answer.lower() == "grape" or answer == "2":
        go = False
        while go == False:
            go = lovely_or_wine()
    else:
        print("Please enter a valid response")
        return False
def big_or_small():
    answer = input("Are you Big(1) or Small(2)")
    if answer.lower() == "big" or answer == "1":
        go = False
        while go == False:
            go = pumpkin_or_melon()
    elif answer.lower() == "small" or answer == "2":
        go = False
        while go == False:
            go = berry_or_grape()
def quizzington():
    go = False
    while go == False:
        go = big_or_small()
#Main
quizzington()
