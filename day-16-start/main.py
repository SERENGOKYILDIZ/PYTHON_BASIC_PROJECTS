# from turtle import Turtle, Screen
#
# kaplumbaga = Turtle()
# print(kaplumbaga)
# kaplumbaga.shape("turtle")
# kaplumbaga.color("black", "red")
# kaplumbaga.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvwidth)
# print(my_screen.canvheight)
# my_screen.exitonclick()
#
from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
table.align="r"
print(table)