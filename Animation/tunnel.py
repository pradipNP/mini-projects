import turtle
import colorsys

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Infinite Zoom Tunnel")
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.width(2)

# Tunnel parameters
num_circles = 25
circles = [i * 20 for i in range(num_circles)]
h = 0

while True:
    t.clear()

    for i in range(num_circles):
        radius = circles[i]

        # Color shift
        r, g, b = colorsys.hsv_to_rgb((h + i * 0.04) % 1, 1, 1)
        t.pencolor(r, g, b)

        # Draw circle
        t.penup()
        t.goto(0, -radius)
        t.pendown()
        t.circle(radius)

        # Move circle forward (Zoom effect)
        circles[i] -= 2

        # Recycle circle to back of tunnel
        if circles[i] < 5:
            circles[i] = num_circles * 20

    h += 0.002
    screen.update()