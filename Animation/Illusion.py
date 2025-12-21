import turtle
import colorsys

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Colorful Illusion Animation")
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.width(2)

# Parameters
num_squares = 40
sizes = [i * 5 for i in range(1, num_squares + 1)]
angles = [i * 10 for i in range(num_squares)]
h = 0

while True:
    t.clear()

    for i in range(num_squares):
        size = sizes[i]
        angle = angles[i]

        r, g, b = colorsys.hsv_to_rgb((h + i / num_squares) % 1.0, 1.0, 1.0)
        t.pencolor(r, g, b)

        t.penup()
        t.goto(0, 0)
        t.setheading(angle)
        t.pendown()

        for _ in range(4):
            t.forward(size)
            t.right(90)
        
        # Illusion motion
        sizes[i] -= 2
        angles[i] += 1

        # Recycle squares
        if sizes[i] <= 0:
            sizes[i] = num_squares * 5
            angles[i] = 0
        

    h += 0.005
    screen.update() 