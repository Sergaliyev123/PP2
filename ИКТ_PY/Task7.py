# Ask the user to enter a number
number = int(input("Enter a number to calculate its factorial: "))

# Initialize factorial to 1
factorial = 1

# Check if the number is negative, zero, or positive
if number < 0:
    print("Factorial is not defined for negative numbers.")
elif number == 0:
    print("The factorial of 0 is 1.")
else:
    # Calculate the factorial
    for i in range(1, number + 1):
        factorial *= i
    print(f"The factorial of {number} is {factorial}")