from turtle import Turtle, Screen
import random

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

blaze_the_turtle = Turtle()

print(blaze_the_turtle)
blaze_the_turtle.resizemode("auto")
colours = ["lightgreen", "DodgerBlue", "Navy", "Magenta", "Yellow", "SpringGreen", "Crimson",
           "MediumVioletRed", "#0000FF", "Gold", "cyan", "deeppink"]


def draw_shape(side_count):
    angle = 360 / side_count
    for _ in range(side_count):
        blaze_the_turtle.forward(100)
        blaze_the_turtle.right(angle)


for i in range(3, 15):
    blaze_the_turtle.color(random.choice(colours))
    draw_shape(i)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
