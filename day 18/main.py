from turtle import Turtle, Screen

# Create the object
t = Turtle()

# Change the shape
t.shape("turtle")

# Change the color
t.color("green")

# Draw a square
# for _ in range(4):
#     t.forward(100)
#     t.right(90)


# Draw a dashed line
for _ in range(15):
    t.forward(10)
    t.penup()
    t.forward(10)
    t.pendown()

















screen = Screen()

screen.exitonclick()
