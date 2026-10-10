# Ask for the input file name
fileName = input("Enter the input file name: ")

# Open and read the file
with open(fileName, "r") as file:
    text = file.read()

# Get the unique words
words = text.split()
uniqueWords = set(words)

# Print the words in alphabetical order
for word in sorted(uniqueWords, key=str.lower):
    print(word.title())