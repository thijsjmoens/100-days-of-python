from turtle import Turtle, Screen
from random import choice

# Create the object
t = Turtle()

# Create a list of colors
colors = ["red", "green", "blue", "yellow", "purple", "brown", "grey", "black", "bisque3", "bisque2"]

# Change the shape
# t.shape("turtle")

# Change the color
# t.color("green")

# Draw a square
# for _ in range(4):
#     t.forward(100)
#     t.right(90)


# Draw a dashed line
# for _ in range(15):
#     t.forward(10)
#     t.penup()
#     t.forward(10)
#     t.pendown()


# Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon

# Create variable for corners
corners = 3

# Create a loop for 8 figures
for _ in range(8):
    # Pick a random color
    t.color(choice(colors))

    # Create inside loop to draw the figure
    for _ in range(corners):
        t.forward(100)
        t.right(360/corners)
    
    # Increase number of corners
    corners += 1
















screen = Screen()

screen.exitonclick()
