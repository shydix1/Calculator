print("Welcome to the Calculator! Please press 'enter' to continue")
input()

while True:
    operator = input("Enter an operator (+, -, *, /): ")

    while operator != "+" and operator != "-" and operator != "*" and operator != "/":
        print("Invalid operator. Please enter a valid operator (+, -, *, /): ")

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    else:
        print(f"{operator} is not a valid operator")

    print(f" {num1} {operator} {num2} = {result}")

    restart = input("Thank you! Type y to restart: ")
    if restart.lower() != "y":
        print("Goodbye!")
        break