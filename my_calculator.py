# Simple calculator program

# simple addition, subtraction, multiplication, and division functions below

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


# starting the program from here
print("Hi there!")
print("Let's solve some arithmetic calculations")
while True:

    # ask and grab user input for operation
    print("\nWhat is your desired operation?")
    choice = input("Please enter one of these symbols +, -, *, or /:")

    # check if user choice is one of the four options of symbols
    if choice in ('+', '-', '*', '/'):
        num1 = int(input("Enter your first number: "))
        num2 = int(input("Enter your second number: "))

        if choice == '+':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '-':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '*':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '/':
            print(num1, "/", num2, "=", divide(num1, num2))

        # user can continue if desired
        # y will continue the program, n will stop it
        more_calc = input("Would you like to continue? (y/n): ")
        if more_calc == "n":
            print("\nThank you for using this simple calculator")
            print("Goodbye!")
            break

    else:
        print("\nOh no! Invalid input, please try again")
