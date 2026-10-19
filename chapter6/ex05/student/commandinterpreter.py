def printMenu(menu):
    """Displays the menu options with numbers."""
    for index in range(len(menu)):
        print(index + 1, menu[index])


def acceptCommand(numberOfOptions):
    """Gets a valid command number from the user."""
    while True:
        try:
            command = int(input("Enter a number: "))

            if 1 <= command <= numberOfOptions:
                return command
            else:
                print("Error: Please enter a number from 1 to",
                      numberOfOptions)

        except ValueError:
            print("Error: Please enter a valid number.")


def performCommand(command, menu):
    """Displays the selected command."""
    print("Command =", menu[command - 1])


def main():
    """Displays the menu and processes commands until Quit."""
    menu = ["Open", "Save", "Compile", "Run", "Quit"]

    while True:
        printMenu(menu)
        command = acceptCommand(len(menu))
        performCommand(command, menu)

        if menu[command - 1] == "Quit":
            print("Have a nice day!")
            break


if __name__ == "__main__":
    main()
