# Create a circle
# Change the direction of the circle into a bigger circle
# Change the color of every circle

# Import modules
import turtle as t
import random

# Create the object
tim = t.Turtle()

# Set the colormode
t.colormode(255)

# Create function to generate random rgb colors
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    
    rgb = (r, g, b)
    
    return rgb

# Change the pensize and speed
tim.speed("fastest")

# Create the spirograph
for _ in range(200):
    tim.color(random_color())
    tim.circle(120, 360)
    tim.left(10)


