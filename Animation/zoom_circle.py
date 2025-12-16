import turtle
import colorsys
import math

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Satisfying Zooming Circles")
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.width(2)

h = 0
phase = 0

while True:
    t.clear()

    zoom = 120 + 60 * math.sin(phase)  # zoom in & out

    for i in range(10):
        r, g, b = colorsys.hsv_to_rgb((h + i * 0.05) % 1, 1, 1)
        t.pencolor(r, g, b)

        t.penup()
        t.goto(0, -zoom - i * 20)
        t.pendown()
        t.circle(zoom + i * 20)

    phase += 0.03
    h += 0.003

    screen.update()
