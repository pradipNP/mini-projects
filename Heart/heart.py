import turtle
import math
import time

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Glowing Heart - Turtle")

heart = turtle.Turtle()
heart.speed(0)
heart.width(3)
heart.hideturtle()

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

def draw_heart(scale, color):
    heart.color(color)
    heart.penup()
    heart.goto(0, -40 * scale)
    heart.pendown()

    heart.begin_fill()
    for t in range(0, 360):
        angle = math.radians(t)
        x = 16 * math.sin(angle) ** 3
        y = (
            13 * math.cos(angle)
            - 5 * math.cos(2 * angle)
            - 2 * math.cos(3 * angle)
            - math.cos(4 * angle)
        )
        heart.goto(x * scale * 10, y * scale * 10)
    heart.end_fill()

# Animation loop
while True:
    heart.clear()
    for i in range(5):
        draw_heart(1 + i * 0.05, colors[i])
        time.sleep(0.2)