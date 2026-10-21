import math


def drawCircle(t, x, y, radius):
    distance = 2.0 * math.pi * radius / 120.0

    t.penup()
    t.goto(x + radius, y)
    t.setheading(90)
    t.pendown()

    for _ in range(120):
        t.left(3)
        t.forward(distance)