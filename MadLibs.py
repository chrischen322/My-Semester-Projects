#Chris Chen
#12/9/24

#Init
def mad_libs():
    adjective = input("Please enter an adjective: ")        #Asks for inputs
    article_of_clothing = input("Please choose an article of clothing: ")
    location = input("Please enter a location: ")
    food = input("Please choose your favorite food: ")        #Puts inputs together into the preselected format below
    print("What a" + " " + adjective + " " + "day! I believe it is a great day to wear my" + " " + article_of_clothing + " " + "today. With this weather I must go and visit" + " " + location + "." + " " + "I'd best grab a snack before heading out today. I'm feeling some" + " " + food + ".")

#Function

#Main
mad_libs()
