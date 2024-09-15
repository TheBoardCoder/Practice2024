# Randolph Paul 4/15/2024 randolphPaul_lab14
# The purpose of this program is to draw and design a snowman
# Note for the scarf design it is partially transparent to show it wraps around the snowman

# Import the turtle module
import turtle

# Set global constants
neg_one_fifty = -150
neg_fifty_seven = -57
neg_thirty = -30
neg_fifteen = -15
neg_ten = -10
neg_eight = -8
zero = 0
two = 2
three = 3
five = 5
eight = 8
ten = 10
twenty = 20
thirty = 30
thirty_three = 33
thirty_five = 35
forty = 40
forty_five = 45
fifty = 50
sixty = 60
seventy = 70
seventy_five = 75
eighty_four = 84
ninety = 90
ninety_five = 95
one_hundred = 100
one_ten = 110
one_fifteen = 115
one_forty_five = 145
one_eighty = 180


# Create the base of he snowman
def draw_base():
    turtle.penup()
    turtle.goto(zero, neg_one_fifty)
    turtle.pendown()
    turtle.circle(seventy)


# Create the snowman's mid section
def draw_mid_section():
    turtle.penup()
    turtle.goto(zero, neg_ten)
    turtle.pendown()
    turtle.circle(forty)


# Create the snowman's arms
def draw_arms():
    turtle.penup()
    turtle.goto(neg_fifty_seven, forty)
    turtle.pendown()
    turtle.right(twenty)
    turtle.forward(twenty)
    turtle.penup()
    turtle.goto(forty, thirty_three)
    turtle.pendown()
    turtle.left(thirty_five)
    turtle.forward(thirty_five)
    turtle.penup()
    turtle.goto(neg_fifty_seven, forty)
    turtle.pendown()
    turtle.left(ninety_five)
    turtle.forward(twenty)
    turtle.right(twenty)
    turtle.forward(ten)
    turtle.right(one_eighty)
    turtle.forward(ten)
    turtle.right(one_ten)
    turtle.forward(ten)
    turtle.penup()
    turtle.goto(forty, thirty_three)
    turtle.pendown()
    turtle.right(one_forty_five)
    turtle.forward(thirty_five)
    turtle.left(forty_five)
    turtle.forward(ten)
    turtle.left(one_eighty)
    turtle.forward(ten)
    turtle.left(one_fifteen)
    turtle.forward(ten)


# Create the snowman's head
def draw_head():
    turtle.penup()
    turtle.goto(zero, seventy)
    turtle.pendown()
    turtle.circle(twenty)

    # Eyes
    turtle.penup()
    turtle.goto(neg_eight, ninety)
    turtle.pendown()
    turtle.circle(three)

    turtle.penup()
    turtle.goto(eight, ninety)
    turtle.pendown()
    turtle.circle(three)

    # Mouth
    turtle.penup()
    turtle.goto(neg_ten, eighty_four)
    turtle.pendown()
    turtle.forward(twenty)


# Create the snowman's hat
def draw_hat():
    turtle.penup()
    turtle.goto(neg_fifteen, one_ten)
    turtle.pendown()
    turtle.color("black")
    turtle.begin_fill()
    for _ in range(two):
        turtle.forward(thirty)
        turtle.left(ninety)
        turtle.forward(twenty)
        turtle.left(ninety)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(neg_thirty, one_hundred)
    turtle.pendown()
    turtle.color("black")
    turtle.begin_fill()
    for _ in range(two):
        turtle.forward(sixty)
        turtle.left(ninety)
        turtle.forward(ten)
        turtle.left(ninety)
    turtle.end_fill()


# Create the snowman's scarf
def draw_scarf():
    turtle.penup()
    turtle.goto(neg_fifteen, seventy_five)
    turtle.pendown()
    turtle.color("red")
    turtle.begin_fill()
    turtle.setheading(zero)
    turtle.forward(thirty)
    turtle.right(ninety)
    turtle.forward(ten)
    turtle.right(ninety)
    turtle.forward(thirty)
    turtle.right(ninety)
    turtle.forward(ten)
    turtle.right(ninety)
    turtle.end_fill()
    turtle.goto(ten, seventy_five)
    turtle.right(sixty)
    turtle.forward(thirty)
    turtle.right(ninety)
    turtle.forward(ten)
    turtle.right(ninety)
    turtle.forward(thirty)
    turtle.right(ninety)
    turtle.forward(ten)
    turtle.end_fill()


# Create the snowman's buttons
def draw_buttons():
    turtle.penup()
    turtle.goto(zero, fifty)
    turtle.pendown()
    turtle.color("black")
    turtle.dot(ten)
    turtle.penup()
    turtle.goto(zero, thirty)
    turtle.pendown()
    turtle.dot(ten)
    turtle.penup()
    turtle.goto(zero, ten)
    turtle.pendown()
    turtle.dot(ten)


# Set the turtle speed and call the other functions
def main():
    turtle.speed(five)
    turtle.hideturtle()
    draw_base()
    draw_mid_section()
    draw_head()
    draw_hat()
    draw_arms()
    draw_buttons()
    draw_scarf()
    turtle.done()


# Entry point of the program
main()
