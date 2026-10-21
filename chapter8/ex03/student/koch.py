import turtle


def drawFractalLine(t, distance, angle, level):
    if level == 0:
        # At level 0, draw one straight line.
        t.setheading(angle)
        t.forward(distance)
    else:
        # Replace this line with four shorter lines that form a bump.
        third = distance / 3.0
        drawFractalLine(t, third, angle, level - 1)
        drawFractalLine(t, third, angle + 60, level - 1)
        drawFractalLine(t, third, angle - 60, level - 1)
        drawFractalLine(t, third, angle, level - 1)


def main():
    screen = turtle.Screen()
    screen.setup(700, 600)

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-100, 100)
    t.pendown()

    distance = 200
    level = 2

    # Draw the snowflake's three sides.
    drawFractalLine(t, distance, 0, level)
    drawFractalLine(t, distance, -120, level)
    drawFractalLine(t, distance, 120, level)

    screen.exitonclick()


if __name__ == "__main__":
    main()