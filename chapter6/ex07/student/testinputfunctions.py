
def inputFloat(prompt):
    """Guarantees that the user inputs a floating-point number.

    Returns the number as a float.
    """
    while True:
        theString = input(prompt)

        try:
            return float(theString)
        except ValueError:
            print("Error: The input must be a number.")


if __name__ == "__main__":
    number = inputFloat("Enter a number: ")
    print("The number is", number)
