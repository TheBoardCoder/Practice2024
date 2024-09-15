# Randolph Paul 4/8/2024 randolphPaul_lab10
# The purpose of this program is to draw a star pattern

# Import Turtle
import turtle

# Create turtle object
t = turtle.Turtle()

# Set the speed of the turtle
t.speed(3)

# Define the constants
points = 8
length = 200
rotation_angle = 135

# Draw the star
for i in range(points):
    t.forward(length)
    t.left(rotation_angle)

# Keep the window open
turtle.done()
