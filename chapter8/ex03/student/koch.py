
from turtle import Turtle

def drawFractalLine(t, distance, angle, level):
    """Draws one line of the Koch snowflake."""
    if level == 0:
        t.setheading(angle)
        t.forward(distance)
    else:
        distance = distance / 3.0
        drawFractalLine(t, distance, angle, level - 1)
        drawFractalLine(t, distance, angle + 60, level - 1)
        drawFractalLine(t, distance, angle - 60, level - 1)
        drawFractalLine(t, distance, angle, level - 1)

def main():
    t = Turtle()
    t.speed(0)

    distance = 200
    level = 2

    for angle in (0, -120, 120):
        drawFractalLine(t, distance, angle, level)

    t.hideturtle()
    t.getscreen().mainloop()

if __name__ == "__main__":
    main()
