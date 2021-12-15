from turtle import Turtle, Screen
import random

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

blaze_the_turtle = Turtle()

print(blaze_the_turtle)
blaze_the_turtle.resizemode("auto")
colours = ["lightgreen", "DodgerBlue", "Navy", "Magenta", "Yellow", "SpringGreen", "Crimson",
           "MediumVioletRed", "#0000FF", "Gold", "cyan", "deeppink", "Blue", "PaleVioletRed"]
directions = [0, 45, 90, 135, 180, 225, 270]

for i in range(70):
    blaze_the_turtle.speed(i)
    blaze_the_turtle.pensize(i)
    blaze_the_turtle.color(random.choice(colours))
    blaze_the_turtle.forward(100)
    blaze_the_turtle.right(random.choice(directions))


my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
