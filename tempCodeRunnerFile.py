value1 = int(input("Please Enter first number: "))
value2 = int(input("Please enter a second number: "))

# Addition
addition = value1 + value2

# Subtraction
subtraction = value1 - value2

# Multiplication
multiplication = value1 * value2

# Division
if value2 != 0:
    division = value1 / value2
else:
    division = "Error: Division by zero is not allowed."

# Display results
print(f"{value1} + {value2}: {addition}")
print(f"{value1} - {value2}: {subtraction}")
print(f"{value1} * {value2}: {multiplication}")
print(f"{value1} / {value2}: {division}")
# This is a simple calculator program that performs basic arithmetic operations.