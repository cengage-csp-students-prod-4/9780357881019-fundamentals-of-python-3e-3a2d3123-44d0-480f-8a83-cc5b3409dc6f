"""
Program: sum.py
Author: Reggie

This program accepts numbers from the user
and calculates their sum and average.
The user can press Enter to finish.
"""

# Create a list to store the numbers
numbers = []

# Get numbers from the user
while True:
    entry = input("Enter a number or press Enter to quit: ")

    if entry == "":
        break

    number = float(entry)
    numbers.append(number)

# Calculate the sum and average
if len(numbers) > 0:
    total = sum(numbers)
    average = total / len(numbers)

    # Display the results
    print("\nThe sum is", total)
    print("The average is", average)
else:
    print("\nNo numbers were entered.")
