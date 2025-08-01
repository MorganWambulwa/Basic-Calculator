# First value input from the user.
value1 = int(input("Please Enter first number: "))

# Second value input from the user.
value2 = int(input("Please enter a second number: "))

# User chooses an operation.
operation = input("Please enter an operation (+, -, *, /): ")

# Basic Calculator Program
if operation == "+":
    result = value1 + value2
    print(f"{value1} + {value2} = {result}")


elif operation == "-":
    result = value1 - value2
    print(f"{value1} - {value2} = {result}")


elif operation == "*":
    result = value1 * value2
    print(f"{value1} * {value2} = {result}")


elif operation == "/":
    if value2 != 0:
        result = value1 / value2
        print(f"{value1} / {value2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")    
else:
    print("Invalid operation. Please enter one of +, -, *, or /.")