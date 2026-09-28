"""
Program: encrypt.py
Author: Reggie

This program encrypts a message using a Caesar cipher.
The user enters a message and a distance value.
"""

# Get the message and distance
message = input("Enter a message: ")
distance = int(input("Enter the distance value: "))

# Create an empty string
encrypted = ""

# Encrypt each character
for char in message:
    code = ord(char)

    # Shift characters within the printable ASCII range
    newCode = 32 + ((code - 32 + distance) % 95)

    encrypted += chr(newCode)

# Display the encrypted message
print(encrypted)