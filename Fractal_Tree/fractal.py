import turtle 
import random

#Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Fractal Tree")

#Create the turtle
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(7)
pen.left(90)

#Function to draw a branch
def draw_branch(branch_length, pen_size):
    if branch_length < 15:
        pen.color(random.choice(["spring green", "lawn green"]))
        pen.stamp()
        pen.color("saddle brown")
        return
    
    pen.pensize(pen_size)
    pen.color("saddle brown")
    pen.forward(branch_length)

    # Randomize new branch angles and lengths
    new_length = branch_length * random.uniform(0.7, 0.9)
    right_angle = random.randint(15, 35)
    left_angle = random.randint(15, 35)

    # Right branch
    pen.right(right_angle)
    draw_branch(new_length, pen_size * 0.7)

    # Left branch
    pen.left(right_angle + left_angle)
    draw_branch(new_length, pen_size * 0.7)

    # Return to the original position and angle
    pen.right(left_angle)
    pen.backward(branch_length)

# Position the turtle
pen.penup()
pen.goto(0, -300)
pen.pendown()

#Start drawing the tree
draw_branch(120, 10)

#Finish
turtle.done()