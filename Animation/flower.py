import turtle
import colorsys

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Satisfying Infinity Flower")
screen.tracer(0)

t = turtle.Turtle()
t.speed(0)
t.width(2)
t.hideturtle()

h = 0
length = 0

while True:
    r, g, b = colorsys.hsv_to_rgb(h, 1, 1)
    t.pencolor(r, g, b)

    t.forward(length * 0.3)
    t.left(59)

    length += 0.1
    h += 0.001

    screen.update()