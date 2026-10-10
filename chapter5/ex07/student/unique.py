# Ask for the input file name
filename = input("Enter the input file name: ")

# Read the file and collect the unique words
uniqueWords = set()

with open(filename, "r") as file:
    for line in file:
        words = line.split()

        for word in words:
            uniqueWords.add(word.lower().strip(".,!?;:\"'()[]{}"))

# Print the words in alphabetical order
for word in sorted(uniqueWords):
    print(word)