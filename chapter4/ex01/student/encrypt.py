
"""
Program: encrypt.py
Author: Reggie

This program encrypts a message using a Caesar cipher.
"""

# Get the message from the user
message = input("Enter a message: ")

# Get the distance value
distance = int(input("Enter the distance value: "))

# Create an empty string
encrypted_message = ""

# Go through each character in the message
for character in message:

    # Get the ASCII value and shift it
    code = ord(character)
    new_code = (code + distance) % 128

    # Convert the new value back to a character
    encrypted_character = chr(new_code)

    # Add it to the encrypted message
    encrypted_message += encrypted_character

# Display the encrypted message
print(encrypted_message)