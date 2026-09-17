"""
Program: momentum.py
Author: Reggie

This program calculates an object's momentum
using its mass and velocity.
"""

# Ask the user for the mass and velocity
mass = float(input("Enter the object's mass: "))
velocity = float(input("Enter the object's velocity: "))

# Calculate momentum
momentum = mass * velocity

# Display the result
print("The object's momentum is", momentum)