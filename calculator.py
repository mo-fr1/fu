# Simple Calculator for Beginners

# Step 1: Get two numbers from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Step 2: Get the operation they want to perform
operation = input("Enter operation (+, -, *, /): ")

# Step 3: Perform the calculation
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Cannot divide by zero!"
else:
    result = "Error: Invalid operation!"

# Step 4: Show the result
print(f"{num1} {operation} {num2} = {result}")
