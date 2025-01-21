# from turtle import Turtle, Screen

# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color('green')
# timmy.forward(100)


# my_screen = Screen()
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Chespin", "Quilladin", "Chesnaught"])
table.add_column("Type", ["Grass", "Water", "Grass"])

table.align["Pokemon Name"] = "l"

print(table)