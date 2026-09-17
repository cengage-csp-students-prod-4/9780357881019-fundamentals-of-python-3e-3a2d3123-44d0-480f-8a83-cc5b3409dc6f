"""
Program: sphere.py
Author: Reggie

This program calculates the diameter, circumference,
surface area, and volume of a sphere using the radius
provided by the user.
"""

import math

# Ask the user for the radius
radius = float(input("Enter the sphere's radius: "))

# Calculate the measurements
diameter = 2 * radius
circumference = 2 * math.pi * radius
surface_area = 4 * math.pi * radius ** 2
volume = (4 / 3) * math.pi * radius ** 3

# Display the results
print("Diameter    :", diameter)
print("Circumference:", circumference)
print("Surface area:", surface_area)
print("Volume      :", volume)