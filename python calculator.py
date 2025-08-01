# Simple calculator with 4 operations

# Input numbers and operator
num1 = float(input("Enter the first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

# Perform calculation
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "undefined (division by zero)"
else:
    result = "invalid operator"

# Display result
if isinstance(result, (int, float)):
    print(f"{num1} {operator} {num2} = {result}")
else:
    print(f"Error: {result}")
