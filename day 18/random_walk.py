''' Draw a random walk with the use of the Turtle Graphic Class
    https://en.wikipedia.org/wiki/Random_walk
    
    The exercise is:
    1. Draw a continuous random walk
    2. Make the line each thicker everytime
    3. Change the color of the line 
    4. Speed up the walk
'''

# Import modules
from turtle import Turtle, Screen
from random import choice

# Create the object
turtle = Turtle()


# Variable for a list of colors
colors = ['green', 'blue', 'yellow', 'red', 'brown', 'purple', 'SeaGreen']

# List with directions
directions = [0, 90, 180, 270]

# Create the pensize
turtle.pensize(15)

# Accelerate more speed
turtle.speed("fastest")

# Create the random walk
for _ in range(200):
    turtle.color(choice(colors))
    turtle.forward(30)
    turtle.setheading(choice(directions))








# Add it to the screen
screen = Screen()

# Exit the screen
screen.exitonclick()
