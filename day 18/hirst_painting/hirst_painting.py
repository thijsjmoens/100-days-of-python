# import colorgram

# number_of_colors = 38

# # Extract 6 colors from an image.
# colors = colorgram.extract('hirst.jpg', number_of_colors)

# rgb_list = []

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b    
    
#     new_color = (r, g, b)
        
    
#     rgb_list.append(new_color)
        
        
# print(rgb_list)

''' 
1. Painting must be 10 rows by 10 columns
2. Dots should be of size 20 and 50 spaces
3. 
'''

# Import modules
import turtle as t
from turtle import Screen
from random import choice

# Create the object
tim = t.Turtle()

# Set the colormode
t.colormode(255)

# List with all colors form Hirst painting
color_list  = [(234, 225, 83), (195, 8, 69), (231, 54, 132), (194, 164, 15), (112, 178, 214), (199, 77, 15), (216, 162, 101), (34, 187, 112), (29, 104, 167), (14, 23, 64), (20, 29, 168), (212, 136, 175), (231, 224, 7), (197, 34, 130), (15, 181, 210), (231, 167, 197), (126, 189, 163), (10, 48, 29), (40, 131, 75), (141, 217, 203), (61, 22, 10), (60, 13, 27), (108, 91, 210), (235, 64, 34), (131, 217, 230), (183, 17, 9), (12, 96, 52), (166, 182, 235), (242, 167, 153), (10, 85, 102), (252, 5, 48), (66, 94, 8), (248, 13, 10), (14, 48, 249)]

# t.setworldcoordinates(1, 1, 20, 20)


# Set the starting position
starting_position = 0

for _ in range(10):
    
    tim.penup()
    tim.goto(0, starting_position)
    tim.pendown()
    
    for _ in range(10):  
        tim.color(choice(color_list))
        tim.dot(20)
        tim.penup()
        tim.forward(50)
        tim.pendown()
        
    starting_position += 70







# Add it to the screen
screen = Screen()

# Exit the screen
screen.exitonclick()