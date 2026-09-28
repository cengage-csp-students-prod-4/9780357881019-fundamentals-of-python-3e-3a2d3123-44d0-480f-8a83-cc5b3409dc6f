"""
Program: encrypt.py
Author: Reggie

This program encrypts a message using a Caesar cipher.
The user enters a message and a distance value.
The program shifts each printable character to create
an encrypted message.
"""

# Get the message and distance from the user
message = input("Enter a message: ")
distance = int(input("Enter the distance value: "))

# Create an empty string for the encrypted message
encrypted = ""

# Encrypt each character
for char in message:
    code = ord(char)
    newCode = 32 + (code - 32 + distance) % 95
    encrypted += chr(newCode)

# Display the encrypted message
print(encrypted)