
"""
File: bouncywithgui.py
Chapter 9 - Programming Exercise 2
Calculates the total distance traveled by a bouncing ball.
"""

from breezypythongui import EasyFrame


class Bouncy(EasyFrame):
    """Displays a bouncing ball calculator."""

    def __init__(self):
        """Sets up the window and its components."""
        EasyFrame.__init__(self, title="Bouncy")

        self.addLabel(text="Initial height", row=0, column=0)
        self.heightField = self.addFloatField(
            value=0.0, row=0, column=1)

        self.addLabel(text="Bounciness index", row=1, column=0)
        self.indexField = self.addFloatField(
            value=0.0, row=1, column=1)

        self.addLabel(text="Number of bounces", row=2, column=0)
        self.bouncesField = self.addIntegerField(
            value=0, row=2, column=1)

        self.addButton(text="Compute", row=3, column=0,
                       columnspan=2, command=self.compute)

        self.addLabel(text="Total distance", row=4, column=0)
        self.distanceField = self.addFloatField(
            value=0.0, row=4, column=1,
            precision=5, state="readonly")

    def compute(self):
        """Calculates the total distance traveled."""
        try:
            height = self.heightField.getNumber()
            index = self.indexField.getNumber()
            bounces = self.bouncesField.getNumber()

            if height < 0 or index < 0 or bounces < 0:
                self.messageBox(
                    title="Input Error",
                    message="Values cannot be negative.")
                return

            totalDistance = height

            for count in range(bounces):
                height = height * index
                totalDistance += height

                if count < bounces - 1:
                    totalDistance += height

            self.distanceField.setNumber(totalDistance)

        except ValueError:
            self.messageBox(
                title="Input Error",
                message="Please enter valid numbers.")


def main():
    """Opens the bouncing ball calculator."""
    Bouncy().mainloop()


if __name__ == "__main__":
    main()
