"""
Program: numberlines.py
Author: Reggie

This program reads a source file and copies its
contents to another file with numbered lines.
"""

# Ask the user for the file names
inputFile = input("Enter the input file name: ")
outputFile = input("Enter the output file name: ")

# Open the input and output files
with open(inputFile, "r") as infile:
    with open(outputFile, "w") as outfile:

        # Read and number each line
        lineNumber = 1

        for line in infile:
            outfile.write(f"{lineNumber:4}> {line}")
            lineNumber += 1