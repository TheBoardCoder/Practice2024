#Randolph Paul 3/20/2024 randolphPaul_lab03
#The purpose of this program is to draw two shapes from chapter 2 exercise #15 in the textbook "Starting out with Python".

#import the modules
import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.title("chapter 2 exercise #15")
screen.bgcolor("white")

#Set constants
oneHundred = 100
fortyFive = 45
ninety = 90
fifty = 50
oneThrityFive = 135
negativeOneHundred = -100
zero = 0
twoHundred = 200

#calculate the diagnols of the square
halfSquareDiagnol = math.sqrt(5000)
fullSquareDiagnol = math.sqrt(20000)


# Create a turtle for drawing
t = turtle.Turtle()
t.speed(3)

# Draw the picture
t.left(fortyFive)
t.forward(oneHundred)
t.right(ninety)
t.forward(oneHundred)
t.right(ninety)
t.forward(oneHundred)
t.right(ninety)
t.forward(twoHundred)
t.left(ninety)
t.forward(oneHundred)
t.left(ninety)
t.forward(oneHundred)
t.left(ninety)
t.forward(oneHundred)

# Draw the second picture
t.penup()
t.goto(zero, negativeOneHundred)
t.pendown()
t.right(fortyFive)
t.forward(fifty)
t.right(ninety)
t.forward(oneHundred)
t.left(ninety)
t.forward(fifty)
t.left(ninety)
t.forward(fifty)
t.left(ninety)
t.forward(oneHundred)
t.right(ninety)
t.forward(fifty)
t.right(ninety)
t.forward(fifty)
t.right(fortyFive)
t.forward(halfSquareDiagnol)
t.right(oneThrityFive)
t.forward(oneHundred)
t.left(oneThrityFive)
t.forward(halfSquareDiagnol)
t.left(fortyFive)
t.forward(fifty)
t.left(oneThrityFive)
t.forward(fullSquareDiagnol)



# Hide the turtle and display the result
t.hideturtle()
turtle.done()
