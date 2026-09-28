# Get the message and distance
message = input("Enter a message: ")
distance = int(input("Enter the distance value: "))

# Create an empty string
encrypted = ""

# Encrypt the message
for char in message:
    code = ord(char)
    newCode = 32 + (code - 32 + distance) % 95
    encrypted = encrypted + chr(newCode)

# Display the encrypted message
print(encrypted)