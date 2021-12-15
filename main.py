
from turtle import Turtle, Screen

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

blaze_the_turtle = Turtle()

print(blaze_the_turtle)
blaze_the_turtle.resizemode("auto")

for i in range(50):
    blaze_the_turtle.shape("square")
    blaze_the_turtle.pencolor("red")
    blaze_the_turtle.forward(10 + i)
    blaze_the_turtle.penup()
    blaze_the_turtle.forward(20 + i)
    blaze_the_turtle.shape("circle")
    blaze_the_turtle.pencolor("blue")
    blaze_the_turtle.pendown()
    blaze_the_turtle.forward(30 + i)
    blaze_the_turtle.penup()
    # blaze_the_turtle.right(90)
    blaze_the_turtle.shape("arrow")
    blaze_the_turtle.pencolor("green")
    blaze_the_turtle.pendown()
    blaze_the_turtle.forward(30 + i)
    blaze_the_turtle.right(90)
    # blaze_the_turtle.forward(100 * i)
    # blaze_the_turtle.right(90)
    # blaze_the_turtle.forward(100 * i)
    # blaze_the_turtle.right(90)
    # blaze_the_turtle.forward(100 * i)












my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()