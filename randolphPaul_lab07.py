# Randolph Paul 4/2/2024 randolphPaul_lab07
'''This program is a game where the user inputs an angle and speed in order to move an object to
hit a target. After each attempt the user will be given hints for where the target is.'''

# Hit the Target Game
import turtle

# Named constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
TARGET_LLEFT_X = 100
TARGET_LLEFT_Y = 250
TARGET_WIDTH = 25
FORCE_FACTOR = 30
PROJECTILE_SPEED = 1
NORTH = 90
SOUTH = 270
EAST = 0
WEST = 180
MAX_FORCE = 10
MIN_FORCE = 1
MAX_ANGLE = 360
MIN_ANGLE = 0
ANGLE_NEEDED = 67
FORCE_NEEDED = 9.8

# Setup the window.
turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

# Draw the target.
turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.goto(TARGET_LLEFT_X, TARGET_LLEFT_Y)
turtle.pendown()
turtle.setheading(EAST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(NORTH)
turtle.forward(TARGET_WIDTH)
turtle.setheading(WEST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(SOUTH)
turtle.forward(TARGET_WIDTH)
turtle.penup()

# Center the turtle.
turtle.goto(0, 0)
turtle.setheading(EAST)
turtle.showturtle()
turtle.speed(PROJECTILE_SPEED)

# Get the angle and force from the user.
print("""\nThis program is a game where the user inputs an angle and speed to move an object to hit a target.
After each attempt the user will be given hints for where the target is.""")
while True:
    try:
        angle = float(input("\nPlease enter the projectile's angle (0-360): "))
        if angle > MAX_ANGLE or angle < MIN_ANGLE:
            raise ValueError
        break
    except ValueError:
        print("Error: Please enter a valid number")
while True:
    try:
        force = float(input("Please enter the launch force (1-10): "))
        if force > MAX_FORCE or force < MIN_FORCE:
            raise ValueError
        break
    except ValueError:
        print("Error: Please enter a valid number")

# Calculate the distance.
distance = force * FORCE_FACTOR

# Set the heading.
turtle.setheading(angle)

# Launch the projectile.
turtle.pendown()
turtle.forward(distance)

# Did it hit the target?
if (turtle.xcor() >= TARGET_LLEFT_X and
        turtle.xcor() <= (TARGET_LLEFT_X + TARGET_WIDTH) and
        turtle.ycor() >= TARGET_LLEFT_Y and
        turtle.ycor() <= (TARGET_LLEFT_Y + TARGET_WIDTH)):
    print('\nTarget hit!')
else:
    #Give the user a hint
    print('\nYou missed the target:')
    if angle < ANGLE_NEEDED:
        print("Try a larger angle")
    elif angle > ANGLE_NEEDED:
        print("Try a smaller angle")
    else:
        print("The angle is correct")
    if force < FORCE_NEEDED:
        print("Use more force")
    elif force > FORCE_NEEDED:
        print("Use less force")
    else:
        print("The force is correct")

turtle.done()
