#
# from turtle import Turtle, Screen
#
# blaze = Turtle()
#
# print(blaze)
# blaze.shape("turtle")
# blaze.color("green")
#
#
# my_screen = Screen()
# print(my_screen.canvheight)
# blaze.position()
# blaze.forward(95)
# blaze.position()
# blaze.right(45)
# blaze.forward(-75)
# blaze.lt(90)
# blaze.forward(-75)
# blaze.position()
#
# my_screen.exitonclick()

from prettytable import PrettyTable

x = PrettyTable()
x.add_column("Names", ["Benjamin", "Joy", "Emmanuel", "Shepherd", "Mikael"])
x.add_column("Gender", [49, 39, 9, 6, 3])
x.align = 'l'
print(x)
print(x.get_string(start=1, end=3))
print(x.get_string(sortby="Gender"))
print(x.get_html_string(attributes={"id":"my_table", "class":"red_table"}))

