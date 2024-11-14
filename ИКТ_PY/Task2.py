while True:
    # Ask the user to enter the first number or 'q' to quit
    num1_input = input("Enter the first number (or 'q' to quit): ")
    if num1_input.lower() == 'q':
        print("Exiting the calculator. Goodbye!")
        break
    try:
        num1 = float(num1_input)
    except ValueError:
        print("Error: Please enter a valid number.")
        continue
    
    # Ask the user to enter the second number
    num2_input = input("Enter the second number: ")
    try:
        num2 = float(num2_input)
    except ValueError:
        print("Error: Please enter a valid number.")
        continue

    # Ask the user to enter the operation
    operation = input("Enter the operation (+, -, *, /): ")

    # Perform the operation and handle errors
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
    
    # Blank line for separation between calculations
    print()