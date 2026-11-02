"""Displays a tax calculator with a graphical user interface."""

from breezypythongui import EasyFrame


# Constants from the Chapter 2 tax calculator
TAX_RATE = 0.20
STANDARD_DEDUCTION = 10000.0
DEPENDENT_DEDUCTION = 3000.0


class TaxForm(EasyFrame):
    """Displays a window for calculating income tax."""

    def __init__(self):
        """Sets up the labels, fields, and Compute button."""
        EasyFrame.__init__(self, title="Tax Calculator")

        self.addLabel(text="Gross income", row=0, column=0)
        self.grossIncomeField = self.addFloatField(
            value=0.0, row=0, column=1, width=15)

        self.addLabel(text="Dependents", row=1, column=0)
        self.dependentsField = self.addIntegerField(
            value=0, row=1, column=1, width=10)

        self.addButton(text="Compute", row=2, column=0,
                       columnspan=2, command=self.computeTax)

        self.addLabel(text="Total tax", row=3, column=0)
        self.taxField = self.addFloatField(
            value=0.0, row=3, column=1, width=15,
            precision=2, state="readonly")

    def computeTax(self):
        """Reads the inputs, calculates the tax, and displays it."""
        try:
            grossIncome = self.grossIncomeField.getNumber()
            numDependents = self.dependentsField.getNumber()
        except ValueError:
            self.messageBox(title="Input error",
                            message="Enter valid numbers in both input fields.")
            return

        if grossIncome < 0 or numDependents < 0:
            self.messageBox(title="Input error",
                            message="Income and dependents cannot be negative.")
            return

        taxableIncome = (grossIncome - STANDARD_DEDUCTION
                         - DEPENDENT_DEDUCTION * numDependents)
        incomeTax = taxableIncome * TAX_RATE
        self.taxField.setNumber(incomeTax)


def main():
    """Opens the tax calculator window."""
    TaxForm().mainloop()


if __name__ == "__main__":
    main()
