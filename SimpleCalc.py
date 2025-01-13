#Chris Chen
#11/18/24

#Init

#Functions
def calculator():
    print("Welcome to Simple Calculator.")
    while True:
        print("Please choose an operation.")  #1-5 asks the user what function they want to perform. 1 = Add, 2 = Subtract, 3 = Multiply, 4 = Divide, 5 = Quit
        print("""1. Add
        2. Subtract
        3. Multiply
        4. Divide
        5. Quit """)
        option = int(input("1-5:"))  #Asking the user for the respective numbers that will be used when performing the selected operation
        if option == 1:
            num1 = int(input("Please enter the first number: "))
            num2 = int(input("Please enter the second number: "))
            add(num1,num2)
        if option == 2:
            num1 = int(input("Please enter the first number: "))
            num2 = int(input("Please enter the second number: "))
            subtract(num1,num2)
        if option == 3:
            num1 = int(input("Please enter the first number: "))
            num2 = int(input("Please enter the second number: "))
            multiply(num1,num2)
        if option == 4:
            num1 = int(input("Please enter the first number: "))
            num2 = int(input("Please enter the second number: "))
            divide(num1,num2)
        if option == 5:   #Quit function if user selects option 5
            quit()
            break
def add(num1, num2):  #Performing indicated functions
    answer = num1 + num2
    print(answer)

def subtract(num1, num2):
    answer = num1 - num2
    print(answer)
def multiply(num1, num2):
    answer = num1 * num2
    print(answer)
def divide(num1, num2):
    answer = num1 / num2
    print(answer)
def quit():
    while True:
        print("The Simple Calculator is closing.")
        break
#Main
calculator()

