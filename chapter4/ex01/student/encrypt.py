
"""
Program: encrypt.py
Author: Reggie

This program encrypts a message using a Caesar cipher.
The user enters a message and a distance value.
"""

# Get a message from the user
message = input("Enter a message: ")

# Get the distance value
distance = int(input("Enter the distance value: "))

# Create an empty string for the encrypted message
encrypted_message = ""

# Go through each character in the message
for character in message:

    # Get the ASCII value of the character
    code = ord(character)

    # Shift the character by the distance value
    new_code = code + distance

    # Keep the character within the printable ASCII range
    if new_code > 126:
        new_code = 32 + (new_code - 127) % 95

    # Convert the new ASCII value back to a character
    encrypted_character = chr(new_code)

    # Add the encrypted character to the message
    encrypted_message = encrypted_message + encrypted_character

# Display the encrypted message
print(encrypted_message)