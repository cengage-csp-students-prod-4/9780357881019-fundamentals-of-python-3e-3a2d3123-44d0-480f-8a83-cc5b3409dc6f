import math


def drawCircle(t, x, y, radius):
    """Draw a circle centered at (x, y) with the given radius."""
    distance = 2.0 * math.pi * radius / 120.0

    # Start at the circle's right edge without drawing a line to it.
    t.penup()
    t.goto(x + radius, y)
    t.setheading(90)
    t.pendown()

    # Each turn is 3 degrees; 120 turns make one full 360-degree circle.
    for _ in range(120):
        t.left(3)
        t.forward(distance)