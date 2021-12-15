
from turtle import Turtle, Screen

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

blaze_the_turtle = Turtle()

print(blaze_the_turtle)
blaze_the_turtle.shape("arrow")
blaze_the_turtle.color("blue")
blaze_the_turtle.resizemode("auto")

for _ in range(4):
    blaze_the_turtle.forward(100)
    blaze_the_turtle.right(90)
    # blaze_the_turtle.forward(100 * i)
    # blaze_the_turtle.right(90)
    # blaze_the_turtle.forward(100 * i)
    # blaze_the_turtle.right(90)
    # blaze_the_turtle.forward(100 * i)












my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()