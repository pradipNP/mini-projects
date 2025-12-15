import turtle
import random
import time

# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Catch the Falling Ball")

screen.tracer(0)

# Basket
basket = turtle.Turtle()
basket.shape("square")
basket.color("white")
basket.shapesize(stretch_wid=1, stretch_len=4)
basket.penup()
basket.goto(0, -250)

# Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(random.randint(-280, 280), 280)

# Score
score = 0
score_display = turtle.Turtle()
score_display.color("yellow")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Score: 0", align="center", font=("Arial", 16, "bold"))

# Movement
def move_left():
    x = basket.xcor()
    if x > -250:
        basket.setx(x - 30)

def move_right():
    x = basket.xcor()
    if x < 250:
        basket.setx(x + 30)

screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

# Main game loop
ball_speed = 4

while True:
    screen.update()
    time.sleep(0.02)

    # Ball fails
    ball.sety(ball.ycor() - ball_speed)

    # Check for catch
    if ball.ycor() < -230 and abs(ball.xcor() - basket.xcor()) < 50:
        score += 1
        score_display.clear()
        score_display.write(f"Score: {score}", align="center", font=("Arial", 16, "bold"))
        ball.goto(random.randint(-280, 280), 280)
        ball_speed += 0.3 # Increase difficulty

    # Ball misses
    if ball.ycor() < -300:
        score_display.goto(0, 0)
        score_display.write("GAME OVER", align="center", font=("Arial", 24, "bold"))
        break

turtle.done()