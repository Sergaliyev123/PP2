# Step 1: Ask the user to enter two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Step 2: Ask the user for the operation
operation = input("Enter the operation (+, -, *, /): ")

# Step 3: Check the operation and perform the corresponding action
if operation == '+':
    result = num1 + num2
    print(f"The result is: {result}")
elif operation == '-':
    result = num1 - num2
    print(f"The result is: {result}")
elif operation == '*':
    result = num1 * num2
    print(f"The result is: {result}")
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"The result is: {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Error: Invalid operation entered.")