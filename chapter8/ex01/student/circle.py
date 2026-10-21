
import math
from turtle import Turtle

def drawCircle(t, x, y, radius):
    """Draws a circle using the given center point and radius."""
    t.up()
    t.goto(x, y - radius)
    t.setheading(0)
    t.down()

    distance = 2.0 * math.pi * radius / 120.0

    for count in range(120):
        t.forward(distance)
        t.left(3)

def main():
    t = Turtle()
    drawCircle(t, 0, 0, 50)
    t.hideturtle()

if __name__ == "__main__":
    main()
