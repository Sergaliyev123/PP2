# Initialize sums for even and odd numbers
sum_even = 0
sum_odd = 0

# Loop through numbers from 1 to 100
for number in range(1, 101):
    if number % 2 == 0:
        sum_even += number  # Add to even sum if number is even
    else:
        sum_odd += number   # Add to odd sum if number is odd

# Output the results
print("Sum of even numbers from 1 to 100:", sum_even)
print("Sum of odd numbers from 1 to 100:", sum_odd)