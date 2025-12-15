import turtle
import math
import time

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Solar System Simulation")

screen.tracer(0)

# SUN
sun = turtle.Turtle()
sun.shape("circle")
sun.color("yellow")
sun.shapesize(2.5)
sun.penup()
sun.goto(0, 0)

# PLANETS CREATOR
def create_planet(color, size):
    planet = turtle.Turtle()
    planet.shape("circle")
    planet.color(color)
    planet.shapesize(size)
    planet.penup()
    return planet

# PLANETS
mercury = create_planet("gray", 0.4)
venus = create_planet("orange", 0.6)
earth = create_planet("blue", 0.6)
mars = create_planet("red", 0.5)
jupiter = create_planet("brown", 1.2)
saturn = create_planet("goldenrod", 1.0)
uranus = create_planet("light blue", 0.8)
neptune = create_planet("dark blue", 0.8)

# ORBIT RADII
radii = {
    mercury: 60,
    venus: 90,
    earth: 120,
    mars: 150,
    jupiter: 200,
    saturn: 240,
    uranus: 280,
    neptune: 320
}

# SLOWER SPEEDS
speeds = {
    mercury: 1.6,
    venus: 1.2,
    earth: 1.0,
    mars: 0.8,
    jupiter: 0.4,
    saturn: 0.3,
    uranus: 0.2,
    neptune: 0.15
}

angle = 0

# ANIMATION LOOP
while True:
    angle += 0.3

    for planet in radii:
        r = radii[planet]
        speed = speeds[planet]
        planet.goto(
            r * math.cos(math.radians(angle * speed)),
            r * math.sin(math.radians(angle * speed))
        )
    
    screen.update()
    time.sleep(0.01)