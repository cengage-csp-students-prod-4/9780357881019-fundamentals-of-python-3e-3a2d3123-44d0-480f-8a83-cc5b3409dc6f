"""
Program: right.py
Author: Reggie

This program determines whether a triangle
is a right triangle using the Pythagorean theorem.
"""

# Ask the user for the three sides
side1 = float(input("Enter the first side: "))
side2 = float(input("Enter the second side: "))
side3 = float(input("Enter the third side: "))

# Sort the sides from smallest to largest
sides = sorted([side1, side2, side3])

# Assign the sides
a = sides[0]
b = sides[1]
c = sides[2]

# Check if the triangle is a right triangle
if a ** 2 + b ** 2 == c ** 2:
    print("\nThe triangle is a right triangle.")
else:
    print("\nThe triangle is not a right triangle.")